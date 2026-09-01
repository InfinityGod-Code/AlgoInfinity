# Dynamic Programming — Pattern-Wise Question Bank (All Non-String Patterns)

Companion to the String DP sheet. Covers every other major DP category asked in competitive exams/interviews: Knapsack family, LIS family, Grid/Matrix DP, Partition/Subset DP, Bitmask DP, Digit DP, Tree DP, Stock Trading DP, Interval DP (non-string), Probability/Expected Value DP, and Game Theory DP.

---

## Pattern 1: 0/1 Knapsack Family
**Core idea:** `dp[i][w]` = best value using first `i` items with capacity `w`. Each item used at most once → take-or-skip choice.
**Recurrence:** `dp[i][w] = max(dp[i-1][w], val[i] + dp[i-1][w-wt[i]])`.

| # | Problem | Link |
|---|---------|------|
| 1 | 0/1 Knapsack (GFG classic) | https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1 |
| 2 | Partition Equal Subset Sum | https://leetcode.com/problems/partition-equal-subset-sum/ |
| 3 | Target Sum | https://leetcode.com/problems/target-sum/ |
| 4 | Last Stone Weight II | https://leetcode.com/problems/last-stone-weight-ii/ |
| 5 | Ones and Zeroes (2D knapsack) | https://leetcode.com/problems/ones-and-zeroes/ |
| 6 | Partition to K Equal Sum Subsets | https://leetcode.com/problems/partition-to-k-equal-sum-subsets/ |

---

## Pattern 2: Unbounded Knapsack Family
**Core idea:** Same as 0/1 but items can be reused infinitely — inner loop iterates capacity forward instead of backward.
**Recurrence:** `dp[w] = max(dp[w], val[i] + dp[w-wt[i]])`.

| # | Problem | Link |
|---|---------|------|
| 1 | Unbounded Knapsack (GFG) | https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1 |
| 2 | Coin Change (min coins) | https://leetcode.com/problems/coin-change/ |
| 3 | Coin Change II (count ways) | https://leetcode.com/problems/coin-change-ii/ |
| 4 | Rod Cutting (GFG) | https://www.geeksforgeeks.org/problems/rod-cutting0840/1 |
| 5 | Perfect Squares | https://leetcode.com/problems/perfect-squares/ |
| 6 | Combination Sum IV | https://leetcode.com/problems/combination-sum-iv/ |

---

## Pattern 3: Longest Increasing Subsequence (LIS) Family
**Core idea:** `dp[i]` = length of best increasing subsequence ending at index `i`. Optimizable to O(n log n) with patience sorting/binary search.
**Recurrence:** `dp[i] = 1 + max(dp[j])` for all `j<i` with `arr[j] < arr[i]`.

| # | Problem | Link |
|---|---------|------|
| 1 | Longest Increasing Subsequence | https://leetcode.com/problems/longest-increasing-subsequence/ |
| 2 | Number of Longest Increasing Subsequences | https://leetcode.com/problems/number-of-longest-increasing-subsequence/ |
| 3 | Russian Doll Envelopes | https://leetcode.com/problems/russian-doll-envelopes/ |
| 4 | Longest Bitonic Subsequence (GFG) | https://www.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1 |
| 5 | Maximum Sum Increasing Subsequence (GFG) | https://www.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1 |
| 6 | Minimum Number of Removals to Make Mountain Array | https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/ |

---

## Pattern 4: Grid / Matrix DP
**Core idea:** `dp[i][j]` depends on neighbors (`dp[i-1][j]`, `dp[i][j-1]`, sometimes diagonals). Classic path-counting / path-cost problems.
**Recurrence:** `dp[i][j] = grid[i][j] + min/max(dp[i-1][j], dp[i][j-1])`.

| # | Problem | Link |
|---|---------|------|
| 1 | Unique Paths | https://leetcode.com/problems/unique-paths/ |
| 2 | Unique Paths II (obstacles) | https://leetcode.com/problems/unique-paths-ii/ |
| 3 | Minimum Path Sum | https://leetcode.com/problems/minimum-path-sum/ |
| 4 | Dungeon Game (reverse DP) | https://leetcode.com/problems/dungeon-game/ |
| 5 | Cherry Pickup | https://leetcode.com/problems/cherry-pickup/ |
| 6 | Maximal Square | https://leetcode.com/problems/maximal-square/ |
| 7 | Minimum Falling Path Sum | https://leetcode.com/problems/minimum-falling-path-sum/ |

