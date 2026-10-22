# LeetCode 1952: Three Divisors

## Problem
Given an integer `n`, return `True` if `n` has exactly three positive divisors. Otherwise, return `False`.

## Approach
1. Initialize `count = 0` to count the divisors.
2. Iterate from `1` to `n` using a `for` loop.
3. Check whether `n % i == 0`. If the remainder is zero, `i` is a divisor of `n`.
4. Increment `count` for every divisor found.
5. If `count == 3`, return `True`; otherwise, return `False`.

## Python Concepts Used
- `for` loop
- Modulus operator (`%`)
- Conditional statements (`if-else`)
- Counting divisors
- Boolean return values

## Example 1

**Input:** `n = 4`

Divisors: `1, 2, 4`

Number of divisors: `3`

**Output:** `True`

## Example 2

**Input:** `n = 10`

Divisors: `1, 2, 5, 10`

Number of divisors: `4`

**Output:** `False`

## Complexity Analysis
- **Time Complexity:** O(n), because the loop checks every integer from `1` to `n`.
- **Space Complexity:** O(1), because only a counter and loop variable are used.

## Optimization
You can solve this problem more efficiently by checking whether `n` is a perfect square of a prime number. That approach takes O(√n) time.

## LeetCode
[1952. Three Divisors](https://leetcode.com/problems/three-divisors/)