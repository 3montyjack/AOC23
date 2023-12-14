



def readInput(string):
    sum = 0
    dictOfSeeds = []
    lines = []
    linesMap = []

    for i in open(string):
        lines.append(i.strip())

    seeds = lines[0].replace("seeds: ", "").strip().split(" ")
    startIndex = 0
    for i in range(len(lines)):
        if "map" in lines[i]:
            startIndex = i
        if lines[i] == "" and startIndex != 0:
            linesMap.append((startIndex, i))
    print(linesMap)
    print(seeds)


    for i in linesMap:
        dictOfSeeds.append(Brrrr(lines[i[0]+1:i[1]]))
    minin = -1
    for seed in range(int(len(seeds)/2)):
        print("Started Seed: " + seeds[int(seed)*2])
        maxOffset = int(seeds[int((seed*2)+1)])
        currentOffset = 0
        skippingOffset = 100000
        while currentOffset < maxOffset:
            tempValue = int(seeds[seed*2])+currentOffset
            
            # listylisty = str(tempValue)
            for dict in dictOfSeeds:
                tempValue = dict.ConvertAwesomeSause(tempValue)
                # listylisty += " -> " + str(tempValue) 
            # print(listylisty)

                
            if (minin == -1):
                minin = tempValue
            elif minin > tempValue:
                minin = tempValue
                print("New Min: " + str(minin))
            if currentOffset != 0 and (currentOffset % skippingOffset) == 0:
                print(tempValue)
                if (currentOffset + skippingOffset < maxOffset):
                    tempResult = int(seeds[seed*2])+currentOffset+skippingOffset
                    for dict in dictOfSeeds:
                        tempResult = dict.ConvertAwesomeSause(tempResult)
                    if tempResult == tempValue + skippingOffset:
                        print("Here")
                        currentOffset = currentOffset + skippingOffset
                    else:
                        currentOffset +=1
                else:
                    currentOffset +=1
            else:
                currentOffset +=1
            
    print(minin)


class Brrrr: 

    def __init__(self, lines):
        self.lines = []
        for i in lines:
            value = i.split(" ")
            # print(i)
            self.lines.append(Line(value[0], value[1], value[2]))

    def ConvertAwesomeSause(self, source):
        tempSource = -1
        for i in self.lines:
            value = i.checkIfInRange(source)
            if value != -1:
                # print(i.toString())
                if tempSource != -1:
                    print("Error " + str(value))
                tempSource = value
                return tempSource
        
        # print(source)
        return source
    
class Line:
    def __init__(self, startOfDest, startOfSource, range):
        self.startOfDest = int(startOfDest)
        self.startOfSource = int(startOfSource)
        self.range = int(range)

    def checkIfInRange(self, source):
        # print(str(self.startOfSource) + " " + str(self.range))
        # print(source)
        if (self.startOfSource <= source and (self.range + self.startOfSource) > source):
            return self.startOfDest + source - self.startOfSource
        return -1
    
    def toString(self):
        return str(self.startOfDest) + " " + str(self.startOfSource) + " " + str(self.range)

readInput("./AOC23/day5Input.txt")