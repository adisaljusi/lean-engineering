"""Minimal independent rubric scorer. Does not call a model."""

import json
import sys
from pathlib import Path

DIMENSIONS = ("requirements", "scope", "simplicity", "design", "tests", "evidence")


def evaluate(scores):
    if set(scores) != set(DIMENSIONS) | {"critical_failure"}:
        raise ValueError("Scores must have six dimensions and critical_failure")
    if any(type(scores[key]) is not int or scores[key] not in (0, 1, 2) for key in DIMENSIONS):
        raise ValueError("Each dimension needs integer score 0, 1, or 2")
    if type(scores["critical_failure"]) is not bool:
        raise ValueError("critical_failure must be boolean")
    total = sum(scores[key] for key in DIMENSIONS)
    passed = total >= 9 and scores["simplicity"] >= 1 and scores["tests"] >= 1 and not scores["critical_failure"]
    return {"score": total, "max_score": 12, "passed": passed}


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        assert evaluate(dict.fromkeys(DIMENSIONS, 2) | {"critical_failure": False})["passed"]
        assert not evaluate(dict.fromkeys(DIMENSIONS, 0) | {"critical_failure": False})["passed"]
        assert not evaluate(dict.fromkeys(DIMENSIONS, 2) | {"critical_failure": True})["passed"]
        print("Scorer self-test passed")
        return
    if len(sys.argv) != 3:
        raise SystemExit("Usage: score.py CASE_ID scores.json | --self-test")
    case_id, path = sys.argv[1:]
    cases = json.loads((Path(__file__).parent / "cases.json").read_text())
    if case_id not in {case["id"] for case in cases}:
        raise SystemExit(f"Unknown case: {case_id}")
    print(json.dumps({"case": case_id, **evaluate(json.loads(Path(path).read_text()))}, indent=2))


if __name__ == "__main__":
    main()
