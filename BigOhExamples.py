# Here we code examples of different asymptotes(Big oh notation)
# To demonstrate O(1) complexity
arrToTest = [1,2,3,4,23,48,9]
if(arrToTest[0] == 1):
    print("Hello")
# To demonstrate O(n) complexity.
# In the worst case scenario this program will iterate over each element
for number in arrToTest:
    if(number == 23):
        print("We found your shirt.")
# To demonstrate O(n(square) complexity)
for number in arrToTest:
    if(number == 23):
        for secondary_number in arrToTest:
            if(secondary_number == 9):
              print("primary number: %d, secondary number: %d" % (number,secondary_number))