# Linear Search Algorithm

This Python project implements a linear search algorithm to find an element in an array and returns its index if found, or -1 if not found.

## Algorithm Description

The `linear_search` function takes an input array `arr` and a target item `target`. It iterates through the array and checks if each element is equal to the target item. If a match is found, it returns the index of the element; otherwise, it returns -1.

### Code Snippet

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage:
data = [3, 7, 2, 8, 5]
target_item = 8
result = linear_search(data, target_item)

if result != -1:
    print(f"Target item {target_item} found at index {result}.")
else:
    print("Target item not found in the list.")

## Dry Run for find_max_location Function

# Input Data:
data_array = [3, 7, 2, 8, 5]


## Initialize Variables:
K = 1
LOC = 1
MAX = data_array[0] # MAX initially 3


## Dry Run Iteration:
- First iteration (K = 1):
  - MAX (3) < data_array[1] (7): Update MAX to 7, LOC to 1.
- Second iteration (K = 2):
  - MAX (7) >= data_array[2] (2): No change.
- Third iteration (K = 3):
  - MAX (7) < data_array[3] (8): Update MAX to 8, LOC to 3.
- Fourth iteration (K = 4):
  - MAX (8) >= data_array[4] (5): No change.
- Fifth iteration (K = 5):
  - End of loop.

## Output:
- LOC = 3 (index of maximum value)
- MAX = 8 (maximum value)

## Final Result:
- Maximum value in data_array: 8 (at index 3)


This README provides an overview of the linear search algorithm, its implementation in Python, and a detailed dry run explanation demonstrating how the algorithm works with example input data.
