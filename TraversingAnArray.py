def linear_traversal(arr):
     # Iterate through the array using a for loop
    for i in range(len(arr)):
          # Process each element of the array
        print(f"Processing element: {arr[i]}")
    print()    
  #array for traversal      
my_array=[10,20,30,40,50]  
  # Call the linear traversal function
linear_traversal(my_array)

# ---------------- Separate Functions for Traversal ------------------------


def process_element(element):
     # Process each element
     print(f"Processing element : {element}")
     
def traverse_array(arr, lower_bound, upper_bound, process_func): 
         # Iterate through the array using a for loop
          for i in range(lower_bound, upper_bound + 1 ):
        # Call the process function to handle each element
              process_func(arr[i])
 
 #create an array
linear_array = [1, 2, 3, 4, 5]
# Set lower and upper bounds
lower_bound=0
upper_bound=len(linear_array)- 1

# Call the function to traverse the array with process_element function
traverse_array(linear_array, lower_bound, upper_bound, process_element)
 




