## Next Greater Element I — Notes

### Key Intuition
"Next greater element" = the first element strictly greater than `x` that appears to its right.
Naively, for every `x` in `nums1` we could scan `nums2` to the right → O(n1 * n2). Too slow.

The trick: compute the answer **for every element of `nums2` once**, then look up `nums1` in a hash map.

**Monotonic decreasing stack** — the stack holds elements whose next-greater is still unknown.
They sit in **decreasing** order (largest at the bottom), because when a new `num` arrives:

- While `stack[-1] < num`, that top element's next greater is exactly `num` → pop and record it.
- Then push `num`. It becomes the smallest so far, i.e. the new top — keeping the stack decreasing.

Each element is pushed exactly once and popped exactly once → O(n2) for the whole pass.

Elements still in the stack at the end have **no** greater element to their right → `-1`.

### Why it works (the invariant)
The stack is decreasing: `stack[0] > stack[1] > ... > stack[-1]`.
When a bigger element appears on the right, it "resolves" every smaller element below the top.
The smaller ones resolved earlier don't affect the larger ones because they are further right
and smaller — they can't be the "first greater" of anything left behind.

### Approach Summary
1. Build `mapping` (value → next greater) for `nums2` with the monotonic stack.   O(n2)
2. Leftover stack elements → `-1`.                                              O(n2)
3. Answer `[mapping[x] for x in nums1]`.                                         O(n1)

Time  : O(n1 + n2) — each element of nums2 pushed/popped once, nums1 is one map lookup each.
Space : O(n2) — stack + map, both bounded by len(nums2).

### Edge Cases
- `nums1 == nums2` → whole-array NGE, last element always `-1`.
- Strictly decreasing `nums2` → every element is `-1` (nothing greater to the right).
- Strictly increasing `nums2` → each element's NGE is its immediate successor.
- Maximum value appears first → `-1`, but smaller values after it still resolve normally.
- Single element → `-1`.
- NGE is **not** necessarily the global max (e.g. `[1,5,2,3,4]`: NGE(2) = 3, not 5).
- Values can be `0` and up to `10^4` — uniqueness guarantees map lookups are exact.

### Reusable Pattern
This is the **"Process Until Condition"** monotonic-stack pattern (see DataStructures/Stack/stack.md):
keep removing previous elements until the current element can fit, recording the answer
for each removed element as you go. Same skeleton powers NGE II (circular), Daily Temperatures,
Largest Rectangle in Histogram, and Stock Span.
