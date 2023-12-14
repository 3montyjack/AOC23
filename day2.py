
def readInput(string):
    sum = 0
    for i in open(string):
        gameInfo = i.split(":")
        index = int(gameInfo[0].strip("Game "))
        tempSum = 1
        games = gameInfo[1].split(";")
        colors = {"red": 0, "blue": 0, "green": 0}
        for game in games:
            colorMarbles = game.split(",")
            for colorMarble in colorMarbles:
                colorMarbleStates = colorMarble.strip().split(" ")
                amount = int(colorMarbleStates[0])
                color = colorMarbleStates[1]
                if colors[color] < amount:
                    colors[color] = amount
        for i in colors:
            tempSum *= colors[i]
        sum += tempSum
    print(sum)


readInput("./AOC23/day2Input.txt")