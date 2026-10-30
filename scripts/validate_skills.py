"""Check this collection or a CLI-installed directory without checkout symlinks.

Standard library; checks format subset and all local Markdown file links inside
individual skills. Actual CLI discovery additionally exercises its YAML parser.
Does not claim semantic, behavioral or diagram-rendering validation.
"""
import argparse
from pathlib import Path
import re


def validate(root):
    skills = sorted(root.glob('*/SKILL.md'))
    if not skills:
        raise ValueError('No skills found')
    links = 0
    for skill in skills:
        directory = skill.parent.resolve()
        text = skill.read_text()
        metadata = text.split('---', 2)[1]
        name = re.search(r'^name: (.+)$', metadata, re.M)
        description = re.search(r'^description: (.+)$', metadata, re.M)
        assert name and name[1] == skill.parent.name, skill
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name[1]), skill
        assert len(name[1]) <= 64, skill
        assert description and 0 < len(description[1]) <= 1024, skill
        assert ': ' not in description[1], 'Quote YAML values containing colons'
        assert len(text.splitlines()) < 500, skill
        for md in directory.rglob('*.md'):
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', md.read_text()):
                if re.match(r'(https?://|#|mailto:)', target):
                    continue
                target = target.split('#')[0]
                path = (md.parent / target).resolve()
                assert path.is_relative_to(directory), (md, target, 'outside selected skill')
                assert path.is_file(), (md, target, 'missing reference')
                links += 1
        assert not any(p.is_symlink() for p in directory.rglob('*')), directory
    return {'skills': len(skills), 'local_links': links, 'status': 'passed'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path('.'))
    print(validate(parser.parse_args().root))
