import array, math

def check_elephant_happiness(arr_candy_req_by_elephants, num_of_elephants, num_of_candies):
    for index, candy in enumerate(arr_candy_req_by_elephants):
        num_of_candies = num_of_candies - candy
        if num_of_candies >= 0 and index == num_of_elephants - 1:
            print("yes")
        elif num_of_candies < 0:
            print("no")


sample_space = int(input())
for test_case in range(sample_space):
    arr_case = [int(i) for i in input().split()]
    num_of_elephants = arr_case[0]
    num_of_candies = arr_case[1]
    arr_candy_req_by_elephants = [int(i) for i in input().split()]
    check_elephant_happiness(arr_candy_req_by_elephants, num_of_elephants, num_of_candies)

# num_of_elephants = 3
# num_of_candies = 8
# arr_candy_req_by_elephants = array.array('i', [4,2,1])
# check_elephant_happiness(arr_candy_req_by_elephants, num_of_elephants, num_of_candies)