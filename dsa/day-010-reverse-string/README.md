# LeetCode 344: Reverse String

## Problem
Given a list of characters `s`, reverse the list in-place without using extra space for another list.

## Approach
1. Initialize two pointers:
   - `i = 0` points to the first character.
   - `j = len(s) - 1` points to the last character.
2. Use a `while` loop that continues while `i < j`.
3. Swap the characters at positions `i` and `j` using Python's tuple unpacking.
4. Move `i` one position forward and `j` one position backward.
5. Stop when the pointers meet or cross.

**Note:** LeetCode expects you to modify `s` in-place and not return anything. Your algorithm is correct, but remove `return s` for the required submission format.

## Python Concepts Used
- Two-pointer technique
- `while` loops
- Tuple unpacking for swapping
- In-place modification
- `len()` function

## Example

**Input:**
```python
s = ["h", "e", "l", "l", "o"]
```

**Execution:**

| Step | List | i | j |
|---|---|---:|---:|
| Initial | `h e l l o` | 0 | 4 |
| Swap 1 | `o e l l h` | 1 | 3 |
| Swap 2 | `o l l e h` | 2 | 2 |
| Finished | `o l l e h` | 2 | 2 |

**Output:** `["o", "l", "l", "e", "h"]`

## Complexity Analysis
- **Time Complexity:** O(n), because each character is processed at most once.
- **Space Complexity:** O(1), because the reversal uses only two pointers and swaps elements in the original list.

## LeetCode
[344. Reverse String](https://leetcode.com/problems/reverse-string/)