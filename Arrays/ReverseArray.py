import array, math

def reverse_array(arr_incomming):
    start_position = 0
    end_position = len(arr_incomming.tolist()) - 1
    while start_position < end_position:
        temp_variable = arr_incomming[start_position]
        arr_incomming[start_position] =  arr_incomming[end_position]
        arr_incomming[end_position] = temp_variable
        start_position += 1
        end_position-=1

arr_to_work = array.array('i', [1,2,3,4,5,6,7,8])
reverse_array(arr_to_work)
print(*arr_to_work, sep=" ")