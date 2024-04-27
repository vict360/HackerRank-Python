
string = "victor"


def mutation(string, position, character):
    
    stringList= list(string)

    stringList[position] = character

    newString = ''.join(stringList)

    return newString

print(mutation(string, 1, "e"))