def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# usage:
data = [3, 7, 2, 8, 5]
target_item = 8
result = linear_search(data, target_item)

if result != -1:
    print(f"Target item {target_item} found at index {result}.")
else:
    print("Target item not found in the list.")




