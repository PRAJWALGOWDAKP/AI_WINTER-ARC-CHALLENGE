# Insertion Sort in Python

## 📌 Problem Statement

Implement the Insertion Sort algorithm to arrange elements in ascending and descending order.

This implementation covers:
- Insertion Sort for arrays in ascending order.
- Insertion Sort for arrays in descending order.
- Insertion Sort for a singly linked list in ascending order.

## 💡 Approach

Insertion Sort divides the array into two portions: a sorted portion and an unsorted portion.

It takes one element from the unsorted portion and inserts it into its correct position in the sorted portion.

### 1. Array Insertion Sort — Ascending Order

1. Start from index `1`, treating the first element as sorted.
2. Store the current element in `key`.
3. Compare `key` with the elements to its left.
4. Shift larger elements one position to the right.
5. Insert `key` into its correct position.
6. Repeat until the array is sorted.

### 2. Array Insertion Sort — Descending Order

1. Start from index `1`.
2. Store the current element in `key`.
3. Compare `key` with the elements to its left.
4. Shift smaller elements one position to the right.
5. Insert `key` into its correct position.
6. Repeat until the array is sorted in descending order.

### 3. Linked List Insertion Sort — Ascending Order

The linked list implementation uses a different approach because linked lists do not support direct index-based access.

1. Create a dummy node to simplify insertion at the beginning.
2. Traverse the original linked list using `curr`.
3. Use `prev` to find the correct insertion position in the sorted list.
4. Save the next node in `next_node` before changing links.
5. Disconnect the current node from its original position and insert it into the sorted list.
6. Continue until all nodes are inserted.
7. Return `dummy.next`, the head of the sorted linked list.

## 🧪 Example

**Input:**
```python
nums = [3, 5, 6, 4, 8, 9, 10, 7, 1]
```

**Output:**
```text
Ascending Order:  [1, 3, 4, 5, 6, 7, 8, 9, 10]
Descending Order: [10, 9, 8, 7, 6, 5, 4, 3, 1]
```

## 🔑 Important Variables

| Variable | Purpose |
|---|---|
| `key` | Stores the element to be inserted into its correct position. |
| `i` | Iterates through the unsorted portion of the array. |
| `j` | Moves backward through the sorted portion of the array. |
| `dummy` | Provides a starting point for building the sorted linked list. |
| `curr` | Tracks the current node being processed. |
| `prev` | Finds the insertion position in the sorted linked list. |
| `next_node` | Saves the next original node before modifying links. |

## ⏱️ Time Complexity

### Array Insertion Sort

| Case | Complexity |
|---|---|
| Best Case | O(n) |
| Average Case | O(n²) |
| Worst Case | O(n²) |

The best case occurs when the array is already sorted in the required order. The worst case occurs when the elements are arranged in reverse order.

### Linked List Insertion Sort

| Case | Complexity |
|---|---|
| Best Case | O(n) |
| Average Case | O(n²) |
| Worst Case | O(n²) |

In the worst case, each node may need to be compared with many nodes already inserted into the sorted list.

## 💾 Space Complexity

- **Array Insertion Sort:** O(1) auxiliary space because sorting is performed in place.
- **Linked List Insertion Sort:** O(1) auxiliary space because existing nodes are rearranged without creating a separate collection of nodes.

## ⚠️ Important Note

Both array sorting functions modify the original list. Therefore, calling `insertion_sort_desc(nums)` after `insertion_sort_asc(nums)` sorts the already ascending list in descending order.

This works correctly for producing both outputs, but to sort the original input independently, pass `nums.copy()` to each function.

## 🎯 Key Concepts

- Insertion Sort
- Sorted and unsorted portions
- Shifting elements
- Inserting elements at the correct position
- Singly linked lists
- Dummy nodes and pointer manipulation
- In-place sorting

## ✅ Conclusion

Insertion Sort builds a sorted sequence one element at a time. The array implementation shifts elements to make room for each key, while the linked list implementation rearranges node links. Both approaches are easy to understand but can be inefficient for large datasets because their average time complexity is O(n²).
