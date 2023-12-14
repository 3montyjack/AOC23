def readInput(string):
    sum = 0
    gameIndex = {}
    for i in open(string):
        gameInfo = i.split(":")
        index = int(gameInfo[0].strip("Card "))
        tempSum = 1
        gameIndex[index] = {"items": range(index+1, index + 1 + calculateWinningAmmount(gameInfo[1])), "triggerAmmount": 0}

    for i in gameIndex:
        AddAnotherObjectAndChainIt(gameIndex, i)
    
    for i in gameIndex:
        sum += gameIndex[i]["triggerAmmount"]
    print(sum)

def AddAnotherObjectAndChainIt(dick, index):
    dick[index]["triggerAmmount"] = dick[index]["triggerAmmount"] + 1
    for i in dick[index]["items"]:
        AddAnotherObjectAndChainIt(dick, i)

def calculateWinningAmmount(gameInfoString):
    games = gameInfoString.split("|")
    winningNumbers = [int(str.strip()) for str in games[0].strip().replace("  ", " ").split(" ")]
    # print(games)
    myNumbers = [int(str.strip()) for str in games[1].strip().replace("  ", " ").split(" ")]
    winning = 0
    # print(myNumbers)
    # print(winningNumbers)
    for num in myNumbers:
        if num in winningNumbers:
            winning += 1
    # print(tempSum)
    return winning

readInput("./AOC23/day4Input.txt")