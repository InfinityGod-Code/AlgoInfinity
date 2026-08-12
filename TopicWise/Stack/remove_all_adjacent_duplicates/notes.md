## Remove All Adjacent Duplicates In String — Notes

### Key Intuition
Removing an adjacent duplicate pair can expose a *new* adjacent pair to its left/right
(e.g. `"abba"` → remove `"bb"` → `"aa"` → remove → `""`). A naive repeated pass over the
string is O(n²) in the worst case.

The stack solves this in **one pass**: it keeps the "kept so far" string, with the most
recent kept character on top. Walking through `s`:

- If the current char equals the top of the stack, the char and the top form an adjacent
  duplicate pair → **pop** (remove both).
- Otherwise the current char survives (for now) → **push**.

When a pop happens, the next char is compared against the *new* top, which automatically
handles the cascading removals — no re-scan needed. At the end, the stack is the final string.

The top of the stack always holds the last character of the current answer, so an adjacent
duplicate is detected the moment it becomes adjacent (even if it was "re-exposed" by a pop).

### Approach Summary
1. Guard: empty string → return as-is.
2. Push `s[0]`, then for each next char: pop if it equals the top, else push.
3. Rebuild the result in original order (stack is LIFO, so reverse it back).

Time  : O(n) — each character pushed at most once and popped at most once.
Space : O(n) — the stack holds at most all characters (e.g. no duplicates).

### Edge Cases
- Single character → unchanged.
- No adjacent duplicates → unchanged.
- All same characters → collapses to `""` (even length) or one char (odd length).
- Cascading removals: `"abba"` → `""`, `"abccba"` → `""` (inner pair exposes outer pair).
- Adjacent duplicates can form mid-string after a removal: `"caaabbbc"` → `"cabc"`.
- Comparison is case-sensitive: `"aA"` is *not* a duplicate pair.
- `"!aa!"` → `""`: the trailing `!` matches the leading `!` only after `"aa"` is removed.

### Reusable Pattern
This is the **"Matching / Adjacent removal"** stack pattern: push while safe, pop when the
new element "cancels" the top. The same one-pass idea appears in Valid Parentheses and in
removing `k` adjacent duplicates (generalize the pop to count runs). Related: the classic
parentheses problems only pop on a *matching* close — here we pop on an *equal* neighbour.
