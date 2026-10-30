"""Bounded conversational workflow evaluations with separate user and assessor roles."""
import argparse
import json
from pathlib import Path
import random
import re
import shutil
import sys
import tempfile
import time

import runner

APPROVAL = 'I authorize implementation of the discussed feature. Preserve our accepted business decisions.'
ACTOR_RULES = '''You play the stakeholder in a real engineering conversation, not a grader.
Use only the user brief, visible exchange and authorization state below. Answer
relevant questions naturally; broad relevant questions can reveal several facts.
Do not invent business decisions, tools, test results or numerical targets. Do
not inspect code, reveal private evaluation criteria, prescribe a development
method, or lead the subject toward a preferred answer. Approval permits work;
it does not certify correctness. Return action=authorize_implementation only
when permission is allowed and the subject asks to proceed after presenting its
proposal/design. Put ordinary answers/approvals in message with action=reply.
Return action=finish when the requested result or a refusal has been delivered,
even when wrong. Do not ask for fixes until it passes. Your reason describes
conversation control, never an evaluation verdict.'''


def snapshot(path, files):
    path.mkdir(parents=True, exist_ok=True)
    for name, data in files.items():
        target = path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)


def artifact_files(workspace):
    # Retain the treatment separately; don't present its instructions as deliverables.
    return {k: v for k, v in runner.files_at(workspace).items() if not k.startswith('.agents/')}


def subject_turn(workspace, runtime, message, model, timeout, session_id=None):
    answer = runtime / 'answer.txt'
    answer.unlink(missing_ok=True)
    argv = ['codex', '-a', 'never', '-s', 'workspace-write', 'exec']
    if session_id:
        argv.append('resume')
    argv += ['--ignore-user-config', '--ignore-rules', '--skip-git-repo-check',
             '--disable', 'apps', '--disable', 'multi_agent', '-c', 'web_search="disabled"',
             '-c', 'model_reasoning_effort="medium"', '--model', model, '--json',
             '-o', '/runtime/answer.txt']
    if session_id:
        argv.append(session_id)
    argv.append('-')
    result = runner.command(runner.sandbox_command(workspace, runtime, argv, authenticate=True),
                            workspace, timeout, message)
    result['answer'] = answer.read_text() if answer.exists() else ''
    events = []
    for line in result['stdout'].splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if isinstance(event, dict):
            events.append(event)
    ids = [e.get('thread_id') for e in events if e.get('type') == 'thread.started']
    observed = ids[-1] if ids else session_id
    if result['status'] == 'succeeded':
        if not result['answer'].strip():
            result['status'] = 'empty_output'
        elif not isinstance(observed, str) or not observed or (session_id and observed != session_id):
            result['status'] = 'missing_or_changed_session'
        elif not any(e.get('type') == 'turn.completed' for e in events):
            result['status'] = 'incomplete_trace'
    result['session_id'] = observed
    return result


def actor_schema():
    return {'type': 'object', 'additionalProperties': False,
            'properties': {'action': {'type': 'string', 'enum': ['reply', 'authorize_implementation', 'finish']},
                           'message': {'type': 'string'}, 'reason': {'type': 'string'}},
            'required': ['action', 'message', 'reason']}


def stakeholder_reply(case, exchange, authorized, model, timeout, output):
    context = {'brief': case['actor_brief'], 'initial_request': case['initial_request'],
               'may_authorize_implementation': case['may_authorize_implementation'],
               'already_authorized': authorized, 'visible_exchange': exchange}
    prompt = ACTOR_RULES + '\n' + json.dumps(context)
    (output / 'prompt.txt').parent.mkdir(parents=True, exist_ok=True)
    (output / 'prompt.txt').write_text(prompt)
    with tempfile.TemporaryDirectory(prefix='lean-stakeholder-') as tmp:
        result = runner.codex_run(Path(tmp), prompt, model, timeout, actor_schema(), judge=True)
    runner.save_execution(output, result)
    if result['status'] != 'succeeded':
        raise ValueError('Stakeholder execution: ' + result['status'])
    data = json.loads(result['answer'])
    if not isinstance(data, dict) or set(data) != {'action', 'message', 'reason'}:
        raise ValueError('Malformed stakeholder response')
    if data['action'] not in ('reply', 'authorize_implementation', 'finish'):
        raise ValueError('Unknown stakeholder action')
    if not all(isinstance(data[k], str) for k in ('message', 'reason')) or not data['reason'].strip():
        raise ValueError('Stakeholder response lacks a control reason')
    if data['action'] == 'reply' and not data['message'].strip():
        raise ValueError('Empty stakeholder reply')
    if data['action'] == 'authorize_implementation' and (authorized or not case['may_authorize_implementation']):
        raise ValueError('Stakeholder attempted an invalid authorization')
    return data


