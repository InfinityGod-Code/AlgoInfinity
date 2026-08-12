from typing import List  # noqa: UP035


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:  # noqa: UP006
        # Map each element of nums2 to its next greater element using a
        # monotonic decreasing stack. The stack holds candidates whose next
        # greater element is not yet known, in decreasing order from bottom.
        mapping = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                mapping[stack.pop()] = num
            stack.append(num)

        # Remaining elements have no greater element to their right.
        for num in stack:
            mapping[num] = -1

        return [mapping[num] for num in nums1]


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
