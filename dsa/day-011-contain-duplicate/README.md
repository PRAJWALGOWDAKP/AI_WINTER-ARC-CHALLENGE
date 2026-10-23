# Contains Duplicate

## 📌 Problem Statement

Given an integer array `nums`, return `True` if any value appears at least twice in the array. Return `False` if every element is distinct.

**LeetCode:** [Contains Duplicate — Problem 217](https://leetcode.com/problems/contains-duplicate/)

## 💡 Approach: Hash Set

Use a Python set to keep track of the numbers that have already been visited.

1. Create an empty set called `seen`.
2. Iterate through each number in the array.
3. If the number already exists in `seen`, return `True`.
4. Otherwise, add the number to `seen`.
5. If the loop finishes without finding a duplicate, return `False`.

## 🐍 Python Solution

```python
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False
```

## 🧪 Examples

### Example 1

**Input:**
```text
nums = [1, 2, 3, 1]
```

**Output:**
```text
True
```

**Explanation:** The number `1` appears twice.

### Example 2

**Input:**
```text
nums = [1, 2, 3, 4]
```

**Output:**
```text
False
```

**Explanation:** Every element is distinct.

### Example 3

**Input:**
```text
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
```

**Output:**
```text
True
```

**Explanation:** Multiple elements appear more than once.

## 🔍 Dry Run

Input: `nums = [1, 2, 3, 2]`

| Number (`n`) | Set (`seen`) before checking | Action |
|---|---|---|
| 1 | `{}` | Add 1 |
| 2 | `{1}` | Add 2 |
| 3 | `{1, 2}` | Add 3 |
| 2 | `{1, 2, 3}` | Duplicate found; return `True` |

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(n)` average — each element is checked and inserted into the set in average constant time.
- **Space Complexity:** `O(n)` — in the worst case, the set stores all `n` elements.

Here, `n` represents the length of the input array.

## 📚 Key Concepts Learned

- Python sets and unique elements.
- Hash-based lookup.
- Duplicate detection.
- Early return to stop unnecessary iterations.
- Time and space complexity analysis.

## ✅ Key Takeaway

A set makes duplicate detection efficient by allowing fast membership checks. Instead of comparing every element with every other element, we track previously visited numbers and return immediately when a duplicate is found.