---

## Pattern 5: Partition / Subset Sum DP
**Core idea:** `dp[i][sum]` = can we form `sum` using first `i` elements. Boolean/counting variant of knapsack.
**Recurrence:** `dp[i][s] = dp[i-1][s] OR dp[i-1][s-arr[i]]`.

| # | Problem | Link |
|---|---------|------|
| 1 | Subset Sum Problem (GFG) | https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1 |
| 2 | Partition Equal Subset Sum | https://leetcode.com/problems/partition-equal-subset-sum/ |
| 3 | Count of Subset Sum (GFG) | https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1 |
| 4 | Minimum Subset Sum Difference (GFG) | https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1 |
| 5 | Target Sum | https://leetcode.com/problems/target-sum/ |

---

## Pattern 6: Bitmask DP (DP on Subsets)
**Core idea:** State includes a bitmask representing which elements are "used". `dp[mask][i]` = best answer given the subset `mask` has been processed, currently at `i`.
**Recurrence:** transition by trying to add one more unset bit to the mask.

| # | Problem | Link |
|---|---------|------|
| 1 | Traveling Salesman Problem (GFG) | https://www.geeksforgeeks.org/problems/travelling-salesman-problem2732/1 |
| 2 | Partition to K Equal Sum Subsets | https://leetcode.com/problems/partition-to-k-equal-sum-subsets/ |
| 3 | Shortest Path Visiting All Nodes | https://leetcode.com/problems/shortest-path-visiting-all-nodes/ |
| 4 | Minimum Cost to Connect Two Groups of Points | https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/ |
| 5 | Maximum Students Taking Exam | https://leetcode.com/problems/maximum-students-taking-exam/ |
| 6 | Number of Ways to Wear Different Hats to Each Other | https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/ |

---

## Pattern 7: Digit DP
**Core idea:** `dp[pos][tight][extra_state]` = count/answer built digit by digit from most significant digit, tracking whether we're still bounded by the input number.

| # | Problem | Link |
|---|---------|------|
| 1 | Numbers At Most N Given Digit Set | https://leetcode.com/problems/numbers-at-most-n-given-digit-set/ |
| 2 | Count of Integers Without Consecutive 1s (GFG-style) | https://www.geeksforgeeks.org/problems/count-of-integers-without-consecutive-1s/1 |
| 3 | Count Numbers with Unique Digits | https://leetcode.com/problems/count-numbers-with-unique-digits/ |
| 4 | Non-negative Integers without Consecutive Ones | https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/ |
| 5 | Count Special Integers | https://leetcode.com/problems/count-special-integers/ |

---

## Pattern 8: Tree DP
**Core idea:** `dp[node]` computed from children's `dp[child]` via post-order DFS. Often two states per node (include/exclude, or with/without constraint).

| # | Problem | Link |
|---|---------|------|
| 1 | House Robber III | https://leetcode.com/problems/house-robber-iii/ |
| 2 | Diameter of Binary Tree | https://leetcode.com/problems/diameter-of-binary-tree/ |
| 3 | Binary Tree Maximum Path Sum | https://leetcode.com/problems/binary-tree-maximum-path-sum/ |
| 4 | Longest Path With Different Adjacent Characters | https://leetcode.com/problems/longest-path-with-different-adjacent-characters/ |
| 5 | Minimum Cost to Cut a Stick (interval/tree-like DP) | https://leetcode.com/problems/minimum-cost-to-cut-a-stick/ |

---

## Pattern 9: Stock Trading DP (State Machine DP)
**Core idea:** `dp[day][holding/not-holding][transactions-used]` — classic finite state machine DP.

| # | Problem | Link |
|---|---------|------|
| 1 | Best Time to Buy and Sell Stock | https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ |
| 2 | Best Time to Buy and Sell Stock II | https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/ |
| 3 | Best Time to Buy and Sell Stock III (at most 2 transactions) | https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/ |
| 4 | Best Time to Buy and Sell Stock IV (at most k transactions) | https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/ |
| 5 | Best Time to Buy and Sell Stock with Cooldown | https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/ |
| 6 | Best Time to Buy and Sell Stock with Transaction Fee | https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/ |

---

## Pattern 10: Interval DP (Non-String)
**Core idea:** `dp[i][j]` computed by splitting interval `[i,j]` at every possible `k`, combining left and right results. Iterate by increasing interval length.
**Recurrence:** `dp[i][j] = min/max over k of (dp[i][k] + dp[k+1][j] + cost(i,j))`.

