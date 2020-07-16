#Given a string S consisting of only 1s and 0s, find the number of substrings which start and end both in 1.
#In this problem, a substring is defined as a sequence of continuous characters Si,
def check_substring(stringToTest, startingEndingChar):
    arrSubstrings = []
    arrDesiredSubstrings = []
    length = len(stringToTest)
    for index, char in enumerate(stringToTest):
        for int in range(index, length + 1):
            if index != int:
                substringToCheck = stringToTest[index:int]
                arrSubstrings.append(substringToCheck)
                # startingChar = substringToCheck[0] # If you want to check strings starting with same character.
                if substringToCheck.startswith(startingEndingChar) and substringToCheck.endswith(startingEndingChar):
                    arrDesiredSubstrings.append(substringToCheck)
    return len(arrDesiredSubstrings)

# both the algorithms have O(n*2)
def check_substring_save_space(stringToTest, startingEndingChar):
    result = 0
    length = len(stringToTest)
    for index in range(length):
        for jindex in range(index, length):
            if stringToTest[index] == stringToTest[jindex] and stringToTest[index] == startingEndingChar:
                result += 1
    return result

# stringToTest = "abcab"
stringToTest = "1111"
print(check_substring(stringToTest, '1'))
print(check_substring_save_space(stringToTest, '1'))