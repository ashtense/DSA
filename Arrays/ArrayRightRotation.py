import array, math

def array_reverse_subset(arr_to_work, start, end):
    while(start<end):
        temp = arr_to_work[start]
        arr_to_work[start] = arr_to_work[end]
        arr_to_work[end] = temp
        start += 1
        end -= 1

def array_right_rotate_reversal_algorithm(arr_to_work, d):
    size_of_array = len(arr_to_work)
    #array_reverse_subset(arr_to_work, 0, size_of_array-1)
    arr_to_work.reverse()
    array_reverse_subset(arr_to_work, 0, d - 1)
    array_reverse_subset(arr_to_work, d, size_of_array-1)

def array_right_rotation(arr_to_work):
    size_of_array = len(arr_to_work)
    temp_element = arr_to_work[size_of_array - 1]
    for i in range(size_of_array-1, 0, -1):
        arr_to_work[i] = arr_to_work[i - 1]
    arr_to_work[0] = temp_element

arr_to_work = array.array('i', [1,2,3,4,5,6,7,8])
# array_right_rotation(arr_to_work)
array_right_rotate_reversal_algorithm(arr_to_work, 2)
print(arr_to_work.tolist())