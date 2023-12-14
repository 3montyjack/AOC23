import math
stars = []
class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def AddBasedOnLines(self, xLines, yLines):
        xVal = [i for i in xLines if i <= self.x]
        yVal = [i for i in yLines if i <= self.y]
        self.x += len(xVal)* 999999
        self.y += len(yVal)* 999999
    def __repr__(self):
        return "[ " + str(self.x) + ", " + str(self.y) + " ]"
        
            
lines = []
xLines = []
yLines = []
def makeMap():
    for line in open("./AOC23/day11Input.txt"):
        lines.append(line.strip())
    y = 0
    for line in lines:
        x = 0
        for char in line:
            if char == "#":
                stars.append(Star(x,y))
            x += 1
        y += 1
    
    for y in range(len(lines)):
        if "#" not in lines[y]:
            yLines.append(y)
        
    for x in range(len(lines[0])):
        empty = True
        for y in range(len(lines)):
            if lines[y][x] == "#":
                empty = False
                break
        if empty:
            xLines.append(x)

def ExpandToHeadDeath():
    yLines.reverse()
    xLines.reverse()

    for i in stars:
        i.AddBasedOnLines(xLines, yLines)

def CalculateAllManhattanDistances():
    sum = 0
    for i in range(len(stars)):
        for j in range(i+1, len(stars)):
            sum += abs(stars[i].x - stars[j].x) + abs(stars[i].y - stars[j].y)
    print(sum)
    print(xLines)
    print(yLines)

makeMap()
print(stars)
ExpandToHeadDeath()
print(stars)
CalculateAllManhattanDistances()