# Selection Sort in Python

## 📌 Problem Statement

Implement **Selection Sort** to sort a list of integers in both ascending and descending order.

- **Ascending Order:** Sort elements from smallest to largest.
- **Descending Order:** Sort elements from largest to smallest.

## 💡 Approach

Selection Sort divides the list into two parts:
- **Sorted portion:** Elements already placed in their correct positions.
- **Unsorted portion:** Elements that still need to be sorted.

### 1. Selection Sort in Ascending Order

1. Start from the first index.
2. Assume the current element is the minimum element.
3. Traverse the remaining unsorted portion to find the smallest element.
4. Swap the smallest element with the element at the current index.
5. Repeat until the entire list is sorted.

### 2. Selection Sort in Descending Order

1. Start from the first index.
2. Assume the current element is the maximum element.
3. Traverse the remaining unsorted portion to find the largest element.
4. Swap the largest element with the element at the current index.
5. Repeat until the entire list is sorted.

## 🧪 Example

**Input:**
```python
l = [1, 7, 8, 4, 5, 6, 9, 2]
```

**Output:**
```text
Ascending Order:  [1, 2, 4, 5, 6, 7, 8, 9]
Descending Order: [9, 8, 7, 6, 5, 4, 2, 1]
```

## ⏱️ Time Complexity

| Case | Complexity |
|---|---|
| Best Case | O(n²) |
| Average Case | O(n²) |
| Worst Case | O(n²) |

**Reason:** The algorithm uses nested loops to find the minimum or maximum element in the remaining unsorted portion.

## 💾 Space Complexity

**O(1)** — Selection Sort sorts the list in place and uses only a constant amount of additional memory.

## ✅ Key Concepts

- Nested loops
- Finding minimum and maximum elements
- Index tracking using `min_index` and `max_index`
- Swapping elements
- In-place sorting
- Ascending and descending order

## 🎯 Conclusion

Selection Sort repeatedly selects the smallest or largest element from the unsorted portion and places it in its correct position. It is easy to understand and implement, but its O(n²) time complexity makes it inefficient for large lists.