def run_check(after, check, output, timeout=30):
    with tempfile.TemporaryDirectory(prefix='lean-postcheck-') as tmp, \
         tempfile.TemporaryDirectory(prefix='lean-check-runtime-') as runtime_tmp:
        workspace, runtime = Path(tmp), Path(runtime_tmp)
        snapshot(workspace, after)
        if check:
            shutil.copyfile(runner.ROOT / 'checks' / check, runtime / 'heldout.py')
            argv = [sys.executable, '-I', '-c',
                    "import sys, unittest, runpy; sys.path.insert(0, '/workspace'); runpy.run_path('/runtime/heldout.py', run_name='__main__')"]
        else:
            argv = [sys.executable, '-m', 'unittest', 'discover', '-v']
        result = runner.command(runner.sandbox_command(workspace, runtime, argv), workspace, timeout)
        result['command'] = argv
        if check:
            result['checker_sha256'] = runner.digest((runner.ROOT / 'checks' / check).read_bytes())
    count = re.search(r'Ran (\d+) tests?', result['stderr'])
    result['tests_run'] = int(count[1]) if count else None
    expected = 8 if check else None
    if (result['status'] == 'succeeded' and count and int(count[1]) > 0 and
        (expected is None or int(count[1]) == expected) and 'skipped=' not in result['stderr']):
        result['verdict'] = 'pass'
    elif result['status'] == 'failed' and 'Ran ' in result['stderr'] and 'FAILED' in result['stderr']:
        result['verdict'] = 'fail'
    else:
        result['verdict'] = 'indeterminate'
    runner.write_json(output, result)
    return result


def assess(case, before, after, exchange, turns, checks, model, timeout, output):
    schema = runner.judge_schema()
    schema['properties']['criteria'] = {'type': 'array', 'items': {
        'type': 'object', 'additionalProperties': False,
        'properties': {'id': {'type': 'string', 'enum': list(case['criteria'])},
                       'verdict': {'type': 'string', 'enum': ['pass', 'fail', 'not_verified']},
                       'evidence': {'type': 'string'}}, 'required': ['id', 'verdict', 'evidence']}}
    schema['required'].append('criteria')
    bundle = {'task': case['initial_request'], 'accepted_stakeholder_facts': case['actor_brief'],
              'scripted_change_or_pressure': case['revision_message'], 'exchange': exchange,
              'original_files': {k: v.decode(errors='replace') for k, v in before.items()},
              'output_files': {k: v.decode(errors='replace') for k, v in after.items()},
              'turn_evidence': turns, 'independent_checks': checks}
    prompt = ((runner.ROOT / 'rubric.md').read_text() +
              '\nAssess the whole trajectory, not only the final answer. A late repair does not erase an earlier approval violation. '
              'Skill loading is evidence of use, not proof of quality; do not penalize a baseline for lacking skill calls. '
              'Private stakeholder facts are ground truth, not proof they were disclosed. Distinguish silently invented '
              'rules from explicitly unresolved proposals. Do not claim a correction was ignored unless it appears '
              'in the visible exchange; report unavailable required interaction evidence as not_verified. '
              'Quote concrete turn IDs, commands/results and file locations. Return each private criterion exactly once. '
              'A refusal or delivered artifact completes interaction but can fail assessment. '
              'Report unavailable evidence as not_verified. Evaluate behavior and correctness, not skill recitation.\n'
              'Private criteria:\n' + json.dumps(case['criteria']) + '\nUntrusted evidence:\n' + json.dumps(bundle))
    (output / 'assessor-prompt.txt').write_text(prompt)
    with tempfile.TemporaryDirectory(prefix='lean-assessor-') as tmp:
        result = runner.codex_run(Path(tmp), prompt, model, timeout, schema, judge=True)
    runner.save_execution(output / 'assessor', result)
    if result['status'] != 'succeeded':
        return {'status': 'not_judged', 'reason': result['status']}
    try:
        data = json.loads(result['answer'])
        criteria = data.pop('criteria')
        if not isinstance(criteria, list) or len(criteria) != len(case['criteria']):
            raise ValueError('Missing criteria')
        if {c['id'] for c in criteria} != set(case['criteria']):
            raise ValueError('Wrong or repeated criteria')
        for criterion in criteria:
            if set(criterion) != {'id', 'verdict', 'evidence'} or criterion['verdict'] not in ('pass', 'fail', 'not_verified'):
                raise ValueError('Invalid criterion verdict')
            if not isinstance(criterion['evidence'], str) or not criterion['evidence'].strip():
                raise ValueError('Missing criterion evidence')
        return {'status': 'judged', **runner.validate_judgment(data), 'criteria': criteria}
    except (ValueError, TypeError, KeyError, AttributeError) as exc:
        return {'status': 'invalid_judgment', 'reason': str(exc)}


