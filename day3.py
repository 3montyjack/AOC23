
import re

def readInput(string):
    sum = 0
    symbols = "[\*]"
    lines = []
    for i in open(string):
        lines.append([char for char in i.strip()])
    height = len(lines)
    width = len(lines[0])
    for y in range(height):
        for x in range(width):
            if re.findall(symbols,lines[y][x]):
                print(re.findall(symbols,lines[y][x]))
                num = checkSurroundingsForNumbers(lines, x, y, height, width)
                if num:
                    sum += num
    print(sum)


def checkSurroundingsForNumbers(lines, x, y, height, width):
    sum1 = 0
    sum2 = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not (i == 0 and j == 0):
                if x + i >= 0 and x + i < width:
                    if y + j >= 0 and y + j < height:
                        char = re.findall("[0-9]",lines[y+j][x+i])
                        print(str(i+x) + " " + str(j + y))
                        if char and sum1 == 0:
                           sum1 = findWholeNumber(lines, x + i, y + j, width)
                        elif char and sum2 == 0:
                           sum2 = findWholeNumber(lines, x + i, y + j, width)
                        elif char:
                            return 0

    return sum1*sum2

def findWholeNumber(lines, x, y, width):
    beforeChars = ""
    tempX = x
    while tempX > -1 and re.findall("[0-9]",lines[y][tempX]):
        beforeChars = re.findall("[0-9]",lines[y][tempX])[0] + beforeChars
        lines[y][tempX] = "."
        tempX -= 1
    tempX = x+1
    
    while tempX < width and re.findall("[0-9]",lines[y][tempX]):
        beforeChars = beforeChars + re.findall("[0-9]",lines[y][tempX])[0]
        lines[y][tempX] = "."

        tempX += 1
    
    return int(beforeChars)




readInput("./AOC23/day3Input.txt")
