# LeetCode 326: Power of Three

## Problem
Given an integer `n`, return `True` if it is a power of three. Otherwise, return `False`.

A number is a power of three if it can be expressed as \(3^x\), where \(x\) is a non-negative integer.

Examples: `1, 3, 9, 27, 81, 243, ...`

## Approach
1. Check whether `n <= 0`. If so, return `False`, because powers of three are positive.
2. Use a `while` loop to check whether `n % 3 == 0`.
3. If divisible by 3, divide `n` by 3 using integer division (`//`).
4. Repeat until `n` is no longer divisible by 3.
5. Return `n == 1`. If the final value is `1`, the original number was a power of three.

## Python Concepts Used
- `while` loop
- Modulus operator (`%`)
- Floor division (`//`)
- Conditional statements
- Boolean return values

## Example

**Input:** `n = 27`

**Execution:**
- `27 / 3 = 9`
- `9 / 3 = 3`
- `3 / 3 = 1`

Now `n == 1`, so the result is `True`.

**Output:** `True`

## Complexity Analysis
- **Time Complexity:** O(log₃ n), because the number is divided by 3 repeatedly.
- **Space Complexity:** O(1), because only a constant amount of extra space is used.

## LeetCode
[326. Power of Three](https://leetcode.com/problems/power-of-three/)