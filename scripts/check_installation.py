"""Exercise skills CLI in fresh destinations outside the source checkout.

Does not call an agent or claim native model discovery. Retains commands/output,
file hashes, local-link checks and installed runnable example results in JSON.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

from validate_skills import validate


def check(source):
    report = {'source': source, 'cli': 'skills@1.7.4', 'runs': [],
              'native_model_discovery': 'not verified; requires live agent traces'}
    with tempfile.TemporaryDirectory(prefix='lean-install-') as tmp:
        root = Path(tmp)
        installations = [('all', '*', 10), ('single', 'technical-design', 1),
                         ('architecture', 'solution-architecture', 1), ('discovery', 'grill-with-docs', 1),
                         ('router', 'lean-engineer', 1)]
        for name, selection, expected in installations:
            dest = root / name; dest.mkdir()
            argv = ['npx', '--yes', 'skills@1.7.4', 'add', source,
                    '--skill', selection, '--agent', 'codex', '--copy', '-y']
            result = subprocess.run(argv, cwd=dest, capture_output=True, text=True, timeout=120)
            row = {'command': argv, 'cwd': str(dest), 'returncode': result.returncode,
                   'stdout': result.stdout, 'stderr': result.stderr}
            if result.returncode:
                report['runs'].append(row)
                continue
            skills = dest / '.agents' / 'skills'
            row['validation'] = validate(skills)
            assert row['validation']['skills'] == expected, row
            row['topic_entries'] = {skill.name: len(list((skill/'references'/'topics').glob('*.md'))) for skill in skills.iterdir() if skill.is_dir() and (skill/'references'/'topic-index.md').is_file()}
            row['files'] = {str(p.relative_to(skills)): hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in sorted(skills.rglob('*')) if p.is_file()}
            if name == 'single':
                example = subprocess.run(['python', '-m', 'unittest', '-v', 'test_publication.py'],
                    cwd=skills/'technical-design'/'examples', capture_output=True, text=True, timeout=30)
                row['example'] = {'returncode': example.returncode, 'stdout': example.stdout, 'stderr': example.stderr}
                assert example.returncode == 0, row
            if name == 'router':
                row['workflow_guides'] = {name: (skills/'lean-engineer'/'references'/name).is_file() for name in ('methods.md', 'workflows.md', 'project-workflow.md', 'walkthrough.md', 'direct-change.md', 'feature-delivery.md', 'design-decision.md', 'investigation.md')}
                assert all(row['workflow_guides'].values())
                row['companions_absent'] = not (skills/'technical-design').exists()
                row['fallback_instruction_present'] = 'If one is absent, do the needed work directly' in (skills/'lean-engineer'/'SKILL.md').read_text()
                assert row['companions_absent'] and row['fallback_instruction_present']
            report['runs'].append(row)
    report['passed'] = len(report['runs']) == len(installations) and all(r['returncode'] == 0 for r in report['runs'])
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = check(args.source)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('Installation checks:', 'passed' if result['passed'] else 'failed')
    raise SystemExit(0 if result['passed'] else 1)
