# LeetCode 204: Count Primes

## Problem
Given an integer `n`, return the number of prime numbers strictly less than `n`.

A prime number is a number greater than `1` that has exactly two positive divisors: `1` and itself.

## Approach
1. Initialize `count = 0` to count the prime numbers.
2. Iterate through numbers from `2` to `n - 1`.
3. Assume each number `i` is prime by setting `is_prime = True`.
4. Check whether any number from `2` to `i - 1` divides `i` evenly.
5. If `i % j == 0`, the number is not prime. Set `is_prime = False` and stop checking using `break`.
6. If `is_prime` remains `True`, increment `count`.
7. Return the total number of prime numbers found.

## Python Concepts Used
- Nested `for` loops
- Boolean variables
- Modulus operator (`%`)
- `break` statement
- Conditional statements
- Counting

## Example

**Input:** `n = 10`

Numbers checked: `2, 3, 4, 5, 6, 7, 8, 9`

Prime numbers: `2, 3, 5, 7`

**Output:** `4`

## Complexity Analysis
- **Time Complexity:** O(n²) in the worst case, due to the nested loops.
- **Space Complexity:** O(1), because only a few variables are used.

## Optimization
You can improve the solution by checking divisors only up to `√i` instead of `i - 1`. For larger inputs, the Sieve of Eratosthenes is even more efficient, with O(n log log n) time complexity and O(n) space complexity.

## LeetCode
[204. Count Primes](https://leetcode.com/problems/count-primes/)