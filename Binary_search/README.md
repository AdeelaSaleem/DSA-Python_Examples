# Binary Search Algorithm

This repository contains a Python implementation of the binary search algorithm to find the location of an item in a sorted array.

## Introduction

Binary search is a search algorithm that finds the position of a target value within a sorted array. It works by repeatedly dividing the search interval in half. This algorithm is efficient for large datasets and has a time complexity of O(log n).

## Algorithm Overview

Initialize segment variables (beg, end, mid) based on the lower and upper bounds of the array.
Repeat steps 3 and 4 while beg is less than or equal to end and the value at data[mid] is not equal to the target item.
If the target item is less than the value at data[mid], update end to mid - 1; otherwise, update beg to mid + 1.
Update mid as the middle index of the new segment ((beg + end) // 2).
If the value at data[mid] is equal to the target item, set LOC (location) to mid; otherwise, set LOC to None.
Exit the algorithm and return the value of LOC.

## Dry Run Explanation

Initial values:
data_array = [1, 3, 5, 7, 9]
target_item = 80
lower_bound = 0
upper_bound = 4
beg = 0, end = 4, mid = 2

First iteration:

data[mid] = 5

Since target_item (80) > data[mid] (5), set beg = mid + 1 = 3, end = 4, mid = 3

Second iteration:

data[mid] = 7

Since target_item (80) > data[mid] (7), set beg = mid + 1 = 4, end = 4, mid = 4

Third iteration:

data[mid] = 9

Since target_item (80) > data[mid] (9) and beg <= end, loop exits.

After the loop, since beg > end, set loc = None.

Final output: None

## Usage

To use the binary search algorithm, call the find_location function with the following parameters:
data: The sorted array to search in.
item: The target item to find.
lb: The lower bound index of the array.
ub: The upper bound index of the array.

## Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

### Code

```python
data_array = [1, 3, 5, 7, 9]
target_item = 80
lower_bound = 0
upper_bound = len(data_array) - 1
location = find_location(data_array, target_item, lower_bound, upper_bound)
if location is not None:
    print(f"{target_item} found at position {location}.")
else:
    print(f"{target_item} not found in the array.")
