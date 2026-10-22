# LeetCode 1979: Find Greatest Common Divisor of Array

## Problem
Given an integer array `nums`, find and return the greatest common divisor (GCD) of the smallest and largest numbers in the array.

## Approach
1. Find the smallest number using `min(nums)` and store it in `a`.
2. Find the largest number using `max(nums)` and store it in `b`.
3. Initialize `gcd = 0` to store the greatest common divisor found so far.
4. Iterate from `1` to `a` using a `for` loop.
5. Check whether both `a` and `b` are divisible by `i` using `a % i == 0 and b % i == 0`.
6. If both are divisible, update `gcd = i`.
7. Return `gcd`. Since the loop checks divisors in increasing order, the last matching divisor is the greatest one.

## Python Concepts Used
- Lists
- `min()` and `max()`
- `for` loops
- Modulus operator (`%`)
- Conditional statements
- Finding common divisors

## Example

**Input:** `nums = [7, 5, 6, 8, 3]`

- Smallest number: `3`
- Largest number: `8`
- Common divisors: `1`

**Output:** `1`

## Complexity Analysis
- **Time Complexity:** O(a), where `a` is the smallest number in the array.
- **Space Complexity:** O(1), because only a constant number of variables are used.

## Optimization
You can use the **Euclidean algorithm** to calculate the GCD more efficiently, with O(log b) time complexity.

## LeetCode
[1979. Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/)