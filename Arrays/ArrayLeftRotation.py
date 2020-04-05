# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
# We will use the juggling algorithm
import array, math

# O(n*d)
def array_left_rotate(arr_to_work):
    size_of_array = len(arr_to_work)
    temp_element = arr_to_work[0]
    for i in range(size_of_array-1):
      arr_to_work[i] = arr_to_work[i + 1]
    arr_to_work[size_of_array-1] = temp_element

# O(n)
def array_left_rotate_juggling_algorithm(arr_to_work,d):
    size_of_array = len(arr_to_work)
    gcd = math.gcd(size_of_array,d)
    for i in range(gcd):
        # i is the current position.
        temp_element_to_swap = arr_to_work[i]
        # j position of the current set's first element.
        j = i
        while 1:
            # K is the temporary position which keeps first element of the set, which moves to the next set.
            k = j + d
            if k >= size_of_array:
                k -= size_of_array
            if k == i:
                break
            arr_to_work[j] = arr_to_work[k]
            # move to the next set in the array and start
            j = k
        arr_to_work[j] = temp_element_to_swap

def array_reverse_subset(arr_to_work, start, end):
    while(start<end):
        temp = arr_to_work[start]
        arr_to_work[start] = arr_to_work[end]
        arr_to_work[end] = temp
        start += 1
        end -= 1

# O(n)
def array_rotate_reversal_algorithm(arr_to_work, d):
    size_of_array = len(arr_to_work)
    array_reverse_subset(arr_to_work, 0, d - 1)
    array_reverse_subset(arr_to_work, d, size_of_array-1)
    #array_reverse(arr_to_work, 0, size_of_array-1)
    arr_to_work.reverse()

arr_to_work = array.array('i', [1,2,3,4,5,6,7,8])
array_rotate_reversal_algorithm(arr_to_work, 2)
# array_left_rotate_juggling_algorithm(arr_to_work,2) 
# for i in range(3):
    # array_left_rotate(arr_to_work)
print(arr_to_work.tolist())