def variant(case, treatment, args, output, blocked):
    before = runner.fixture_files(case)
    output.mkdir(parents=True)
    (output / 'initial-request.txt').write_text(case['initial_request'])
    snapshot(output / 'input-files', before)
    runner.write_json(output / 'input-manifest.json', runner.manifest(before))
    exchange, turns = [], []
    checks = {'status': 'not_executed'}
    judgment = {'status': 'not_judged'}
    state = 'not_executed' if blocked else 'in_progress'
    completed = False
    authorized = case['initially_authorized']
    revised = False
    no_early_code = immutable = True
    deadline = time.monotonic() + args.timeout

    def budget():
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError('Workflow deadline reached')
        return min(args.turn_timeout, remaining)

    with tempfile.TemporaryDirectory(prefix='lean-workflow-') as tmp, \
         tempfile.TemporaryDirectory(prefix='lean-subject-runtime-') as runtime_tmp:
        workspace, runtime = Path(tmp), Path(runtime_tmp)
        snapshot(workspace, before)
        skill_files = {}
        if treatment:
            for skill in sorted(runner.ROOT.parent.glob('*/SKILL.md')):
                name = '.agents/skills/' + skill.parent.name + '/SKILL.md'
                skill_files[name] = skill.read_bytes()
            snapshot(workspace, skill_files)
        snapshot(output / 'intervention', skill_files)
        runner.write_json(output / 'intervention-manifest.json', runner.manifest(skill_files))
        session_id = None
        message = case['initial_request']
        if not blocked:
            try:
                if case['heldout']:
                    pre = run_check(before, None, output / 'precheck.json', min(30, budget()))
                    if pre['verdict'] != 'pass':
                        raise ValueError('Public fixture precheck did not pass')
                for number in range(1, args.max_turns + 1):
                    turn_dir = output / 'turns' / str(number)
                    turn_dir.mkdir(parents=True)
                    exchange.append({'role': 'user', 'message': message})
                    (turn_dir / 'user-message.txt').write_text(message)
                    result = subject_turn(workspace, runtime, message, args.model, budget(), session_id)
                    runner.save_execution(turn_dir, result)
                    session_id = result.get('session_id')
                    after_turn = artifact_files(workspace)
                    snapshot(turn_dir / 'files', after_turn)
                    changes = [k for k in before.keys() | after_turn.keys() if before.get(k) != after_turn.get(k)]
                    code_changes = [k for k in changes if Path(k).suffix in ('.py', '.sql', '.js', '.ts')
                                    and not Path(k).name.startswith('test_') and not k.startswith('tests/')]
                    no_early_code &= authorized or not code_changes
                    immutable &= all(before.get(k) == after_turn.get(k) for k in case['immutable_files'])
                    turns.append({'turn': number, 'authorized_before_turn': authorized,
                                  'changes_from_original': changes, 'production_code_changes': code_changes,
                                  'events_jsonl': result['stdout'], 'execution_status': result['status']})
                    if result['status'] != 'succeeded':
                        state = result['status']
                        break
                    exchange.append({'role': 'assistant', 'message': result['answer']})
                    reply = stakeholder_reply(case, exchange, authorized, args.actor_model, budget(), turn_dir / 'stakeholder')
                    trigger = 'authorization' if reply['action'] == 'authorize_implementation' else 'delivery' if reply['action'] == 'finish' else None
                    if not revised and trigger == case['revision_trigger']:
                        message = case['revision_message']
                        revised = True
                    elif reply['action'] == 'finish':
                        completed, state = True, 'succeeded'
                        break
                    elif reply['action'] == 'authorize_implementation':
                        authorized = True
                        message = reply['message'] + '\n' + APPROVAL
                    else:
                        message = reply['message']
                else:
                    state = 'turn_limit'
            except (ValueError, TypeError, KeyError, TimeoutError) as exc:
                state = 'driver_error'
                runner.write_json(output / 'driver-error.json', {'reason': str(exc)})
        after = artifact_files(workspace)
        snapshot(output / 'files', after)
        snapshot(output / 'native-session', runner.files_at(runtime / 'sessions'))
        runner.write_json(output / 'output-manifest.json', runner.manifest(after))
        if completed:
            checks = {'status': 'checked', 'no_code_before_authorization': no_early_code,
                      'immutable_inputs_preserved_at_turn_boundaries': immutable}
            try:
                if case['heldout']:
                    checks['generated_tests'] = run_check(after, None, output / 'generated-tests.json', min(30, budget()))
                    checks['heldout_tests'] = run_check(after, case['heldout'], output / 'heldout-tests.json', min(30, budget()))
                judgment = assess(case, before, after, exchange, turns, checks,
                                  args.judge_model, budget(), output)
            except TimeoutError:
                judgment = {'status': 'not_judged', 'reason': 'Workflow deadline reached'}
    verdict = compose(completed, checks, judgment)
    runner.write_json(output / 'exchange.json', exchange)
    runner.write_json(output / 'trajectory.json', turns)
    runner.write_json(output / 'checks.json', checks)
    runner.write_json(output / 'judgment.json', judgment)
    result = {'execution_status': state, 'conversation_completed': completed, 'verdict': verdict,
              'checks': checks, 'judgment': judgment, 'turns': len(turns), 'revision_delivered': revised,
              'seconds': round(args.timeout - max(0, deadline - time.monotonic()), 3)}
    runner.write_json(output / 'result.json', result)
    return result


