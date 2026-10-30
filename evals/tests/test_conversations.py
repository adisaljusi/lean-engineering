import argparse
import contextlib
import copy
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import conversations as flow
import runner

CASES = json.loads((runner.ROOT / 'workflows.json').read_text())


def good_judgment(case):
    data = {'scores': dict.fromkeys(runner.METRICS, 2),
            'reasons': dict.fromkeys(runner.METRICS, 'Synthetic test evidence'),
            'critical_failure': False, 'critical_reason': '', 'overall': 'Synthetic control'}
    return {'status': 'judged', **runner.validate_judgment(data),
            'criteria': [{'id': k, 'verdict': 'pass', 'evidence': 'Synthetic turn 1'} for k in case['criteria']]}


def args():
    return argparse.Namespace(model='test-subject', actor_model='test-user', judge_model='test-assessor',
                              timeout=60, turn_timeout=5, max_turns=8)


class ConversationTests(unittest.TestCase):
    def test_native_resume_preserves_session_and_rejects_stale_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workspace = root / 'workspace'; workspace.mkdir()
            runtime = root / 'runtime'; runtime.mkdir()
            commands = []

            def fake_command(argv, cwd, timeout, message):
                commands.append(argv)
                self.assertFalse((runtime / 'answer.txt').exists())
                (runtime / 'answer.txt').write_text('A new answer')
                return {'status': 'succeeded', 'stdout': json.dumps({'type': 'thread.started', 'thread_id': 'session-1'}) + '\n' +
                        json.dumps({'type': 'turn.completed', 'usage': {}}), 'stderr': ''}

            with patch.object(runner, 'command', side_effect=fake_command), \
                 patch.object(runner, 'sandbox_command', side_effect=lambda w, r, argv, **kw: argv):
                first = flow.subject_turn(workspace, runtime, 'first', 'test', 5)
                second = flow.subject_turn(workspace, runtime, 'second', 'test', 5, first['session_id'])
            self.assertEqual(second['status'], 'succeeded')
            self.assertNotIn('--ephemeral', commands[0])
            self.assertIn('resume', commands[1])
            self.assertIn('session-1', commands[1])

    def test_native_trace_is_required_even_when_process_and_answer_succeed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)
            def fake_command(*a, **kw):
                (path / 'answer.txt').write_text('Claimed complete')
                return {'status': 'succeeded', 'stdout': '', 'stderr': ''}
            with patch.object(runner, 'command', side_effect=fake_command), \
                 patch.object(runner, 'sandbox_command', return_value=['fake']):
                result = flow.subject_turn(path, path, 'request', 'test', 5)
            self.assertEqual(result['status'], 'missing_or_changed_session')

    def test_stakeholder_never_receives_private_criteria_or_treatment(self):
        case = CASES[0]
        def fake_run(workspace, prompt, model, timeout, schema, judge):
            self.assertIn(case['actor_brief'], prompt)
            for criterion in case['criteria'].values():
                self.assertNotIn(criterion, prompt)
            self.assertNotIn('SKILL.md', prompt)
            self.assertTrue(judge)
            return {'status': 'succeeded', 'stdout': '', 'stderr': '',
                    'answer': json.dumps({'action': 'reply', 'message': 'Only approvers publish.', 'reason': 'Answer the user question'})}
        with tempfile.TemporaryDirectory() as tmp, patch.object(runner, 'codex_run', side_effect=fake_run):
            reply = flow.stakeholder_reply(case, [{'role': 'assistant', 'message': 'Who may publish?'}],
                                           False, 'test-user', 5, Path(tmp))
            self.assertEqual(reply['action'], 'reply')

    def test_revision_precedes_authorization_and_early_edit_remains_a_failure(self):
        case = copy.deepcopy(CASES[0])
        case['heldout'] = None
        messages, auth_states = [], []
        actions = iter([
            {'action': 'authorize_implementation', 'message': 'Proceed', 'reason': 'Proposal presented'},
            {'action': 'authorize_implementation', 'message': 'Proceed after correction', 'reason': 'Revision discussed'},
            {'action': 'finish', 'message': '', 'reason': 'Delivered; do not coach fixes'}])
        def subject(workspace, runtime, message, model, timeout, session_id):
            messages.append(message)
            if len(messages) == 1:
                (workspace / 'app.py').write_text('unauthorized implementation')
            return {'status': 'succeeded', 'stdout': 'raw events', 'stderr': '',
                    'answer': 'Visible subject reply', 'session_id': 'same-session'}
        def actor(case, exchange, authorized, model, timeout, output):
            auth_states.append(authorized)
            return next(actions)
        with tempfile.TemporaryDirectory() as tmp, patch.object(flow, 'subject_turn', side_effect=subject), \
             patch.object(flow, 'stakeholder_reply', side_effect=actor), \
             patch.object(flow, 'assess', return_value=good_judgment(case)):
            output = Path(tmp) / 'result'
            result = flow.variant(case, True, args(), output, False)
            self.assertEqual(auth_states, [False, False, True])
            self.assertEqual(messages[1], case['revision_message'])
            self.assertIn(flow.APPROVAL, messages[2])
            self.assertEqual(result['verdict'], 'fail')
            self.assertTrue(result['conversation_completed'])
            self.assertTrue((output / 'turns' / '1' / 'files' / 'app.py').exists())
            self.assertTrue((output / 'intervention' / '.agents' / 'skills' / 'lean-engineer' / 'SKILL.md').exists())
            self.assertFalse((output / 'files' / '.agents').exists())

    def test_independent_failures_and_incomplete_evidence_cannot_be_overruled(self):
        case = CASES[0]
        judgment = good_judgment(case)
        checks = {'status': 'checked', 'no_code_before_authorization': True,
                  'immutable_inputs_preserved_at_turn_boundaries': True,
                  'heldout_tests': {'verdict': 'fail'}}
        self.assertEqual(flow.compose(True, checks, judgment), 'fail')
        checks['heldout_tests']['verdict'] = 'indeterminate'
        self.assertEqual(flow.compose(True, checks, judgment), 'indeterminate')
        checks['heldout_tests']['verdict'] = 'pass'
        judgment['criteria'][0]['verdict'] = 'not_verified'
        self.assertEqual(flow.compose(True, checks, judgment), 'indeterminate')
        self.assertEqual(flow.compose(False, checks, good_judgment(case)), 'indeterminate')

    def test_assessment_requires_each_criterion_with_evidence(self):
        case = CASES[1]
        data = good_judgment(case)
        data.pop('status'); data.pop('legacy_result'); data.pop('quality_result')
        data['criteria'].pop()
        fake = {'status': 'succeeded', 'stdout': '', 'stderr': '', 'answer': json.dumps(data)}
        with tempfile.TemporaryDirectory() as tmp, patch.object(runner, 'codex_run', return_value=fake):
            result = flow.assess(case, {}, {}, [], [], {}, 'test', 5, Path(tmp))
            self.assertEqual(result['status'], 'invalid_judgment')

    def test_blocked_run_keeps_unscored_paired_inputs(self):
        settings = args()
        with tempfile.TemporaryDirectory() as tmp:
            settings.output = Path(tmp) / 'result'
            settings.cases = ['commission-lifecycle']
            settings.pilot = 'commission-lifecycle'
            settings.repeats = 1
            settings.seed = 0
            settings.prepare_only = False
            with patch.object(runner, 'capability_check', return_value={'live_ready': False}), \
                 patch.object(runner, 'command', return_value={'status': 'succeeded', 'stdout': 'test-commit'}), \
                 patch.object(flow, 'subject_turn') as subject, \
                 patch.object(flow, 'stakeholder_reply') as actor, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(flow.run(settings), 2)
                subject.assert_not_called(); actor.assert_not_called()
            summary = json.loads((settings.output / 'comparison.json').read_text())
            case = summary['cases'][0]
            paths = [settings.output / case[arm]['path'] for arm in ('baseline', 'lean')]
            self.assertEqual((paths[0] / 'input-manifest.json').read_bytes(), (paths[1] / 'input-manifest.json').read_bytes())
            self.assertTrue(all(case[a]['verdict'] == 'indeterminate' for a in ('baseline', 'lean')))
            self.assertNotIn('"scores"', (settings.output / 'comparison.json').read_text())

    def test_business_oracle_discriminates_broken_symptom_only_and_correct_controls(self):
        case = CASES[0]
        fixture = runner.fixture_files(case)
        correct = (Path(__file__).with_name('commission_control.py')).read_bytes()
        symptom = correct.replace(b"return {'id': change['id'], 'status': 'pending'}",
            b"conn.execute('UPDATE sections SET base_rate=? WHERE tenant=? AND treaty=? AND section=?', (change['rate'], actor['tenant'], change['treaty'], change['section'])); conn.commit()\n    return {'id': change['id'], 'status': 'pending'}")
        def local_command(workspace, runtime, argv, **kw):
            return [part.replace("'/workspace'", repr(str(workspace)))
                    .replace("'/runtime/heldout.py'", repr(str(runtime / 'heldout.py'))) for part in argv]
        with tempfile.TemporaryDirectory() as tmp, patch.object(runner, 'sandbox_command', side_effect=local_command):
            for name, source, expected in [('broken', fixture['app.py'], 'fail'),
                                            ('symptom-only', symptom, 'fail'), ('correct', correct, 'pass')]:
                with self.subTest(control=name):
                    data = dict(fixture, **{'app.py': source})
                    result = flow.run_check(data, 'commission.py', Path(tmp) / (name + '.json'))
                    self.assertEqual(result['tests_run'], 8, result['stderr'])
                    self.assertEqual(result['verdict'], expected, result['stderr'])


if __name__ == '__main__':
    unittest.main()
