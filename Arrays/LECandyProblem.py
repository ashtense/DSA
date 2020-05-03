""" A Little Elephant and his friends from the Zoo of Lviv like candies very much.
There are N elephants in the Zoo. The elephant with number K (1 ≤ K ≤ N) will be happy if he receives at least AK candies. There are C candies in all in the Zoo.

The Zoo staff is interested in knowing whether it is possible to make all the N elephants happy by giving each elephant at least as many candies as he wants, that is, 
the Kth elephant should receive at least AK candies. Each candy can be given to only one elephant. Print Yes if it is possible and No otherwise. """

""" The first line of the input file contains an integer T, the number of test cases. T test cases follow. Each test case consists of exactly 2 lines. 
The first line of each test case contains two space separated integers N and C, the total number of elephants and the total number of candies in the Zoo respectively. 
The second line contains N space separated integers A1, A2, ..., AN. """

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