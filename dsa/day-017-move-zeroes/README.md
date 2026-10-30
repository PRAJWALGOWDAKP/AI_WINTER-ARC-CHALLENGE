# Move Zeroes

## Problem Statement
Given an integer array `nums`, move all `0`s to the end of the array while maintaining the relative order of all non-zero elements.

You must modify the array in-place without making a copy of the array.

## Example 1

**Input:**
```python
nums = [0, 1, 0, 3, 12]
```

**Output:**
```python
[1, 3, 12, 0, 0]
```

## Example 2

**Input:**
```python
nums = [0]
```

**Output:**
```python
[0]
```

## Approach: Two Pointers

We use two pointers:

- `i`: Tracks the position where the next non-zero element should be placed.
- `j`: Traverses the entire array to find non-zero elements.

### Algorithm

1. Initialize `i = 0`.
2. Traverse the array using `j`.
3. If `nums[j]` is not zero:
   - Swap `nums[i]` and `nums[j]`.
   - Increment `i` by 1.
4. Continue until the entire array is traversed.
5. All zeroes will automatically move to the end.

## Python Solution

```python
class Solution(object):
    def moveZeroes(self, nums):
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        return nums
```

## Complexity Analysis

- **Time Complexity:** O(n) — We traverse the array only once.
- **Space Complexity:** O(1) — We modify the original array without using extra space.

## Key Concepts

- Two Pointers
- Array Traversal
- In-place Modification
- Swapping Elements

**LeetCode:** Move Zeroes