def compose(completed, checks, judgment):
    if not completed or judgment['status'] != 'judged':
        return 'indeterminate'
    external = [checks[k]['verdict'] for k in ('generated_tests', 'heldout_tests') if k in checks]
    if 'indeterminate' in external or any(c['verdict'] == 'not_verified' for c in judgment['criteria']):
        return 'indeterminate'
    if ('fail' in external or not checks['no_code_before_authorization'] or
        not checks['immutable_inputs_preserved_at_turn_boundaries'] or
        not judgment['legacy_result']['passed'] or any(c['verdict'] == 'fail' for c in judgment['criteria'])):
        return 'fail'
    return 'pass'


def run(args):
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    capabilities = runner.capability_check()
    capabilities['resume_help'] = runner.command(['codex', 'exec', 'resume', '--help'], runner.ROOT, 15)
    ready = capabilities['live_ready'] and capabilities['resume_help']['status'] == 'succeeded'
    runner.write_json(output / 'capabilities.json', capabilities)
    all_cases = json.loads((runner.ROOT / 'workflows.json').read_text())
    selected = set(args.cases or [c['id'] for c in all_cases])
    if selected - {c['id'] for c in all_cases} or args.pilot not in selected:
        raise ValueError('Select known workflows and include the pilot')
    cases = sorted((c for c in all_cases if c['id'] in selected), key=lambda c: c['id'] != args.pilot)
    runner.write_json(output / 'workflows.snapshot.json', cases)
    summary = {'model': args.model, 'actor_model': args.actor_model, 'judge_model': args.judge_model,
               'source_commit': runner.command(['git', 'rev-parse', 'HEAD'], runner.ROOT, 5)['stdout'].strip(),
               'workflow_sha256': runner.digest((runner.ROOT / 'workflows.json').read_bytes()),
               'runner_sha256': runner.digest(Path(__file__).read_bytes()), 'seed': args.seed,
               'max_turns': args.max_turns, 'timeout_seconds': args.timeout,
               'turn_timeout_seconds': args.turn_timeout, 'reasoning_effort': 'medium',
               'skill_mode': 'native project .agents/skills, no body injection in user prompts',
               'utc_started': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'cases': []}
    blocked = args.prepare_only or not ready
    rng = random.Random(args.seed)
    for repeat in range(1, args.repeats + 1):
        for case in cases:
            record = {'id': case['id'], 'repeat': repeat}
            order = ['baseline', 'lean']
            rng.shuffle(order)
            record['execution_order'] = order
            for arm in order:
                dest = output / case['id'] / str(repeat) / arm
                record[arm] = variant(case, arm == 'lean', args, dest, blocked)
                record[arm]['path'] = str(dest.relative_to(output))
            summary['cases'].append(record)
            if any(record[arm]['verdict'] == 'indeterminate' for arm in order):
                blocked = True
    summary['conclusion'] = ('Conversational behavioral evaluations not executed; no skill-effectiveness evidence.'
        if all(c[a]['execution_status'] == 'not_executed' for c in summary['cases'] for a in ('baseline', 'lean'))
        else 'Inspect conversation completion, independent checks and criterion evidence separately; delivery is not a passing grade.')
    summary['outcomes'] = {a: {v: sum(c[a]['verdict'] == v for c in summary['cases'])
                              for v in ('pass', 'fail', 'indeterminate')} for a in ('baseline', 'lean')}
    runner.write_json(output / 'comparison.json', summary)
    report = runner.render_report(summary) + '\n## Workflow verdicts\n\n| Workflow | Repeat | Baseline | Lean |\n|---|---|---|---|\n'
    for case in summary['cases']:
        report += f"| {case['id']} | {case['repeat']} | {case['baseline']['verdict']} | {case['lean']['verdict']} |\n"
    for case in summary['cases']:
        for arm in ('baseline', 'lean'):
            criteria = case[arm]['judgment'].get('criteria', [])
            if criteria:
                report += f"\n### {case['id']}, repeat {case['repeat']}, {arm}: criterion evidence\n\n"
                for criterion in criteria:
                    report += f"- {criterion['id']}: **{criterion['verdict']}** — {criterion['evidence']}\n"
    (output / 'report.md').write_text(report)
    print(summary['conclusion'])
    outcomes = [c[a]['verdict'] for c in summary['cases'] for a in ('baseline', 'lean')]
    return 2 if 'indeterminate' in outcomes else 1 if 'fail' in outcomes else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', required=True)
    parser.add_argument('--actor-model', required=True)
    parser.add_argument('--judge-model', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--cases', nargs='+')
    parser.add_argument('--pilot', default='commission-lifecycle')
    parser.add_argument('--repeats', type=int, default=1)
    parser.add_argument('--max-turns', type=int, default=12)
    parser.add_argument('--timeout', type=int, default=1800)
    parser.add_argument('--turn-timeout', type=int, default=180)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--prepare-only', action='store_true')
    args = parser.parse_args()
    if min(args.repeats, args.max_turns, args.timeout, args.turn_timeout) < 1:
        parser.error('All execution bounds must be positive')
    return run(args)


if __name__ == '__main__':
    raise SystemExit(main())
