# LeetCode 509: Fibonacci Number

## Problem
The Fibonacci sequence is a sequence of numbers where each number is the sum of the two preceding numbers.

The sequence starts with:

`0, 1, 1, 2, 3, 5, 8, 13, 21, ...`

Given an integer `n`, return the `n`th Fibonacci number.

## Approach
1. **Base case:** If `n == 0` or `n == 1`, return `n`.
2. **Recursive case:** Calculate the sum of the previous two Fibonacci numbers using `self.fib(n-1) + self.fib(n-2)`.
3. Continue recursively until the base cases are reached.

## Python Concepts Used
- Recursion
- Base cases
- Recursive function calls
- Return statements

## Example

**Input:** `n = 5`

**Execution:**
- `fib(5) = fib(4) + fib(3)`
- `fib(4) = fib(3) + fib(2)`
- `fib(3) = fib(2) + fib(1)`
- `fib(2) = fib(1) + fib(0) = 1`

The final result is:

**Output:** `5`

## Complexity Analysis
- **Time Complexity:** O(2ⁿ) — repeated recursive calls calculate the same Fibonacci values multiple times.
- **Space Complexity:** O(n) — the maximum recursion depth is proportional to `n`.

## Optimization
An iterative approach using two variables can solve the problem in O(n) time and O(1) extra space.

## LeetCode
[509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)