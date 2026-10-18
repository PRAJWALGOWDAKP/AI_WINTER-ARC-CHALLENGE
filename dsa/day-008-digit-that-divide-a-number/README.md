Problem Statement

Given an integer num, count how many digits in num divide the original number evenly.

A digit divides the number if the remainder is zero when the original number is divided by that digit.

Example 1

Input: num = 1248

Output: 4

Explanation:

1248 % 1 = 0

1248 % 2 = 0

1248 % 4 = 0

1248 % 8 = 0

All four digits divide the original number evenly.

Example 2

Input: num = 121

Output: 2

Explanation:

121 % 1 = 0

121 % 2 = 1

121 % 1 = 0

The digits 1 and 1 divide the original number evenly. Therefore, the count is 2.

Approach

The solution uses modulo (%) and floor division (//) to process each digit.

Store the original number in temp so it can be used for divisibility checks.

Initialize count = 0.

Extract the last digit using num % 10.

Check whether temp % rem == 0.

If the condition is true, increment count.

Remove the last digit using num = num // 10.

Repeat until all digits have been processed.

Return count.