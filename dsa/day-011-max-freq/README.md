# Count Elements With Maximum Frequency

## 📌 Problem Statement

Given an array of positive integers `nums`, return the total frequencies of all elements that have the maximum frequency.

The **frequency** of an element is the number of times it appears in the array.

**LeetCode:** [3005. Count Elements With Maximum Frequency](https://leetcode.com/problems/count-elements-with-maximum-frequency/)

## 💡 Approach: Hash Map (Dictionary)

Use a Python dictionary to count how many times each element appears, then add the frequencies of all elements that share the maximum frequency.

1. Create an empty dictionary `freq`.
2. Iterate through `nums` and count each element's occurrences using `freq.get(n, 0) + 1`.
3. Find the highest frequency using `max(freq.values())`.
4. Initialize `total = 0`.
5. Iterate through the frequency values and add each count equal to `max_freq` to `total`.
6. Return `total`.

## 🐍 Python Solution

```python
class Solution(object):
    def maxFrequencyElements(self, nums):
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        max_freq = max(freq.values())
        total = 0

        for count in freq.values():
            if count == max_freq:
                total = total + count

        return total
```

## 🧪 Examples

### Example 1

**Input:**
```text
nums = [1, 2, 2, 3, 1, 4]
```

**Output:**
```text
4
```

**Explanation:** The numbers `1` and `2` both appear twice, which is the maximum frequency. Adding their frequencies gives `2 + 2 = 4`.

### Example 2

**Input:**
```text
nums = [1, 2, 3, 4, 5]
```

**Output:**
```text
5
```

**Explanation:** Every number appears once. All five elements share the maximum frequency, so the result is `5`.

## 🔍 Dry Run

Input: `nums = [1, 2, 2, 3, 1, 4]`

**Step 1: Build the frequency dictionary**

| Element | Frequency |
|---|---:|
| 1 | 2 |
| 2 | 2 |
| 3 | 1 |
| 4 | 1 |

Dictionary: `{1: 2, 2: 2, 3: 1, 4: 1}`

**Step 2: Find the maximum frequency**

`max_freq = 2`

**Step 3: Calculate the total**

| Frequency | Condition | Total |
|---:|---|---:|
| 2 | Equal to maximum | 2 |
| 2 | Equal to maximum | 4 |
| 1 | Not equal to maximum | 4 |
| 1 | Not equal to maximum | 4 |

**Final output:** `4`

## ⏱️ Complexity Analysis

Let `n` be the length of the input array and `k` be the number of distinct elements.

- **Time Complexity:** `O(n)` average — counting frequencies takes `O(n)`, finding the maximum takes `O(k)`, and summing the maximum frequencies takes `O(k)`. Since `k ≤ n`, the overall complexity is `O(n)`.
- **Space Complexity:** `O(k)` — the dictionary stores one entry per distinct element.

## 📚 Key Concepts Learned

- Python dictionaries and hash maps.
- Frequency counting with `dict.get()`.
- Finding maximum values with `max()`.
- Iterating over dictionary values.
- Accumulating a result using a variable.
- Time and space complexity analysis.

## ✅ Key Takeaway

A dictionary efficiently counts the occurrences of each element. By finding the maximum frequency and summing every element's frequency that matches it, we can solve this problem in linear time on average.
