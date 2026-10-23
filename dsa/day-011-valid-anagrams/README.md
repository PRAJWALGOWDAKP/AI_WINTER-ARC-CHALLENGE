# Valid Anagram

## 📌 Problem Statement

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

An **anagram** is a word or string formed by rearranging the characters of another string, using exactly the same characters with the same frequencies.

**LeetCode:** [Valid Anagram — Problem 242](https://leetcode.com/problems/valid-anagram/)

## 💡 Approach: Sorting

The solution sorts both strings and compares the results.

1. Use `sorted(s)` to arrange the characters of `s` in alphabetical order.
2. Use `sorted(t)` to arrange the characters of `t` in alphabetical order.
3. Compare the two sorted lists.
4. If they are equal, return `True`; otherwise, return `False`.

## 🐍 Python Solution

```python
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
```

## 🧪 Examples

### Example 1

**Input:**
```text
s = "anagram"
t = "nagaram"
```

**Output:**
```text
True
```

**Explanation:** Both strings contain the same characters with the same frequencies.

### Example 2

**Input:**
```text
s = "rat"
t = "car"
```

**Output:**
```text
False
```

**Explanation:** The strings contain different characters.

### Example 3

**Input:**
```text
s = "a"
t = "ab"
```

**Output:**
```text
False
```

**Explanation:** The strings have different lengths and cannot be anagrams.

## 🔍 Dry Run

Input:

```python
s = "listen"
t = "silent"
```

| Step | Operation | Result |
|---|---|---|
| 1 | `sorted(s)` | `['e', 'i', 'l', 'n', 's', 't']` |
| 2 | `sorted(t)` | `['e', 'i', 'l', 'n', 's', 't']` |
| 3 | Compare both lists | `True` |

Since both sorted lists are identical, the strings are anagrams.

## ⏱️ Complexity Analysis

Let `n` be the length of `s` and `m` be the length of `t`.

- **Time Complexity:** `O(n log n + m log m)` — sorting both strings takes time proportional to their lengths multiplied by the logarithm of their lengths.
- **Space Complexity:** `O(n + m)` — `sorted()` creates new lists containing the characters of both strings.

## 📚 Key Concepts Learned

- String manipulation.
- Python's built-in `sorted()` function.
- List comparison.
- Anagram detection.
- Time and space complexity analysis.

## 🚀 Alternative Approach

A character-frequency counting approach can solve this problem in `O(n + m)` time by counting the occurrences of each character rather than sorting the strings.

## ✅ Key Takeaway

Sorting provides a simple and readable way to check whether two strings are anagrams. If their sorted characters are identical, both strings contain exactly the same characters with the same frequencies.
