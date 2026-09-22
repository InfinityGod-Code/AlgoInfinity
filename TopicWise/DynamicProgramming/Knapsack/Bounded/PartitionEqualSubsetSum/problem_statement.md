## Partition Equal Subset Sum

### Problem Statement

Given a non-empty array `nums` containing only positive integers, determine if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

### Examples

Example 1:
```
Input: nums = [1, 5, 5, 11]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11], both having sum 11.
```

Example 2:
```
Input: nums = [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into two subsets with equal sum.
```

Example 3:
```
Input: nums = [1, 1]
Output: true
Explanation: The array can be partitioned as [1] and [1], both having sum 1.
```

### Constraints

- ```1 <= nums.length <= 100```
- ```1 <= nums[i] <= 100```
- The total sum of the array will not exceed 1000
- All elements are positive integers