# Dynamic Programming on Strings — Pattern-Wise Question Bank

A curated, pattern-first roadmap for String DP, the way it's usually asked in competitive/interview exams (LeetCode, GFG, InterviewBit, Codeforces). Each pattern has: the core idea, a recurrence sketch, and 3–5 practice problems with links, ordered easy → hard.

---

## Pattern 1: Longest Common Subsequence (LCS) Family
**Core idea:** Two-pointer state `dp[i][j]` = answer using first `i` chars of `s1` and first `j` chars of `s2`. If chars match, extend diagonally; else branch.
**Recurrence:** `dp[i][j] = dp[i-1][j-1] + 1` if `s1[i]==s2[j]`, else `max(dp[i-1][j], dp[i][j-1])`.

| # | Problem | Link |
|---|---------|------|
| 1 | Longest Common Subsequence | https://leetcode.com/problems/longest-common-subsequence/ |
| 2 | Print the LCS (reconstruct string) | https://www.geeksforgeeks.org/problems/print-longest-common-subsequence2610/1 |
| 3 | Longest Common Substring (contiguous variant) | https://www.geeksforgeeks.org/problems/longest-common-substring1235/1 |
| 4 | Shortest Common Supersequence | https://leetcode.com/problems/shortest-common-supersequence/ |
| 5 | Delete Operation for Two Strings | https://leetcode.com/problems/delete-operation-for-two-strings/ |
| 6 | Minimum Insertions to Make String Palindrome (LCS with reverse) | https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/ |
| 7 | Longest Palindromic Subsequence (LCS of s and reverse(s)) | https://leetcode.com/problems/longest-palindromic-subsequence/ |

---

## Pattern 2: Edit Distance Family
**Core idea:** Same 2D grid as LCS, but every cell has 3 operation choices (insert/delete/replace) instead of a pure match/skip.
**Recurrence:** if match → `dp[i-1][j-1]`; else `1 + min(insert, delete, replace)`.

| # | Problem | Link |
|---|---------|------|
| 1 | Edit Distance | https://leetcode.com/problems/edit-distance/ |
| 2 | One Edit Distance | https://leetcode.com/problems/one-edit-distance/ |
| 3 | Minimum ASCII Delete Sum for Two Strings | https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/ |
| 4 | Wildcard Matching (`?`, `*`) | https://leetcode.com/problems/wildcard-matching/ |
| 5 | Regular Expression Matching (`.`, `*`) | https://leetcode.com/problems/regular-expression-matching/ |

---

## Pattern 3: Palindrome DP
**Core idea:** `dp[i][j]` = true/count/cost over substring `s[i..j]`. Build by increasing substring length (interval DP).
**Recurrence:** `dp[i][j] = dp[i+1][j-1] && s[i]==s[j]` (palindrome check).

| # | Problem | Link |
|---|---------|------|
| 1 | Longest Palindromic Substring | https://leetcode.com/problems/longest-palindromic-substring/ |
| 2 | Palindromic Substrings (count all) | https://leetcode.com/problems/palindromic-substrings/ |
| 3 | Longest Palindromic Subsequence | https://leetcode.com/problems/longest-palindromic-subsequence/ |
| 4 | Palindrome Partitioning II (min cuts) | https://leetcode.com/problems/palindrome-partitioning-ii/ |
| 5 | Palindrome Partitioning (all partitions — DP + backtrack) | https://leetcode.com/problems/palindrome-partitioning/ |
| 6 | Minimum Insertion Steps to Make a String Palindrome | https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/ |
| 7 | Count Different Palindromic Subsequences | https://leetcode.com/problems/count-different-palindromic-subsequences/ |

---

## Pattern 4: Subsequence Counting / Matching
**Core idea:** `dp[i][j]` counts ways to form `t[0..j]` as a subsequence of `s[0..i]`.
**Recurrence:** `dp[i][j] = dp[i-1][j-1] + dp[i-1][j]` if `s[i]==t[j]`, else `dp[i-1][j]`.

