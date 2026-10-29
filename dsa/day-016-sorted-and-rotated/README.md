# Check if Array Is Sorted and Rotated

## Problem Statement

Given an integer array `nums`, return `True` if the array was originally sorted in non-decreasing order and then rotated some number of positions. Otherwise, return `False`.

## Approach: Count the Descending Pairs

The main idea is to count how many times an element is greater than the next element.

### Algorithm

1. Initialize `count = 0` to track the number of descending pairs.
2. Traverse the array using a loop.
3. Compare each element `nums[i]` with the next element `nums[(i + 1) % n]`.
4. If the current element is greater than the next element, increment `count`.
5. After checking all elements, return `True` if `count` is less than or equal to `1`; otherwise, return `False`.

## Why Use `(i + 1) % n`?

The modulo operator allows us to compare the last element with the first element.

For example, in `[3, 4, 5, 1, 2]`, the last element `2` is compared with the first element `3`.

This ensures that the rotation point at the end of the array is also checked.

## Example 1

**Input:**
`nums = [3, 4, 5, 1, 2]`

**Output:**
`True`

**Explanation:**

There is only one descending pair: `5 > 1`. Therefore, the array is sorted and rotated.

## Example 2

**Input:**
`nums = [2, 1, 3, 4]`

**Output:**
`False`

**Explanation:**

There are two descending pairs when checking circularly: `2 > 1` and `4 > 2`. Since the count is greater than `1`, the array is not sorted and rotated.

## Complexity Analysis

- **Time Complexity:** `O(n)` — Each element is checked once.
- **Space Complexity:** `O(1)` — Only a counter and a variable for the array length are used.

## Key Concepts

- Array traversal
- Circular array indexing
- Modulo operator (`%`)
- Counting descending pairs
- Conditional statements