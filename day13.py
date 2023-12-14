import math

class Maperson:
    
    def __init__(self, lines):
        # Y then X
        self.contentYX = []
        self.contentXY = []
        # print(lines)
        for y in range(len(lines)):
            self.contentYX.append([])
            
            for x in range(len(lines[y])):
                if y == 0:
                    self.contentXY.append([])
                self.contentYX[-1].append(lines[y][x])
        
        for y in range(len(self.contentYX)):
            for x in range(len(self.contentYX[y])):
                self.contentXY[x].append(self.contentYX[y][x])
            


    def findMirrorReflectionsAll(self, isX):
        index1 = []
        resultingInformation = []
        if isX:
            index1 = self.contentYX
        else:
            index1 = self.contentXY
        
        for i in range(len(index1)):
            resultingInformation.append(self.findMirrorReflections(isX, i))
        return resultingInformation

    def findMirrorReflections(self, isX, index = 0):
        resultingIndex = []
        index1 = []
        if isX:
            index1 = self.contentYX[index]
        else:
            index1 = self.contentXY[index]
        # print(index1)
        for i in range(1, int(len(index1))):
            # print(index1[:i])
            # print(index1[i-len(index1):i*2-len(index1)])
            # print(index1[len(index1) - i*2:len(index1) - i])
            # print(index1[-1*i:])
            
            if (self.verifyAtIndex(index1, i) == 0):
                resultingIndex.append(i)
                # print("Found at " + str(i))
        return resultingIndex

    def verifyAtIndex(self, array, index):
        index1 = array
        i = index
        # print(array)
        diffCount = 0

        if index < len(array)/2:

            # print("Here" + str(index) + " Lower")
            # print(index1[:i])
            first = index1[:i]
            temp = index1[i-len(index1):i*2-len(index1)].copy()
            temp.reverse()
            # print(temp)
            for i in range(len(temp)):
                if first[i] != temp[i]:
                    diffCount += 1

            return diffCount
        else:
            i = len(index1) - i
            print(index1)
            print("Here" + str(index) + " Higher")
            print(index1[len(index1) - i*2:len(index1) - i])
            print(i)
            print(index1[len(index1) - i:])
            first = index1[len(index1) - i*2:len(index1) - i]
            temp = index1[len(index1) - i:].copy()
            temp.reverse()
            # print(temp)
            for i in range(len(temp)):
                if first[i] != temp[i]:
                    diffCount += 1
            print(diffCount)
            return diffCount


    def ContinueToVerify(self, isX, indicies):
        index1 = []
        
        if isX:
            index1 = self.contentYX
        else:
            index1 = self.contentXY
        print(index1[0])
        print(indicies)
        tempIndiciesAlreadyHit = []
        for i in index1:
            for j in range(len(indicies)):
                if (indicies[j] != 0):
                    diff = self.verifyAtIndex(i, indicies[j])
                    if (diff > 1):
                        # print("Invalidated Index at: " + str(indicies[j]))
                        # tempI = i.copy()
                        # tempI.insert(indicies[j], "|")
                        # print(tempI)
                        indicies[j] = 0
                    elif diff == 1:
                        if indicies[j] in tempIndiciesAlreadyHit:
                            print("Invalidated Index at: " + str(indicies[j]))
                            # tempI = i.copy()
                            # tempI.insert(indicies[j], "|")
                            # print(tempI)
                            print(tempIndiciesAlreadyHit)
                            indicies[j] = 0
                        else:
                            tempIndiciesAlreadyHit.append(indicies[j])
            indicies = [x for x in indicies if x != 0]
        return indicies

            


mirrors = []  

