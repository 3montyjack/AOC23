import sys

class MapPiece:

    def __init__(self, pipe:str):
        self.pipe = pipe
        self.xObjN = None
        self.xObjP = None
        self.yObjN = None
        self.yObjP = None
        self.hit = False
        self.x = None
        self.y = None
        self.distance = -1

        self.isInLoop = None
        self.inside = None
        self.outside = None
    
    def FindAllConnectedPipes(self):
        arr = []
        if self.xObjN:
            arr.append(self.xObjN)
        if self.xObjP:
            arr.append(self.xObjP)
        if self.yObjN:
            arr.append(self.yObjN)
        if self.yObjP:
            arr.append(self.yObjP)
        return arr
    
    def RemoveNeighborRefrences(self):
        if self.xObjN:
            self.xObjN.xObjP = None
            self.xObjN = None
        if self.xObjP:
            self.xObjP.xObjN = None
            self.xObjP = None
        if self.yObjN:
            self.yObjN.yObjP = None
            self.yObjN = None
        if self.yObjP:
            self.yObjP.yObjN = None
            self.yObjP = None

    def checkIf2NeighborsLessBy1(self):
        count = 0
        if (self.checkForGreater()):
            return False
        if self.xObjN:
           if self.xObjN.distance == self.distance -1 and self.xObjN.distance != -1 and self.distance != -1:
               count += 1
        if self.xObjP:
            if self.xObjP.distance == self.distance -1 and self.xObjP.distance != -1 and self.distance != -1:
               count += 1
        if self.yObjN:
            if self.yObjN.distance == self.distance -1 and self.yObjN.distance != -1 and self.distance != -1:
               count += 1
        if self.yObjP:
            if self.yObjP.distance == self.distance -1 and self.yObjP.distance != -1 and self.distance != -1:
               count += 1
        return count >= 2

    def checkForGreater(self):
        if self.xObjN:
           if self.xObjN.distance > self.distance and self.xObjN.distance != -1 and self.distance != -1:
               return True
        if self.xObjP:
            if self.xObjP.distance > self.distance and self.xObjP.distance != -1 and self.distance != -1:
                return True

        if self.yObjN:
            if self.yObjN.distance > self.distance and self.yObjN.distance != -1 and self.distance != -1:
                return True

        if self.yObjP:
            if self.yObjP.distance > self.distance and self.yObjP.distance != -1 and self.distance != -1:
                return True

        return False
    
    def PopulateOutsideOutwards(self, depth):
        if depth < 500:
            if self.isInLoop == None and self.inside == None and self.outside == None:
                self.outside = True
                for deltaX in [-1, 0, 1]:
                    for deltaY in [-1, 0, 1]:
                        if not (deltaX == 0 and deltaY == 0) :
                            if (isInBounds( self.x, self.y, deltaX, deltaY)):
                                map[deltaY + self.y][deltaX + self.x].PopulateOutsideOutwards(depth + 1)
    
    def SetDistance(self, distance, depth = 0):
        if depth < 500:
            if distance < self.distance or self.distance == -1:
                self.distance = distance
                if self.xObjN:
                    if self.xObjN.distance > distance + 1:
                        self.xObjN.SetDistance(distance + 1, depth + 1)
                    elif self.xObjN.distance + 1 < distance and self.xObjN.distance != -1:
                        self.SetDistance(self.xObjN.distance + 1, depth + 1)
                if self.xObjP:
                    if self.xObjP.distance > distance + 1:
                        self.xObjP.SetDistance(distance + 1, depth + 1)
                    elif self.xObjP.distance + 1 < distance and self.xObjP.distance != -1:
                        self.SetDistance(self.xObjP.distance + 1, depth + 1)
                if self.yObjN:
                    if self.yObjN.distance > distance + 1:
                        self.yObjN.SetDistance(distance + 1, depth + 1)
                    elif self.yObjN.distance + 1 < distance and self.yObjN.distance != -1:
                        self.SetDistance(self.yObjN.distance + 1, depth + 1)
                if self.yObjP:
                    if self.yObjP.distance > distance + 1:
                        self.yObjP.SetDistance(distance + 1, depth + 1)
                    elif self.yObjP.distance + 1 < distance and self.yObjP.distance != -1:
                        self.SetDistance(self.yObjP.distance + 1, depth + 1)

    def GoOtherWay(self, prevNode):
        tempItems = [x for x in [self.xObjN, self.xObjP, self.yObjN, self.yObjP] if x]
        if tempItems[0] == prevNode:
            return tempItems[1]
        else:
            return tempItems[0]



    def niceStringFromObjs(self):
        
        string = "["
        if self.xObjN:
            string += " \"" + self.xObjN.pipe + "\", "
        else:
            string += " \"None\", "
        if self.xObjP:
            string += " \"" + self.xObjP.pipe + "\", "
        else:
            string += " \"None\", "
        if self.yObjN:
            string += " \"" + self.yObjN.pipe + "\", "
        else:
            string += " \"None\", "
        if self.yObjP:
            string += " \"" + self.yObjP.pipe + "\" "
        else:
            string += " \"None\" "
        string += "]"
        return string


    def __repr__(self):
        return "[ \"" + self.pipe + "\", "+ str(self.distance) + ", " + self.niceStringFromObjs() + "]"

    def __str__(self):
        return "{ \"" + self.pipe + "\": "+ str(self.distance) + " }"

