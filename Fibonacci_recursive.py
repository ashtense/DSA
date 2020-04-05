def fibonacci_number(number):
  if(number <= 1):
      return number
  return fibonacci_number(number -2) + fibonacci_number(number -1)

arr_fibonacci = []
for number in range(1,11):
    arr_fibonacci.append(fibonacci_number(number))
print(arr_fibonacci)