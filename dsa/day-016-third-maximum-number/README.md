# Third Maximum Number

## Problem Statement

Given an integer array `nums`, return the **third distinct maximum number** in the array. If the third maximum does not exist, return the maximum number.

## Approach: Three Variables

We maintain three variables:

- `first`: Stores the largest distinct number.
- `second`: Stores the second-largest distinct number.
- `third`: Stores the third-largest distinct number.

Initially, all three variables are set to negative infinity (`float('-inf')`) to indicate that no number has been assigned yet.

### Algorithm

1. Initialize `first`, `second`, and `third` to negative infinity.
2. Traverse each number in the array.
3. If the number already exists among `first`, `second`, and `third`, skip it to avoid duplicates.
4. If the number is greater than `first`, update all three variables by shifting their values.
5. Otherwise, if it is greater than `second`, update `second` and `third`.
6. Otherwise, if it is greater than `third`, update `third`.
7. After traversing the array:
   - If `third` is still negative infinity, return `first`.
   - Otherwise, return `third`.

## Python Solution

```python
class Solution(object):
    def thirdMax(self, nums):
        first = second = third = float('-inf')

        for num in nums:
            if num in (first, second, third):
                continue
            elif num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num

        return first if third == float('-inf') else third
```

## Example

**Input:**
```python
nums = [3, 2, 1]
```

**Output:**
```python
1
```

**Explanation:**

- Largest distinct number: `3`
- Second-largest distinct number: `2`
- Third-largest distinct number: `1`

Therefore, the third maximum number is `1`.

## Complexity Analysis

- **Time Complexity:** `O(n)`, where `n` is the length of the array. We traverse the array once, and checking membership in a tuple of three elements takes constant time.
- **Space Complexity:** `O(1)`, because we use only three variables to track the maximum values.

## Key Concepts

- Array traversal
- Conditional statements
- Multiple variable assignment
- Handling duplicate values
- Tracking the three largest distinct numbers