| # | Problem | Link |
|---|---------|------|
| 1 | Matrix Chain Multiplication (GFG) | https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1 |
| 2 | Burst Balloons | https://leetcode.com/problems/burst-balloons/ |
| 3 | Minimum Cost to Merge Stones | https://leetcode.com/problems/minimum-cost-to-merge-stones/ |
| 4 | Minimum Cost Tree From Leaf Values | https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/ |
| 5 | Minimum Cost to Cut a Stick | https://leetcode.com/problems/minimum-cost-to-cut-a-stick/ |

---

## Pattern 11: Probability / Expected Value DP
**Core idea:** `dp[state]` = probability or expected value of reaching/using that state, combining sub-results with weighted sums.

| # | Problem | Link |
|---|---------|------|
| 1 | New 21 Game | https://leetcode.com/problems/new-21-game/ |
| 2 | Knight Probability in Chessboard | https://leetcode.com/problems/knight-probability-in-chessboard/ |
| 3 | Soup Servings | https://leetcode.com/problems/soup-servings/ |
| 4 | Airplane Seat Assignment Probability | https://leetcode.com/problems/airplane-seat-assignment-probability/ |

---

## Pattern 12: Game Theory DP
**Core idea:** `dp[state]` = whether current player can force a win / best score-difference achievable, alternating min/max between two players.

| # | Problem | Link |
|---|---------|------|
| 1 | Predict the Winner | https://leetcode.com/problems/predict-the-winner/ |
| 2 | Stone Game | https://leetcode.com/problems/stone-game/ |
| 3 | Stone Game II | https://leetcode.com/problems/stone-game-ii/ |
| 4 | Nim Game | https://leetcode.com/problems/nim-game/ |
| 5 | Optimal Strategy for a Game (GFG) | https://www.geeksforgeeks.org/problems/optimal-strategy-for-a-game-1587115620/1 |

---

## Pattern 13: 1D Sequence DP (House Robber / Fibonacci-style)
**Core idea:** `dp[i]` depends on a small fixed window of previous states — the simplest DP shape, worth mastering first.

| # | Problem | Link |
|---|---------|------|
| 1 | Climbing Stairs | https://leetcode.com/problems/climbing-stairs/ |
| 2 | House Robber | https://leetcode.com/problems/house-robber/ |
| 3 | House Robber II (circular) | https://leetcode.com/problems/house-robber-ii/ |
| 4 | Maximum Subarray (Kadane's, DP view) | https://leetcode.com/problems/maximum-subarray/ |
| 5 | Delete and Earn | https://leetcode.com/problems/delete-and-earn/ |

---

## Suggested Solving Order (progressive difficulty across all patterns)
1. **1D Sequence DP** → Climbing Stairs → House Robber → House Robber II
2. **0/1 Knapsack** → Partition Equal Subset Sum → Target Sum
3. **Unbounded Knapsack** → Coin Change → Coin Change II
4. **LIS** → LIS → Number of LIS → Russian Doll Envelopes
5. **Grid DP** → Unique Paths → Minimum Path Sum → Maximal Square
6. **Interval DP** → Matrix Chain Multiplication → Burst Balloons
7. **Stock DP** → Buy/Sell I → II → with Cooldown → with Fee → IV
8. **Bitmask DP** → TSP → Partition to K Equal Sum Subsets
9. **Tree DP** → House Robber III → Binary Tree Max Path Sum
10. **Digit DP** → Numbers At Most N Given Digit Set
11. **Game Theory DP** → Predict the Winner → Stone Game
12. **Probability DP** → Knight Probability → New 21 Game

---

## Notes for Exam-Style Practice
- Identify the pattern first by asking: *"What changes as I move through the problem?"* — an index (1D), two indices (grid/2-pointer), a capacity/sum (knapsack), or a subset (bitmask).
- For Knapsack-family problems, always clarify aloud: bounded vs unbounded, and 0/1 vs counting vs boolean — this determines loop direction and combination rule.
- Practice space-optimizing 2D knapsack/grid DPs down to a 1D rolling array — a very common follow-up in interviews.
- For Bitmask and Digit DP, always state the meaning of every dimension of the state explicitly before coding; these are the two patterns examiners most often penalize for unclear state definitions.

Want full worked solutions (code + dry run) for any specific pattern, or a combined timed mock test mixing String DP and these patterns?
