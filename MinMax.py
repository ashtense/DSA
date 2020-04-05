
def min_max_in_array(arr_to_work):
    min_number = None
    max_number = None
    for number in arr_to_work:
        if min_number == None or max_number == None:
            min_number = number
            max_number = number
        elif number < min_number:
            min_number = number
        elif number > max_number:
            max_number = number
    return [min_number, max_number]

arr_to_work = [11,2,4,8,3]
arr_result = min_max_in_array(arr_to_work)
print("Minimum from the array is: %d \nMaximum in the array is: %d" % (arr_result[0], arr_result[1]))