def ProcessData():
    global startingPostion

    for i in open("./AOC23/day10Input.txt"):
        map.append([])
        for letter in i.strip():
            map[-1].append(MapPiece(letter))

    for y in range(len(map)):
        for x in range(len(map[y])):
            map[y][x].x = x
            map[y][x].y = y
            if map[y][x].pipe == "|":
                if isInBounds(x,y,0, -1):
                    map[y][x].yObjN = map[y-1][x]
                if isInBounds(x,y,0, 1):
                    map[y][x].yObjP = map[y+1][x]
            if map[y][x].pipe == "-":
                if isInBounds(x,y,-1, 0):
                    map[y][x].xObjN = map[y][x-1]
                if isInBounds(x,y,1, 0):
                    map[y][x].xObjP = map[y][x+1]
            if map[y][x].pipe == "L":
                if isInBounds(x,y,0, -1):
                    map[y][x].yObjN = map[y-1][x]
                if isInBounds(x,y,1, 0):
                    map[y][x].xObjP = map[y][x+1]
            if map[y][x].pipe == "J":
                if isInBounds(x,y,0, -1):
                    map[y][x].yObjN = map[y-1][x]
                if isInBounds(x,y,-1, 0):
                    map[y][x].xObjN = map[y][x-1]
            if map[y][x].pipe == "7":
                if isInBounds(x,y,-1, 0):
                    map[y][x].xObjN = map[y][x-1]
                if isInBounds(x,y,0, 1):
                    map[y][x].yObjP = map[y+1][x]
            if map[y][x].pipe == "F":
                if isInBounds(x,y,1, 0):
                    map[y][x].xObjP = map[y][x+1]
                if isInBounds(x,y,0, 1):
                    map[y][x].yObjP = map[y+1][x]
            if map[y][x].pipe == "S":
                
                startingPostion = map[y][x]
                # print(startingPostion)
                
                if isInBounds(x,y,0, -1) and (map[y-1][x].pipe == "7" or map[y-1][x].pipe == "F" or map[y-1][x].pipe == "|"):
                    map[y][x].yObjN = map[y-1][x]
                if isInBounds(x,y,0, 1) and (map[y+1][x].pipe == "J" or map[y+1][x].pipe == "L" or map[y+1][x].pipe == "|"):
                    map[y][x].yObjP = map[y+1][x]
                if isInBounds(x,y,-1, 0) and (map[y][x-1].pipe == "F" or map[y][x-1].pipe == "L" or map[y][x-1].pipe == "-"):
                    map[y][x].xObjN = map[y][x-1]
                if isInBounds(x,y,1, 0) and (map[y][x+1].pipe == "J" or map[y][x+1].pipe == "7" or map[y][x+1].pipe == "-"):
                    map[y][x].xObjP = map[y][x+1]
            
map = []
startingPostion = None
paths = []


def isInBounds(x,y,deltaX, deltaY):
    return y + deltaY >= 0 and y + deltaY < len(map) and x + deltaX >= 0 and x + deltaX < len(map[y+deltaY])

def resetSearch():
    for i in map:
        for j in i:
            j.hit = False
            j.distance = -1

