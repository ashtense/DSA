def checkPangram(sentence):
    arr_ascii = []
    for index in range(ord('a'), ord('z') + 1):
        arr_ascii.append(index)
    for char in sentence.lower():
        if(char != " " and ord(char) in arr_ascii):
            arr_ascii.remove(ord(char))
    #return arr_ascii
    return ''.join(map(chr, arr_ascii))

sentence = "A quick rown fox jumps over the lay dog"
print(checkPangram(sentence))