def readFile(string):
    lineBuffer = []
    for line in open(string):
        stripper = line.strip()
        if stripper == '':
            mirrors.append(Maperson(lineBuffer))

            lineBuffer = []
        else:
            lineBuffer.append(stripper)
    mirrors.append(Maperson(lineBuffer))
    sum = 0

    # resultX = mirrors[0].ContinueToVerify(True, mirrors[0].findMirrorReflections(True))
    # print(resultX)
    # print("Starting Y")
    # resultY = mirrors[0].ContinueToVerify(False, mirrors[0].findMirrorReflections(False))
    # print(resultY)
    index = 0
    invalidMirrorConfig = []
    for mirror in mirrors:
        # print(mirror.findMirrorReflectionsAll(True))
        # mirror.findMirrorReflections(True)
        tempResultX = []
        tempResultY = []
        tempGarbageOBj = {}
        for i in invalidCrap:
            if i["index"] == index:
                tempGarbageOBj = i
                tempResultX = i["resultX"]
                tempResultY = i["resultY"]
                
        tempRangeX = [int(x) for x in range(1,len(mirror.contentXY)) if x not in tempResultX]
        tempRangeY = [int(x) for x in range(1,len(mirror.contentYX)) if x not in tempResultY]
        resultX = mirror.ContinueToVerify(True, tempRangeX)
        resultY = mirror.ContinueToVerify(False, tempRangeY)
        # resultX = mirror.ContinueToVerify(True, mirror.findMirrorReflections(True))
        # resultY = mirror.ContinueToVerify(False, mirror.findMirrorReflections(False))

        invalidMirrorConfig.append({"index": index, "resultX": resultX, "resultY": resultY})
        index += 1
        if (len(resultX) + len(resultY)) > 1:
            print(resultX)
            print(resultY)
            print(tempGarbageOBj)
            # raise Exception('I know Python!')
        for i in resultX:

            sum += i
        for i in resultY:
            sum += i * 100
        print(sum)
        
    # mirrors[0].findMirrorReflections(True)
    # mirrors[0].findMirrorReflections(False)

    print(invalidMirrorConfig)

