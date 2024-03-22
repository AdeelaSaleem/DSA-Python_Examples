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

data_array = [3, 7, 2, 8, 5]
location, maximum_value = find_max_location(data_array)
print(f"Location of the maximum value: {location}")
print(f"Maximum value: {maximum_value}")