class Path:
    def __init__(self, prevPath):
        self.path = []
        for i in prevPath:
            self.path.append(i)
    
    def TryAdd(self, item:MapPiece):
        
        for i in self.path:
            if item == i:
                return False
        self.path.append(item)
        return True

    def __repr__(self):
        tempStr = "[ "
        for i in self.path:
            tempStr += str(i) + ", "
        
        tempStr =tempStr[:-2] + "]"
        return tempStr   
    def checkPathLoopThroughS(self, otherPath):
        for i in range(len(self.path)):
            if not (i == 0 or i == (len(self.path)-1)):
                if self.path[i] in otherPath.path:
                    return False
        return True
                
listOfUnfinishedPaths = []

def findLoop():
    print([startingPostion])
    print("Starting Finding Loops")
    listOfUnfinishedPaths.append(Path([startingPostion]))
    CountLoops()
    # print(map)


def CountLoops():
    while (len(listOfUnfinishedPaths) != 0):
        tempPath = listOfUnfinishedPaths.pop()
        currObject = tempPath.path[-1]
        if (currObject.hit == False):
            currObject.hit = True
            currObject.SetDistance(len(tempPath.path))
            for piece in currObject.FindAllConnectedPipes():
                tempPathN = Path(tempPath.path)
                if tempPathN.TryAdd(piece):
                    listOfUnfinishedPaths.append(tempPathN)
                else:
                    paths.append(tempPath) 
        else:
            paths.append(tempPath)
pathPairs = []
maxPath = None

def FindEqualLoops():
    global maxPath
    print("StartedFindingLoops")
    print(len(paths))
    for i in range(len(paths)):
        if (i %1000 == 0):
            print(i)
            print(len(pathPairs))
        for j in range(i+1, len(paths)):
            if paths[i].path[-1] == paths[j].path[-1] and paths[i].path[1] != paths[j].path[1]:
                # if paths[i].checkPathLoopThroughS(paths[j]):
                pathPairs.append([paths[i],paths[j]])
    # for line in map:
    #     for pipe in line:
    #         if pipe.checkIf2NeighborsLessBy1():
    #             print(pipe)
    print(pathPairs)

    runningMax = 0
    for i in pathPairs:
        tempRunningMax = 0
        tempRunningMax += ((len(i[0].path) + len(i[1].path))/2)-1
        if tempRunningMax > runningMax:
            runningMax = tempRunningMax
            maxPath = i
        # for j in i[0].path:
        #     if j.distance > runningMax:
        #         runningMax = j.distance
        # for j in i[1].path:
        #     if j.distance > runningMax:
        #         runningMax = j.distance
    print(runningMax)
    print(maxPath)
    maxPath[1].path.reverse()
    maxPath[0].path.extend(maxPath[1].path[:len(maxPath[1].path)-1])
    for line in map:
        for pipe in line:
            if pipe not in maxPath[0].path:
                pipe.RemoveNeighborRefrences()
                pipe.pipe = "."
            else:
                pipe.isInLoop = True
    deltaCounts = -1

    print(maxPath[0])
    prevCount = 0
    while(deltaCounts != 0):
        for y in range(len(map)):
            for x in range(len(map[y])):
                map[y][x].PopulateOutsideOutwards(0)
        
        count = 0
        for y in range(len(map)):
            for x in range(len(map[y])):
                if map[y][x].outside:
                    count += 1
        deltaCounts = count - prevCount
        prevCount = count
        print(count)

    tempListUnresolved = []
    prevSpot = startingPostion
    nextSpot = startingPostion.GoOtherWay(startingPostion)
    leftIsOutside = None
    while nextSpot.pipe != "S":
        for deltaX in [-1, 0, 1]:
            for deltaY in [-1, 0, 1]:
                if not (deltaX == 0 and deltaY == 0) :
                    if (isInBounds( nextSpot.x, nextSpot.y, deltaX, deltaY)):
                        if leftIsOutside == None:
                            if (map[nextSpot.y + deltaY][nextSpot.x + deltaX].isInside):
                                if (prevSpot.x < nextSpot.x ):

                            elif (map[nextSpot.y + deltaY][nextSpot.x + deltaX].isInside):



    
    

                


    

    


ProcessData()
findLoop()
FindEqualLoops()
# print(paths)
