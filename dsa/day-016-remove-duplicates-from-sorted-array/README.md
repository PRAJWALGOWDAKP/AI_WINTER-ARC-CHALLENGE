# Remove Duplicates from Sorted Array

## Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** so that each distinct element appears only once.

Return the number of unique elements, `k`. The first `k` elements of `nums` must contain the unique values in their original order.

## Approach: Two Pointers

This solution uses two pointers to remove duplicates without creating another array.

- `i`: Traverses the array to check each element.
- `k`: Tracks the position where the next unique element should be placed.

### Algorithm

1. Initialize `k = 1`, because the first element is always unique when the array is non-empty.
2. Traverse the array starting from index `1`.
3. Compare `nums[i]` with `nums[k - 1]`, the last unique element.
4. If they are different:
   - Place `nums[i]` at index `k`.
   - Increment `k`.
5. Return `k`, the total number of unique elements.

## Python Solution

```python
class Solution(object):
    def removeDuplicates(self, nums):
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k = k + 1

        return k
```

## Example

**Input:**

`nums = [1, 1, 2, 2, 3]`

**Output:**

`3`

**Modified array:**

`[1, 2, 3, 2, 3]`

The first `k = 3` elements contain the unique values: `[1, 2, 3]`.

The elements after index `k - 1` do not matter.

## Complexity Analysis

- **Time Complexity:** `O(n)` — The array is traversed once.
- **Space Complexity:** `O(1)` — The solution modifies the original array without using an additional array.

## Key Concepts

- Two-pointer technique
- In-place array modification
- Sorted arrays
- Duplicate detection
- Time and space complexity