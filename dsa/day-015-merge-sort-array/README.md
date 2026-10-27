# Merge Sorted Array – LeetCode 88

## Problem Statement

You are given two integer arrays, `nums1` and `nums2`, sorted in non-decreasing order, and two integers, `m` and `n`, representing the number of valid elements in each array.

Merge `nums2` into `nums1` as one sorted array **in-place**, without returning a new array.

## Approach: Three Pointers (Two-Pointer Technique)

Instead of merging from the beginning and overwriting existing elements, we start from the end of both arrays and place the largest element at the end of `nums1`.

### Algorithm

1. Initialize `i = m - 1` to point to the last valid element of `nums1`.
2. Initialize `j = n - 1` to point to the last element of `nums2`.
3. Initialize `k = m + n - 1` to point to the last position of `nums1`.
4. Compare `nums1[i]` and `nums2[j]`.
   - If `nums1[i]` is greater, place it at `nums1[k]` and decrement `i`.
   - Otherwise, place `nums2[j]` at `nums1[k]` and decrement `j`.
5. Decrement `k` after each placement.
6. If any elements remain in `nums2`, copy them into `nums1`.
7. No extra copying is needed for the remaining elements of `nums1`, because they are already in their correct positions.

## Example

**Input:**
```python
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
```

**Output:**
```python
[1, 2, 2, 3, 5, 6]
```

### Dry Run

Initially:

```text
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

i = 2, j = 2, k = 5
```

| Comparison | Action | Updated `nums1` |
|---|---|---|
| 3 vs 6 | Place 6 at index 5 | `[1, 2, 3, 0, 0, 6]` |
| 3 vs 5 | Place 5 at index 4 | `[1, 2, 3, 0, 5, 6]` |
| 3 vs 2 | Place 3 at index 3 | `[1, 2, 3, 3, 5, 6]` |
| 2 vs 2 | Place 2 from `nums2` at index 2 | `[1, 2, 2, 3, 5, 6]` |

Now `j = 0` and `i = 0`. The remaining element in `nums2` is `2`, which is already placed. The algorithm finishes with:

```python
[1, 2, 2, 3, 5, 6]
```

## Complexity Analysis

- **Time Complexity:** `O(m + n)` — Each element is processed at most once.
- **Auxiliary Space Complexity:** `O(1)` — The algorithm modifies `nums1` directly without using an additional array.

## Key Concepts Learned

- Two-pointer technique
- In-place array modification
- Merging sorted arrays
- Comparing elements from the end
- Time and space complexity analysis

## Why Start From the End?

Starting from the beginning could overwrite valid elements in `nums1` before they are processed. Starting from the end avoids this problem because the largest remaining element can be safely placed in the last available position.

## Conclusion

This solution merges two sorted arrays efficiently using three pointers. It achieves `O(m + n)` time complexity and `O(1)` auxiliary space, making it an optimal in-place solution.
