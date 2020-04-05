import array
array_to_work = array.array('i',[1,2,3,4,5]) # i -> Integer, d -> Double, f -> float
#to print elements of the list
print(array_to_work.tolist())
#to iterate over the array.
#for number in array_to_work:
    #print(number)
#to access an element in the list
print(array_to_work[3])
array_to_work.pop(3)
print(array_to_work.tolist())
# now there is python list also. But they take up size and not pure arrays. They even store heterogeneous data.
list_to_work=[1,2,"Hello"]
print(list_to_work)
list_to_work.pop(2)
print(list_to_work)