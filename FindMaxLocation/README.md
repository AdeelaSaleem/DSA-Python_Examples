# Find Max Location Function

This Python function `find_max_location(data)` is used to find the maximum value and its index in a given array.

## Function Description

The function takes an input array `data` and iterates through it to find the maximum value and its corresponding index.

### Code Snippet

```python
def find_max_location(data):
    K = 1
    LOC = 1
    MAX = data[0]
    while K < len(data):
        if MAX < data[K]:
            LOC = K
            MAX = data[K]
        K += 1
    return LOC, MAX

# Example usage:
data_array = [3, 7, 2, 8, 5]
location, maximum_value = find_max_location(data_array)
print(f"Location of the maximum value: {location}")
print(f"Maximum value: {maximum_value}")

## Dry Run Explanation
Input Data:
data_array = [3, 7, 2, 8, 5]

Initialize Variables:
K = 1
LOC = 1
MAX = data_array[0] # MAX initially 3

Dry Run Iteration:

First iteration (K = 1):
MAX (3) < data_array[1] (7): Update MAX to 7, LOC to 1.

Second iteration (K = 2):
MAX (7) >= data_array[2] (2): No change.

Third iteration (K = 3):
MAX (7) < data_array[3] (8): Update MAX to 8, LOC to 3.

Fourth iteration (K = 4):
MAX (8) >= data_array[4] (5): No change.

Fifth iteration (K = 5):

End of loop.
Output:


LOC = 3 (index of maximum value)

MAX = 8 (maximum value)

Final Result:

Maximum value in data_array: 8 (at index 3)


This README provides an overview of the `find_max_location` function, its code snippet, and a detailed dry run explanation demonstrating how the function works with example input data.
