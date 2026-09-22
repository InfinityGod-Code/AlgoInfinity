## 0/1 Knapsack

### Problem Statement

Given weights and values of `n` items, put these items in a knapsack of capacity `W` to get the maximum total value in the knapsack. You cannot break an item, either pick the complete item or leave it (0/1 property).

### Examples

Example 1:
```
Input: val[] = {60, 100, 120}, wt[] = {10, 20, 30}, W = 50
Output: 220
Explanation: Pick items with weight 20 and 30 for total value 100 + 120 = 220.
```

Example 2:
```
Input: val[] = {100, 20, 30, 40}, wt[] = {5, 20, 10, 40}, W = 60
Output: 200
Explanation: Pick items with weight 5, 20, and 10 for total value 100 + 20 + 30 = 150.
Or pick items with weight 20 and 40 for total value 20 + 40 = 60.
Best is items with weight 5, 20, and 10 = 150.
Wait, let me recalculate: 100+20+30=150, 20+40=60. So 150 is optimal.
```

Example 3:
```
Input: val[] = {10, 30, 20}, wt[] = {1, 3, 2}, W = 4
Output: 50
Explanation: Pick items with weight 3 and 2 for total value 30 + 20 = 50.
```

### Constraints

- ```1 <= n <= 100``` (number of items)
- ```1 <= W <= 1000``` (knapsack capacity)
- ```1 <= val[i], wt[i] <= 100``` (item values and weights)
- All values and weights are positive integers