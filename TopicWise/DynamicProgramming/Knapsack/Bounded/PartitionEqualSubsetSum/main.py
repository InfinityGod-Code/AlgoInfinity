class Solution:
    def solution(self, nums: list) -> bool:
        """
        Most optimal solution - default method called by test runner.
        Uses iterative bottom-up DP with boolean array.
        Time  : O(n * target) - polynomial
        Space : O(target) - optimized from O(n * target)
        """
        n = len(nums)
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for w in range(target, num - 1, -1):
                dp[w] = dp[w] or dp[w - num]

        return dp[target]


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