| # | Problem | Link |
|---|---------|------|
| 1 | Distinct Subsequences | https://leetcode.com/problems/distinct-subsequences/ |
| 2 | Is Subsequence | https://leetcode.com/problems/is-subsequence/ |
| 3 | Number of Matching Subsequences | https://leetcode.com/problems/number-of-matching-subsequences/ |
| 4 | Count Subsequences Matching a Given Pattern (GFG) | https://www.geeksforgeeks.org/problems/count-subsequences-of-type-a-i-b-j-c-k4028/1 |

---

## Pattern 5: String Partition / Segmentation DP
**Core idea:** `dp[i]` = can/optimally segment `s[0..i]` using a dictionary or cost function. 1D DP scanning break points.
**Recurrence:** `dp[i] = OR/MIN over j<i of (dp[j] AND s[j..i] is valid)`.

| # | Problem | Link |
|---|---------|------|
| 1 | Word Break | https://leetcode.com/problems/word-break/ |
| 2 | Word Break II (return all sentences) | https://leetcode.com/problems/word-break-ii/ |
| 3 | Palindrome Partitioning II (min cuts — also fits here) | https://leetcode.com/problems/palindrome-partitioning-ii/ |
| 4 | Concatenated Words | https://leetcode.com/problems/concatenated-words/ |

---

## Pattern 6: Interleaving / Merge DP (two strings → one)
**Core idea:** `dp[i][j]` = can `s3[0..i+j]` be formed by interleaving `s1[0..i]` and `s2[0..j]`.
**Recurrence:** `dp[i][j] = (dp[i-1][j] && s1[i]==s3[i+j]) || (dp[i][j-1] && s2[j]==s3[i+j])`.

| # | Problem | Link |
|---|---------|------|
| 1 | Interleaving String | https://leetcode.com/problems/interleaving-string/ |
| 2 | Shuffle String Check (GFG variant) | https://www.geeksforgeeks.org/problems/shuffle-string3618/1 |

---

## Pattern 7: String Matching with Wildcards / Automaton-Style DP
**Core idea:** 2D DP over pattern vs text with special handling for `*` (zero/more) and `?`/`.` (any one). Often reused with edit-distance grid.

| # | Problem | Link |
|---|---------|------|
| 1 | Wildcard Matching | https://leetcode.com/problems/wildcard-matching/ |
| 2 | Regular Expression Matching | https://leetcode.com/problems/regular-expression-matching/ |
| 3 | String Matching with Wildcard (GFG) | https://www.geeksforgeeks.org/problems/wildcard-string-matching1126/1 |

---

## Pattern 8: Interval DP on Strings (build up by length)
**Core idea:** Iterate over substring length; `dp[i][j]` depends on smaller intervals `dp[i+1][j]`, `dp[i][j-1]`, `dp[i+1][j-1]`.

| # | Problem | Link |
|---|---------|------|
| 1 | Longest Palindromic Substring (interval variant) | https://leetcode.com/problems/longest-palindromic-substring/ |
| 2 | Burst Balloons (classic interval DP, not string but same pattern) | https://leetcode.com/problems/burst-balloons/ |
| 3 | Strange Printer | https://leetcode.com/problems/strange-printer/ |
| 4 | Minimum Cost to Merge Stones (interval DP) | https://leetcode.com/problems/minimum-cost-to-merge-stones/ |
| 5 | Scramble String | https://leetcode.com/problems/scramble-string/ |

---

## Pattern 9: Counting Distinct Ways / Decode-Style DP
**Core idea:** 1D DP where `dp[i]` = number of ways to interpret/decode prefix `s[0..i]`.

| # | Problem | Link |
|---|---------|------|
| 1 | Decode Ways | https://leetcode.com/problems/decode-ways/ |
| 2 | Decode Ways II | https://leetcode.com/problems/decode-ways-ii/ |
| 3 | Count Ways to Form a Target String Given a Dictionary | https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/ |

---

## Suggested Solving Order (progressive difficulty)
1. Is Subsequence → LCS → Longest Common Substring
2. Longest Palindromic Substring → Palindromic Substrings → Longest Palindromic Subsequence
3. Edit Distance → Delete Operation for Two Strings → Minimum ASCII Delete Sum
4. Word Break → Word Break II → Palindrome Partitioning → Palindrome Partitioning II
5. Distinct Subsequences → Interleaving String → Scramble String
6. Wildcard Matching → Regular Expression Matching
7. Decode Ways → Decode Ways II → Number of Ways to Form Target String

---


