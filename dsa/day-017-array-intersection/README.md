# Intersection of Two Arrays

## Problem Statement

Given two integer arrays `nums1` and `nums2`, return an array containing their intersection.

Each element in the result must be unique, regardless of how many times it appears in the input arrays.

The result can be returned in any order.

## Example 1

**Input:**
```python
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
```

**Output:**
```python
[2]
```

## Example 2

**Input:**
```python
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
```

**Output:**
```python
[9, 4]
```

**Explanation:** `[4, 9]` is also an accepted output.

## Approach: Brute Force (Nested Loops)

We use nested loops to compare elements from both arrays.

### Algorithm

1. Create an empty list called `res` to store common elements.
2. Traverse the first array using `i`.
3. Traverse the second array using `j`.
4. Compare `nums1[i]` with `nums2[j]`.
5. If both elements are equal:
   - Check whether the element already exists in `res`.
   - If it does not exist, append it to `res`.
6. Return the result.

## Python Solution

```python
class Solution(object):
    def intersection(self, nums1, nums2):
        res = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if nums1[i] not in res:
                        res.append(nums1[i])

        return res
```

## Complexity Analysis

Let:
- `n` = length of `nums1`
- `m` = length of `nums2`

- **Time Complexity:** O(n × m × r) in the worst case, where `r` is the number of unique elements in the result, because checking `not in res` takes O(r).
- **Space Complexity:** O(r) for storing unique common elements.

## Key Concepts

- Arrays
- Nested Loops
- Linear Search
- Duplicate Handling
- Brute Force Approach

**LeetCode:** Intersection of Two Arrays