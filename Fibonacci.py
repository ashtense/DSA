fibonacci_array = []
for number in range(0,9): # O(n)
    if(number < 2):       # O(1) * 2
        fibonacci_array.append(1) #O(1)
    else:
        length_of_array = len(fibonacci_array) # O(1)
        element_to_add = fibonacci_array[length_of_array - 1] + fibonacci_array[length_of_array - 2] # O(1)
        fibonacci_array.append(element_to_add) O(1)
print(fibonacci_array)