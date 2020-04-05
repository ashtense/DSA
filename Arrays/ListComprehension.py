import array

arr_humans = [letter for letter in 'humans']
# print(arr_humans)

arr_even_numbers = [x for x in range(0,20) if x % 2 == 0]
# print(arr_even_numbers)

arr_nested_if_condition = [x for x in range(100) if x % 2 ==0 if x % 5 == 0]
# print(arr_nested_if_condition)

arr_if_else = ["Even" if x % 2 == 0 else "Odd" for x in range(100)]
print(arr_if_else)

# This will select sub array based on a position
arr_to_work = array.array('i', [1,2,3,4,5,6,7,8])
temp_array = [x for index, x in enumerate(arr_to_work) if 2 > index >= 0]
print(temp_array)