invalidCrap = [{'index': 0, 'resultX': [], 'resultY': [7]}, {'index': 1, 'resultX': [5], 'resultY': []}, {'index': 2, 'resultX': [], 'resultY': [12]}, {'index': 3, 'resultX': [], 'resultY': [8]}, {'index': 4, 'resultX': [], 'resultY': [1]}, {'index': 5, 'resultX': [13], 'resultY': []}, {'index': 6, 'resultX': [1], 'resultY': []}, {'index': 7, 'resultX': [], 'resultY': [4]}, {'index': 8, 'resultX': [], 'resultY': [3]}, {'index': 9, 'resultX': [12], 'resultY': []}, {'index': 10, 'resultX': [], 'resultY': [16]}, {'index': 11, 'resultX': [], 'resultY': [2]}, {'index': 12, 'resultX': [4], 'resultY': []}, {'index': 13, 'resultX': [5], 'resultY': []}, {'index': 14, 'resultX': [1], 'resultY': []}, {'index': 15, 'resultX': [], 'resultY': [1]}, {'index': 16, 'resultX': [2], 'resultY': []}, {'index': 17, 'resultX': [], 'resultY': [3]}, {'index': 18, 'resultX': [3], 'resultY': []}, {'index': 19, 'resultX': [], 'resultY': [1]}, {'index': 20, 'resultX': [1], 'resultY': []}, {'index': 21, 'resultX': [1], 'resultY': []}, {'index': 22, 'resultX': [7], 'resultY': []}, {'index': 23, 'resultX': [6], 'resultY': []}, {'index': 24, 'resultX': [6], 'resultY': []}, {'index': 25, 'resultX': [], 'resultY': [7]}, {'index': 26, 'resultX': [14], 'resultY': []}, {'index': 27, 'resultX': [16], 'resultY': []}, {'index': 28, 'resultX': [], 'resultY': [4]}, {'index': 29, 'resultX': [], 'resultY': [13]}, {'index': 30, 'resultX': [], 'resultY': [9]}, {'index': 31, 'resultX': [], 'resultY': [10]}, {'index': 32, 'resultX': [2], 'resultY': []}, {'index': 33, 'resultX': [], 'resultY': [16]}, {'index': 34, 'resultX': [15], 'resultY': []}, {'index': 35, 'resultX': [8], 'resultY': []}, {'index': 36, 'resultX': [], 'resultY': [1]}, {'index': 37, 'resultX': [1], 'resultY': []}, {'index': 38, 'resultX': [], 'resultY': [14]}, {'index': 39, 'resultX': [12], 'resultY': []}, {'index': 40, 'resultX': [], 'resultY': [3]}, {'index': 41, 'resultX': [], 'resultY': [12]}, {'index': 42, 'resultX': [11], 'resultY': []}, {'index': 43, 'resultX': [12], 'resultY': []}, {'index': 44, 'resultX': [], 'resultY': [10]}, {'index': 45, 'resultX': [12], 'resultY': []}, {'index': 46, 'resultX': [3], 'resultY': []}, {'index': 47, 'resultX': [14], 'resultY': []}, {'index': 48, 'resultX': [], 'resultY': [8]}, {'index': 49, 'resultX': [], 'resultY': [1]}, {'index': 50, 'resultX': [14], 'resultY': []}, {'index': 51, 'resultX': [], 'resultY': [12]}, {'index': 52, 'resultX': [4], 'resultY': []}, {'index': 53, 'resultX': [], 'resultY': [14]}, {'index': 54, 'resultX': [], 'resultY': [12]}, {'index': 55, 'resultX': [], 'resultY': [11]}, {'index': 56, 'resultX': [1], 'resultY': []}, {'index': 57, 'resultX': [], 'resultY': [10]}, {'index': 58, 'resultX': [16], 'resultY': []}, {'index': 59, 'resultX': [], 'resultY': [10]}, {'index': 60, 'resultX': [1], 'resultY': []}, {'index': 61, 'resultX': [12], 'resultY': []}, {'index': 62, 'resultX': [], 'resultY': [12]}, {'index': 63, 'resultX': [], 'resultY': [1]}, {'index': 64, 'resultX': [], 'resultY': [4]}, {'index': 65, 'resultX': [], 'resultY': [3]}, {'index': 66, 'resultX': [7], 'resultY': []}, {'index': 67, 'resultX': [12], 'resultY': []}, {'index': 68, 'resultX': [], 'resultY': [10]}, {'index': 69, 'resultX': [], 'resultY': [3]}, {'index': 70, 'resultX': [], 'resultY': [3]}, {'index': 71, 'resultX': [1], 'resultY': []}, {'index': 72, 'resultX': [], 'resultY': [1]}, {'index': 73, 'resultX': [1], 'resultY': []}, {'index': 74, 'resultX': [], 'resultY': [6]}, {'index': 75, 'resultX': [16], 'resultY': []}, {'index': 76, 'resultX': [], 'resultY': [1]}, {'index': 77, 'resultX': [5], 'resultY': []}, {'index': 78, 'resultX': [], 'resultY': [5]}, {'index': 79, 'resultX': [], 'resultY': [1]}, {'index': 80, 'resultX': [2], 'resultY': []}, {'index': 81, 'resultX': [], 'resultY': [4]}, {'index': 82, 'resultX': [], 'resultY': [1]}, {'index': 83, 'resultX': [1], 'resultY': []}, {'index': 84, 'resultX': [13], 'resultY': []}, {'index': 85, 'resultX': [], 'resultY': [3]}, {'index': 86, 'resultX': [7], 'resultY': []}, {'index': 87, 'resultX': [], 'resultY': [12]}, {'index': 88, 'resultX': [12], 'resultY': []}, {'index': 89, 'resultX': [1], 'resultY': []}, {'index': 90, 'resultX': [], 'resultY': [1]}, {'index': 91, 'resultX': [], 'resultY': [10]}, {'index': 92, 'resultX': [], 'resultY': [2]}, {'index': 93, 'resultX': [], 'resultY': [9]}, {'index': 94, 'resultX': [], 'resultY': [5]}, {'index': 95, 'resultX': [6], 'resultY': []}, {'index': 96, 'resultX': [], 'resultY': [3]}, {'index': 97, 'resultX': [], 'resultY': [16]}, {'index': 98, 'resultX': [], 'resultY': [1]}, {'index': 99, 'resultX': [2], 'resultY': []}]
readFile("./AOC23/day13Input.txt")


# print(mirrors)

temp = {'index': 69, 'resultX': [], 'resultY': [3]}