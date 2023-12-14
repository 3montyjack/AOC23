import re
import math
types = ["5ofK", "4ofK", "Full", "3ofK", "2pair", "1pair", "High"]
orderOfCards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
arrOfNodes = []

def readInput(string):
    sum = 0
    lines = []

    file = open(string)
    file2 = open("./AOC23/pyOut.txt", "w")
    # file2.
    instructions = file.readline().strip()
    file.readline()
    for i in file:
        vars = i.strip().split(" = ")
        nodeName = vars[0]
        leftRight = vars[1].replace("(", "").replace(")", "").replace(" ", "").split(",")
        element = findNode(nodeName)
        
        if not element:
            element = Edge(nodeName)
            arrOfNodes.append(element)
        
        left = findNode(leftRight[0])
        if not left:
            left = Edge(leftRight[0])
            arrOfNodes.append(left)
        right = findNode(leftRight[1])
        if not right:
            right = Edge(leftRight[1])
            arrOfNodes.append(right)

        element.addNodeL(left)
        element.addNodeR(right)
    print(arrOfNodes)
    listOfCurrentNodes = findNodeA()
    listOfNodesLastZ = [0,0,0,0,0,0]
    currentNode = findNode("AAA")
    currInstruction = 0
    while not checkAllNodes(listOfCurrentNodes):
        inst = instructions[currInstruction%len(instructions)]
        if (currInstruction%(len(instructions)) == 0):
            # print(listOfCurrentNodes)
            printVal = False
            # for i in listOfNodesLastZ:
            #     if listOfNodesLastZ.count(i) > 1:
            #         printVal = True
            #         break
            # if printVal:
            file2.write(str(listOfNodesLastZ) + "\n")
            print(listOfNodesLastZ)
            
            # for i in range(len(listOfCurrentNodes)):
            #     checkForLoops(listOfCurrentNodes[i])


        for i in range(len(listOfCurrentNodes)):
            if inst == "R":
                listOfCurrentNodes[i] = listOfCurrentNodes[i].rightNode
            if inst == "L":
                listOfCurrentNodes[i] = listOfCurrentNodes[i].leftNode
            if listOfCurrentNodes[i].name[2] == 'Z':
                listOfNodesLastZ[i] = currInstruction
        currInstruction += 1
    print(currInstruction)
            

def findNode(name):
    for j in arrOfNodes:
            if j.name == name:
                return j
    return None

def findNodeA():
    listOfNodes = []
    for j in arrOfNodes:
            if j.name[2] == "A":
                listOfNodes.append(j)
    return listOfNodes

def checkAllNodes(list):
    for i in list:
        if (i.name[2] != "Z"):
            return False
    return True

def checkForLoops(list):
    count = 0
    for i in list:
        if (i.name[2] == "Z"):
            count += list.count(i) -1
    if count > 0:
        print(count)
        print(list)

class Paths:

    officalList = []
    offsetListIndex = 0


class Edge:
    leftNode = None
    rightNode = None
    name = ""
    def __init__(self,name):
        self.name = name
    
    def addNodeL(self, node):
        self.leftNode = node

    def addNodeR(self, node):
        self.rightNode = node

    def __repr__(self):
        return self.name # + " " + str(self.leftNode) + " " + str(self.rightNode)

    def __str__(self):
        return self.name

currentLocation1 = [40441]
currentLocation2 = [26037]
currentLocation3 = [39333]
currentLocation4 = [29361]
currentLocation5 = [37117]
currentLocation6 = [33793]
rate1 = 20221
rate2 = 13019
rate3 = 19667
rate4 = 14681
rate5 = 18559
rate6 = 16897
for i in range(1000000):
    currentLocation1.append(currentLocation1[-1] + rate1)
    currentLocation2.append(currentLocation2[-1] + rate2)
    currentLocation3.append(currentLocation3[-1] + rate3)
    currentLocation4.append(currentLocation4[-1] + rate4)
    currentLocation5.append(currentLocation5[-1] + rate5)
    currentLocation6.append(currentLocation6[-1] + rate6)

currentPlace = 0

currentLocation1T = currentLocation1[0]
currentLocation2T = currentLocation2[0]
currentLocation3T = currentLocation3[0]
currentLocation4T = currentLocation4[0]
currentLocation5T = currentLocation5[0]
currentLocation6T = currentLocation6[0]

same = False

while not same:
    if (currentPlace %100000000 == 0):
        print(currentPlace)
        print(currentLocation1T)
    
    currentLocation4T += rate4

    if currentLocation1T < currentLocation4T:
        currentLocation1T += rate1
    if currentLocation2T < currentLocation4T:
        currentLocation2T += rate2
    if currentLocation3T < currentLocation4T:
        currentLocation3T += rate3
    if currentLocation5T < currentLocation4T:
        currentLocation5T += rate5
    if currentLocation6T < currentLocation4T:
        currentLocation6T += rate6

    if currentLocation1T == currentLocation2T and currentLocation1T == currentLocation3T and currentLocation1T == currentLocation4T and currentLocation1T == currentLocation5T and currentLocation1T == currentLocation6T:
        same = True
    currentPlace += 1
    

print(currentLocation4T)


def bianarySearch(arr, number):
    lengthT = len(arr)
    mid = math.floor(lengthT/2)
    if (lengthT < 1 ):
        return False
    if (lengthT == 1):
        return arr[0] == number
    if (number > arr[mid]):
        return bianarySearch(arr[mid:], number)
    elif (number < arr[mid]):
        return bianarySearch(arr[:mid], number)
    elif number == arr[mid]:
        return True

# for i in currentLocation1:
#     if (currentPlace %1000 == 0):
#         print(currentPlace)
#     if bianarySearch(currentLocation2, i):
#         if bianarySearch(currentLocation3, i):
#             print("here3")
#             if bianarySearch(currentLocation4, i):
#                 print("here4")
#                 if bianarySearch(currentLocation5, i):
#                     print("here5")
#                     if bianarySearch(currentLocation6, i):
#                         print("here6")
#                         if i not in currentLocation4:
#                             print("error")
#                         print(i)
#     currentPlace += 1

# print("Here")



# readInput("./AOC23/day8Input.txt")