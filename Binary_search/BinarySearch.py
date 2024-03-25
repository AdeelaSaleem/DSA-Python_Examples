def find_location(data, item, lb, ub):
    # Step 1: Initialize segment variables.
    beg, end = lb, ub
    mid = (beg + end) // 2
    
    # Step 2: Repeat steps 3 and 4 while BEG ≤ END and DATA[MID] ≠ ITEM.
    while beg <= end and data[mid] != item:
        # Step 3: If ITEM < DATA[MID], then set END = MID - 1. Else set BEG = MID + 1.
        if item < data[mid]:
            end = mid - 1
        else:
            beg = mid + 1
        
        # Step 4: Set MID = INT((BEG + END) / 2).
        mid = (beg + end) // 2
    
    # Step 5: If DATA[MID] = ITEM, then set LOC = MID. Else set LOC = None.
    if beg <= end:
        loc = mid
    else:
        loc = None
    
    # Step 6: Exit
    return loc

#  Usage:
data_array = [1, 3, 5, 7, 9]
target_item = 80
lower_bound = 0
upper_bound = len(data_array) - 1
location = find_location(data_array, target_item, lower_bound, upper_bound)
if location is not None:
    print(f"{target_item} found at position {location}.")
else:
    print(f"{target_item} not found in the array.")
