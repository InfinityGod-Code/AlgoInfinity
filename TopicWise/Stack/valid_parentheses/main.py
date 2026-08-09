class Solution:
    def isValidParentheses(self, s: str) -> bool:
        stack = []

        # since we know the characters
        catalog = {}
        catalog["{"] = "}"
        catalog["["] = "]"
        catalog["("] = ")"

        # Edge case when we dont have characters that are present as keys
        atleast_one_open = False

        for ch in s:
            if ch in catalog:
                atleast_one_open = True
                stack.append(ch)

            else:
                if stack:
                    if catalog[stack[-1]] == ch:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        return len(stack) == 0 and atleast_one_open


if __name__ == "__main__":
    # Bootstrap: add the repo root (where run_tests.py lives) to sys.path.
    import sys
    from pathlib import Path

    root = Path(__file__).resolve().parent
    while not (root / "run_tests.py").exists() and root.parent != root:
        root = root.parent
    sys.path.insert(0, str(root))

    from run_tests import run_tests_for

    raise SystemExit(run_tests_for(__file__))
