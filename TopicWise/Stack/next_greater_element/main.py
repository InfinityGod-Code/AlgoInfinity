from typing import List  # noqa: UP035


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:  # noqa: UP006
        pass

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
