import re
from multiprocessing import Pool as ThreadPool
import threading
import time

def work(line):
    result = line.ProcessTheJunk()
    return result 

class LineData:
    def __init__(self, line):



        parts = line.split(" ")
        tempReques = [int(i) for i in parts[1].split(",")]
        self.reqs = []
        self.reqs.extend(tempReques)
        self.reqs.extend(tempReques)
        self.reqs.extend(tempReques)
        self.reqs.extend(tempReques)
        self.reqs.extend(tempReques)
        self.count = 0
        self.totalHash = 0 
        self.maxHash = 0
        self.total = 0 

                    
        self.reqsSet = set(self.reqs)

        for i in self.reqs:
            self.total += i
            if i > self.maxHash:
                self.maxHash = i
                self.countMaxHash = 1
            elif (i == self.maxHash):
                self.countMaxHash += 1
            self.totalHash += i

        self.line = parts[0] + "?" + parts[0] + "?" + parts[0] + "?" + parts[0] + "?" + parts[0]
        print(self.line)
        
    def ProcessTheJunk(self):
        # global compteted
        # global lenLines
        tempLines = [self.line]
        tempIndex = 0
        while(len(tempLines) > 0):
            lineOps = tempLines.pop()
            if (tempIndex %1000000 == 0):
                print(self.line)
                print(lineOps)
                print(self.reqs)
                print(self.reqsSet)
                print(self.count)
            questions = lineOps.count("?")
            if (questions == 0):
                splitage = [x for x in re.split("\.+", lineOps) if x]
                # print(splitage)
                viable = True
                if len(self.reqs) == len(splitage):
                    for i in range(len(self.reqs)):
                        if (self.reqs[i] != len(splitage[i])):
                            viable = False
                            break
                else:
                    viable = False
                
                if (viable):
                    self.count += 1
                    # print(self.count)
            else:
                matchers = re.findall("[#\?]{" + str(self.maxHash) + ",}", lineOps)
                
                
                valid = True
                if matchers == None:
                    matchers = []

                if valid and len(matchers) == 0:
                    valid = False             
                
                if valid:
                    maxLength = re.search("#{" + str(self.maxHash+1) + ",}", lineOps)
                    if maxLength != None:
                        valid = False
                    
                if valid:
                    dots = lineOps.count(".")
                    hashes = lineOps.count("#")
                    if (hashes > self.totalHash or questions + hashes < self.totalHash or dots + questions < len(self.reqs)-1):
                        valid = False

                if valid:
                    matchesForInvalid = re.findall("\.#+\.", lineOps)
                    for i in matchesForInvalid:
                        if len(i)-2 not in self.reqsSet:
                            valid = False
                            break
                
                if valid:
                    matchersLong = re.findall("[#\?]{" + str((self.maxHash*2)+1) + ",}", lineOps)
                    if matchersLong == None:
                        matchersLong = []
                    if not (len(matchersLong) > 1 or len(matchers) >= self.countMaxHash or len(matchers[-1]) > ((self.countMaxHash-len(matchers)) * (self.maxHash+1))-1):
                        valid = False
                    
                if valid :
                    
                    if (self.total / len(self.reqs) > 1.5 ):
                        tempStringAhh = lineOps.split("?")[0]
                        elements = [x for x in re.split("\.+", tempStringAhh) if x]
                        # print(lineOps)
                        # print(self.reqs)
                        # print(elements)
                        for ele in range(len(elements)-1):
                            
                            if len(elements[ele]) != self.reqs[ele]:
                                # print(elements[ele])
                                # print(self.reqs[ele])
                                valid = False
                                break
                if valid:
                    
                    tempLines.append(lineOps.replace("?", "#", 1))    
                    tempLines.append(lineOps.replace("?", ".", 1))    
            tempIndex += 1
        # compteted += 1
        print("Done: " + str(self.count))
        # print(str(compteted) + "/" + str(lenLines))
                
        return self.count
        # print(self.reqs)


def MainGuiLoop():
    global counterCount
    while True:
        time.sleep(10)
        print("Completed: " + str(counterCount))

def readFile(string):
    global lenLines
    global compteted
    global counterCount
    global i 
    i = 0
    lines = []
    counterCount = 0

    lenLines = 0
    compteted = 0

    pool = ThreadPool(16)
    fs  = open(string)
    for line in fs:
        lenLines += 1
        lines.append(LineData(line.strip()))
        # lines[-1].ProcessTheJunk()

    outputErr = pool.map_async(work, lines, chunksize=1)

    while not outputErr.ready():
        print("Number Left: " + str(outputErr._number_left) + " --------------------------------------------------------------------------------------------")
        time.sleep(60)

    sum = 0
    for line in outputErr.get():
        sum += line
    print(sum)

if __name__ == "__main__":
    readFile("./AOC23/day12Input.txt")