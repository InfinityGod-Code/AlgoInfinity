class Solution:
    def solution(self, nums: list, target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int 
        """
        memo={}
        def target_sum(index, current_sum) -> int : 
            #base condition
            
            if index == len(nums):
                return 1 if current_sum == target else 0

            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            positive = target_sum(
                index + 1,
                current_sum + nums[index]
            )

            negative = target_sum(
                index + 1,
                current_sum - nums[index]
            )
            memo[(index, current_sum)] = positive + negative

            return memo[(index, current_sum)]

        return target_sum(0, 0)


if __name__ == "__main__":
    # Bootstrap: add the repo root (where run_tests.py lives) to sys.path.
    import sys
    from pathlib import Path

    root = Path(__file__).resolve().parent
    while not (root / "run_tests.py").exists() and root.parent != root:
        root = root.parent
    sys.path.insert(0, str(root))

    from run_tests import run_tests_for

    _, failed, _, _ = run_tests_for(__file__)
    raise SystemExit(1 if failed else 0)
