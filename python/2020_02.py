import input_02
import input_02b

def countPasswordsDict(passwordsDict):
    totalPasswords = 0
    goodPasswords = 0
    goodPasswordsList = []
    for rule in passwordsDict:
        totalPasswords += 1
        password = passwordsDict[rule]
        rangeList = getRangeList(rule)
        letter = rule[-1:]
        isGood = checkPassword(rangeList, letter, password)
        if isGood:
            goodPasswords += 1
            goodPasswordsList.append(password)
    print(f"Found {goodPasswords} good passwords out of {totalPasswords} passwords checked")


def countPasswordsList(passwordsList):
    totalPasswords = 0
    goodPasswords = 0
    for instance in passwordsList:
        totalPasswords += 1
        rule = instance[0]
        password = instance[1]
        rangeList = getRangeList(rule)
        letter = rule[-1:]
        isGood = checkPassword(rangeList, letter, password)
        if isGood:
            goodPasswords += 1
    print(f"Found {goodPasswords} good passwords out of {totalPasswords} passwords checked")


def getRangeList(ruleString):
    ruleString = ruleString[:-2]
    rangeListString = ruleString.split("-")
    return list(map(int, rangeListString))


def checkPassword(rule, x, word):
    occurances = 0
    goodPassword = False
    for character in word:
        if character == x:
            occurances += 1
    if occurances > rule[1]:
        goodPassword = False
    elif occurances < rule[0]:
        goodPassword = False
    else:
        goodPassword = True
    # print(f"{occurances} occurances of {x} in {word}. The legal range was {rule[0]} to {rule[1]}, so 'goodPassword' is {goodPassword}")
    return goodPassword


exampleInput = {
    "1-3 a": "abcde",
    "1-3 b": "cdefg",
    "2-9 c": "ccccccccc"
}
countPasswordsDict(exampleInput)
countPasswordsDict(input_02.puzzleInput)
countPasswordsList(input_02b.puzzleInput)
