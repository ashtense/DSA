def checkPangram(sentence):
    arrCharacters = []
    for char in sentence.lower():
        if(char != " " and char not in arrCharacters):
            arrCharacters.append(char)
    if len(arrCharacters) == 26:
        return "true"
    return "false"


sentence = "Jived fox nymph grabs quick waltz"
print(checkPangram(sentence))