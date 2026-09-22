class Solution:
    def solution(self, values: list, weights: list, capacity: int) -> int:
        """
        MOST OPTIMIZED: Iterative bottom-up DP with space optimization.
        Uses 1D DP array, iterates capacity backward (0/1 knapsack property).
        Time  : O(n * capacity) - polynomial
        Space : O(capacity) - optimized from O(n * capacity)
        """
        n = len(values)
        dp = [0] * (capacity + 1)

        for i in range(n):
            # Iterate backward to enforce 0/1 (each item used at most once)
            for w in range(capacity, weights[i] - 1, -1):
                dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

        return dp[capacity]


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
