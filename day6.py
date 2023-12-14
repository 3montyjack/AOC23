def readInput(string):
    sum = 0
    dictOfSeeds = []
    lines = []
    linesMap = []

    for i in open(string):
        lines.append(i.strip())
    
    raceTimes = lines[0].strip().replace("Time:", "").strip().replace("  ", "").replace("  ", "").replace("  ", "").replace(" ", "").split(" ")
    raceDistance = lines[1].strip().replace("Distance:", "").strip().replace("  ", "").replace(" ", "").split(" ")

    print(raceTimes)
    print(raceDistance)

    resultingMaffs = []
    for i in range(len(raceTimes)):
        resultingMaffs.append(DoMaths(int(raceTimes[i]), int(raceDistance[i])))
    total = 1
    for i in resultingMaffs:
        total *= i
    print(total)

def DoMaths(raceTime, raceDist):
    count = 0
    for i in range(raceTime):
        remaingingTime = raceTime - i
        speed = i
        time = 1000000000000000000000
        if speed != 0:
            time = raceDist/speed
        if remaingingTime > time:
            count += 1
    return count

readInput("./AOC23/day6Input.txt")