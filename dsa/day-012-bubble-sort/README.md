# Bubble Sort in Python

## 📌 Problem Statement

Implement Bubble Sort to arrange a list of integers in both ascending and descending order using adjacent comparisons and swaps.

- **Ascending Order:** Smallest to largest.
- **Descending Order:** Largest to smallest.

## 💡 Approach

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

### 1. Bubble Sort in Ascending Order

1. Start from the beginning of the list.
2. Compare adjacent elements, `nums[j]` and `nums[j + 1]`.
3. If the current element is greater than the next element, swap them.
4. After each pass, the largest remaining element moves to its correct position at the end.
5. Repeat until the list is sorted or a pass completes without any swaps.

### 2. Bubble Sort in Descending Order

1. Start from the beginning of the list.
2. Compare adjacent elements.
3. If the current element is smaller than the next element, swap them.
4. After each pass, the largest remaining element moves toward the beginning.
5. Repeat until the list is sorted or a pass completes without any swaps.

## 🧪 Example

**Input:**
```python
nums = [5, 8, 1, 6, 9, 2, 4]
```

**Output:**
```text
Ascending Order:  [1, 2, 4, 5, 6, 8, 9]
Descending Order: [9, 8, 6, 5, 4, 2, 1]
```

## ⚙️ Optimization

The variable `is_swap` tracks whether any swaps occur during a pass.

- If a swap occurs, `is_swap` becomes `True`.
- If no swaps occur, the list is already sorted, so the loop terminates early.

This optimization improves performance for already sorted lists.

## ⏱️ Time Complexity

Let `n` be the number of elements.

| Case | Time Complexity |
|---|---|
| Best Case | O(n), with early termination |
| Average Case | O(n²) |
| Worst Case | O(n²) |

## 💾 Space Complexity

**O(1)** — Bubble Sort sorts the list in place and uses only a constant amount of additional memory.

## 🎯 Key Concepts

- Nested loops
- Adjacent element comparisons
- Swapping elements
- In-place sorting
- Early termination optimization
- Ascending and descending order

## ⚠️ Important Note

Both functions modify the original list in place. Therefore, calling `bubblesort_desc(nums)` after `bubblesort_asc(nums)` sorts the already ascending list in descending order.

If you want to sort the original list independently in both directions, use a copy of the list for each function.

## ✅ Conclusion

Bubble Sort is a simple sorting algorithm that repeatedly compares adjacent elements and swaps them when necessary. Its early termination optimization makes it efficient for already sorted lists, but its quadratic average and worst-case time complexity makes it unsuitable for large datasets.
