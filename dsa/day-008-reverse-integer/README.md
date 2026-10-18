Given a signed 32-bit integer x, reverse its digits and return the reversed integer.

If the reversed integer falls outside the signed 32-bit integer range, return 0.

Examples

Example 1

Input: x = 123

Output: 321

Explanation: The digits of 123 are reversed to get 321.

Example 2

Input: x = -123

Output: -321

Explanation: The negative sign is preserved.

Approach

The problem is solved using the modulo (%) and floor division (//) operators.

Initialize rev = 0 to store the reversed number.

Store the sign of the original number.

Convert the number to its absolute value using abs(x).

Use a while loop to extract the last digit using x % 10.

Append the extracted digit to the reversed number using rev = rev * 10 + num.

Remove the last digit using x = x // 10.

Restore the original sign.

Check whether the reversed number is within the 32-bit signed integer range. If not, return 0.