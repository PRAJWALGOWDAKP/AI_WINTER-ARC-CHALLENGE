# LeetCode 258: Add Digits

## Problem
Given an integer `num`, repeatedly add all its digits until the result has only one digit. Return that single-digit result.

## Approach
1. Check whether `num` is a single-digit number (`num < 10`). If so, return it.
2. Initialize `s = 0` to store the sum of the digits.
3. Use a `while` loop to extract each digit using `% 10`.
4. Add each digit to `s`.
5. Remove the last digit using `// 10`.
6. Recursively call `addDigits(s)` until a single digit remains.

## Python Concepts Used
- Recursion
- `while` loop
- Modulus operator (`%`)
- Floor division operator (`//`)
- Base case and recursive case

## Example

**Input:** `199`

**Execution:**
- `1 + 9 + 9 = 19`
- `1 + 9 = 10`
- `1 + 0 = 1`

**Output:** `1`

## Complexity Analysis
- **Time Complexity:** O(log n) for each digit-summing pass, with O(log n) passes in the worst case; overall O(log n × log log n) for positive integers.
- **Space Complexity:** O(log log n) auxiliary recursion stack space for positive integers greater than 9.

## LeetCode
[258. Add Digits](https://leetcode.com/problems/add-digits/)