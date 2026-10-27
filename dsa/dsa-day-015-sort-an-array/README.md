# Merge Sort – LeetCode

## Problem Statement
Given an integer array `nums`, sort the array in ascending order and return it.

## Approach: Merge Sort

Merge Sort is a **Divide and Conquer** sorting algorithm. It divides an array into smaller subarrays, sorts them recursively, and merges them to produce a sorted array.

### Algorithm

1. **Base Case:** If the array contains zero or one element, return it because it is already sorted.
2. **Divide:** Find the middle index and split the array into two halves.
3. **Recursively Sort:** Call `sortArray()` on both halves to sort them independently.
4. **Merge:** Use `merge_array()` to combine the two sorted halves into one sorted array.
5. **Return:** Return the final sorted array.

## Example

**Input:**
```python
nums = [5, 2, 3, 1]
```

**Output:**
```python
[1, 2, 3, 5]
```

### Dry Run

**Step 1: Divide the array**
```text
[5, 2, 3, 1]
      /    \
  [5, 2]  [3, 1]
   /  \    /  \
 [5] [2] [3] [1]
```

**Step 2: Merge the sorted subarrays**
```text
[5] + [2]  → [2, 5]
[3] + [1]  → [1, 3]

[2, 5] + [1, 3] → [1, 2, 3, 5]
```

**Final Sorted Array:** `[1, 2, 3, 5]`

## Complexity Analysis

- **Time Complexity:** `O(n log n)` — The array is divided into approximately `log n` levels, and merging at each level takes `O(n)` time.
- **Auxiliary Space Complexity:** `O(n)` — Temporary arrays are created during merging, along with the recursion stack.

## Key Concepts Learned

- Divide and Conquer
- Recursion
- Array slicing
- Merging two sorted arrays
- Time and space complexity analysis

## Conclusion

Merge Sort efficiently sorts an array using recursion and merging. It guarantees `O(n log n)` time complexity for best, average, and worst cases.
