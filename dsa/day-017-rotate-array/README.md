# Rotate Array

## Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

Modify the array in-place without using extra space.

## Example 1

**Input:**
```python
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
```

**Output:**
```python
[5, 6, 7, 1, 2, 3, 4]
```

**Explanation:**

Rotate the array to the right by 3 steps.

## Example 2

**Input:**
```python
nums = [-1, -100, 3, 99]
k = 2
```

**Output:**
```python
[3, 99, -1, -100]
```

## Approach: Reversal Algorithm

We use the **Three Reversals Technique** to rotate the array without using extra space.

### Algorithm

1. Calculate the length of the array `n`.
2. If the array is empty, return.
3. Use `k = k % n` to handle cases where `k` is greater than the array length.
4. Reverse the entire array.
5. Reverse the first `k` elements.
6. Reverse the remaining `n-k` elements.

### Python Solution

```python
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)

        if n == 0:
            return

        k = k % n

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
```

## Dry Run

**Input:**
```python
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
```

| Step | Operation | Array |
|---|---|---|
| Initial | Original array | [1, 2, 3, 4, 5, 6, 7] |
| 1 | Reverse entire array | [7, 6, 5, 4, 3, 2, 1] |
| 2 | Reverse first 3 elements | [5, 6, 7, 4, 3, 2, 1] |
| 3 | Reverse remaining elements | [5, 6, 7, 1, 2, 3, 4] |

## Complexity Analysis

- **Time Complexity:** O(n) — Each reversal takes linear time, and there are three reversals.
- **Space Complexity:** O(1) — The rotation happens in-place without using an extra array.

## Key Concepts

- Arrays
- Two Pointers
- Reversal Algorithm
- In-place Modification

**LeetCode:** Rotate Array