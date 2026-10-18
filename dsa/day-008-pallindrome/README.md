Given an integer x, return True if x is a palindrome; otherwise, return False.

A palindrome number reads the same forward and backward.


Examples

Example 1

Input: x = 121

Output: True

Explanation: 121 reads the same forward and backward.

Example 2

Input: x = -121

Output: False

Explanation: Reading backward gives 121-, which is not the same number.


Approach

This solution reverses the number using the modulo (%) and floor division (//) operators.

Store the original number in temp so it remains unchanged for comparison.

Initialize rev = 0 to store the reversed number.

Extract the last digit using x % 10.

Append the digit to rev using rev = rev * 10 + rem.

Remove the last digit using x = x // 10.

Repeat until x becomes zero.

Compare rev with temp. If they are equal, the number is a palindrome.