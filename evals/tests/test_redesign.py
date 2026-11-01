"""Harness controls, not subject outputs or measured skill effectiveness."""
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import runner
import conversations as flow


def judged(**scores):
    values = dict.fromkeys(runner.METRICS, 2)
    values.update(scores)
    return {'status': 'judged', **runner.validate_judgment({
        'scores': values, 'reasons': dict.fromkeys(runner.METRICS, 'Synthetic evidence'),
        'critical_failure': False, 'critical_reason': '', 'overall': 'Harness control'})}


class RedesignTests(unittest.TestCase):
    def test_real_reference_tree_is_available_in_selected_install(self):
        files = runner.installed_skill_files({'technical-design'})
        self.assertIn('.agents/skills/technical-design/references/python.md', files)
        self.assertIn('.agents/skills/technical-design/examples/publication.py', files)
        self.assertFalse(any('/solution-architecture/' in p for p in files))
        self.assertFalse(any('__pycache__' in p for p in files))

    def test_empty_skipped_missing_crashed_and_wrong_counts_cannot_pass(self):
        for result in [
            {'status': 'succeeded', 'stderr': 'Ran 0 tests\nOK'},
            {'status': 'succeeded', 'stderr': 'Ran 2 tests\nOK (skipped=1)'},
            {'status': 'succeeded', 'stderr': ''},
            {'status': 'timeout', 'stderr': 'Ran 2 tests\nOK'},
            {'status': 'failed', 'stderr': 'Ran 1 test\nFAILED (errors=1)'},
            {'status': 'succeeded', 'stderr': 'Ran 8 tests\nOK'},
        ]:
            with self.subTest(result=result):
                self.assertEqual(runner.check_verdict(result, 2), 'indeterminate')
        self.assertEqual(runner.check_verdict({'status': 'succeeded', 'stderr': 'Ran 2 tests\nOK'}, 2), 'pass')
        self.assertEqual(runner.check_verdict({'status': 'failed', 'stderr': 'Ran 2 tests\nFAILED (failures=1)'}, 2), 'fail')

    def test_quality_and_real_failures_cannot_be_hidden_by_high_total(self):
        judgment = judged(maintainability=0)
        self.assertTrue(judgment['legacy_result']['passed'])
        self.assertFalse(judgment['quality_result']['passed'])
        case = {'heldout': 'message.py'}
        checks = {'generated_tests': {'verdict': 'pass'}, 'heldout_tests': {'verdict': 'fail'}}
        self.assertEqual(runner.smoke_verdict(case, checks, judged()), 'fail')
        self.assertEqual(runner.smoke_verdict(case, {}, judged()), 'indeterminate')
        checks['heldout_tests']['verdict'] = 'pass'
        self.assertEqual(runner.smoke_verdict(case, checks, judgment), 'fail')

    def test_workflow_missing_check_and_stakeholder_fault_are_indeterminate(self):
        j = judged()
        j['criteria'] = [{'id': 'stakeholder_policy', 'verdict': 'pass', 'evidence': 'Synthetic exposure'}]
        checks = {'no_code_before_authorization': True, 'immutable_inputs_preserved_at_turn_boundaries': True}
        self.assertEqual(flow.compose(True, checks, j, ('heldout_tests',)), 'indeterminate')
        j['criteria'][0]['verdict'] = 'fail'
        self.assertEqual(flow.compose(True, checks, j), 'indeterminate')

    def test_new_oracles_discriminate_original_and_correct_controls(self):
        import tempfile
        controls = {
            'authorized-message-fix': 'def validation_error():\n    return {"error": "Currency is invalid"}\n',
            'resume-corrected-feature': 'def eligible(captured_on, requested_on):\n    return captured_on is not None and 0 <= (requested_on-captured_on).days <= 45\n',
            'documented-refund-feature': 'def eligible(captured_on, requested_on):\n    return captured_on is not None and 0 <= (requested_on-captured_on).days <= 30\n',
        }
        cases = json.loads((runner.ROOT / 'cases.json').read_text())
        for case_id, source in controls.items():
            case = next(c for c in cases if c['id'] == case_id)
            for correct in (False, True):
                with self.subTest(case=case_id, correct=correct), tempfile.TemporaryDirectory() as tmp:
                    path = Path(tmp)
                    for name, data in runner.fixture_files(case).items():
                        (path / name).write_bytes(data)
                    if correct:
                        (path / 'app.py').write_text(source)
                    (path / 'check.py').write_bytes((runner.ROOT / 'checks' / case['heldout']).read_bytes())
                    result = runner.command([sys.executable, 'check.py'], path, 10)
                    self.assertEqual(runner.check_verdict(result, case['expected_checks']), 'pass' if correct else 'fail')

    def test_each_required_oracle_has_case_owned_expected_count(self):
        for name in ('cases.json', 'workflows.json'):
            for case in json.loads((runner.ROOT / name).read_text()):
                if case.get('heldout'):
                    self.assertIs(type(case['expected_checks']), int)
                    self.assertGreater(case['expected_checks'], 0)
                    self.assertTrue((runner.ROOT / 'checks' / case['heldout']).is_file())
        cases = json.loads((runner.ROOT / 'cases.json').read_text())
        self.assertTrue(any(c.get('holdout') for c in cases))
        self.assertTrue(any(c.get('expected_checks') == 2 for c in cases))


if __name__ == '__main__':
    unittest.main()
