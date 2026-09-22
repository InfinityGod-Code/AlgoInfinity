## Target Sum

### Problem Statement

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols `+` and `-`. For each integer, you should choose one from `+` and `-` as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target `S`.

### Examples

Example 1:
```
Input: nums = [1, 1, 1, 1, 1], S = 3
Output: 5
Explanation: -1+1+1+1+1 = 3
             1-1+1+1+1 = 3
             1+1-1+1+1 = 3
             1+1+1-1+1 = 3
             1+1+1+1-1 = 3
```

Example 2:
```
Input: nums = [1], S = 1
Output: 1
```

### Constraints

- ```1 <= nums.length <= 20```
- ```0 <= nums[i] <= 1000```
- ```0 <= sum(nums) <= 1000```
- The output is guaranteed to fit in a 32-bit integer