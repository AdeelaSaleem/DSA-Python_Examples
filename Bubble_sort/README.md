# Bubble Sort Algorithm

This repository contains a Python implementation of the bubble sort algorithm to sort an array of elements.

## Introduction
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

## Algorithm Overview
1. Start with an unsorted array of elements.
2. Repeat the following steps for each element in the array:
   a. Compare the current element with the next element.
   b. If the current element is greater than the next element, swap them.
3. After each pass, the largest unsorted element will move to its correct position.
4. Repeat the process until no more swaps are needed, indicating that the array is sorted.

## Dry Run Explanation
Consider the following unsorted array: `arr = [5, 3, 8, 2, 1]`

First pass:
- Compare 5 and 3, no swap.
- Compare 5 and 8, no swap.
- Compare 8 and 2, swap to get `[5, 3, 2, 8, 1]`.
- Compare 8 and 1, swap to get `[5, 3, 2, 1, 8]`.

Second pass:
- Compare 5 and 3, swap to get `[3, 5, 2, 1, 8]`.
- Compare 5 and 2, swap to get `[3, 2, 5, 1, 8]`.
- Compare 5 and 1, swap to get `[3, 2, 1, 5, 8]`.

Third pass:
- Compare 3 and 2, swap to get `[2, 3, 1, 5, 8]`.
- Compare 3 and 1, swap to get `[2, 1, 3, 5, 8]`.

Fourth pass:
- Compare 2 and 1, swap to get `[1, 2, 3, 5, 8]`.

Fifth pass:
- No swaps needed, array is sorted.

## Usage
To use the bubble sort algorithm, call the `bubble_sort` function with the array you want to sort. For example:
```python
arr = [5, 3, 8, 2, 1]
bubble_sort(arr)
print("Sorted array:", arr)  # Output: [1, 2, 3, 5, 8]
```

## Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## Code
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
arr = [5, 3, 8, 2, 1]
bubble_sort(arr)
print("Sorted array:", arr)  # Output: [1, 2, 3, 5, 8]
```
