class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return s

        stack = []
        res = ""
        stack.append(s[0])
        for ch in s[1:]:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)

        # temporary stack to reverse the stack to get the correct order of characters
        temp_stack = []

        while stack:
            temp_stack.append(stack.pop())
        while temp_stack:
            res += temp_stack.pop()
        return res


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
