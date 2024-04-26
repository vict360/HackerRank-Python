
inputText = "this is a string"


def splitAndJoin(line: str):
    text = line.split(" ")
    text = "-".join(text)
    return text

print(splitAndJoin(inputText))