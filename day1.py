import re

regsp1  = re.compile("one")
regsp2  = re.compile("two")
regsp3  = re.compile("three")
regsp4  = re.compile("four")
regsp5  = re.compile("five")
regsp6  = re.compile("six")
regsp7  = re.compile("seven")
regsp8  = re.compile("eight")
regsp9  = re.compile("nine")
regsp  = re.compile("[A-Za-z]")

regsp21  = re.compile("twone")
regsp18  = re.compile("oneight")
regsp38  = re.compile("threeight")
regsp58  = re.compile("fiveight")
regsp82  = re.compile("eightwo")
regsp83  = re.compile("eighthree")
regsp98  = re.compile("nineight")

def readInput(fileName):
    file = open(fileName)
    sum = 0
    for i in file:
        out = i
        out = regsp21.sub("21", out)
        out = regsp18.sub("18", out)
        out = regsp38.sub("38", out)
        out = regsp58.sub("58", out)
        out = regsp82.sub("82", out)
        out = regsp83.sub("83", out)
        out = regsp98.sub("98", out)
        out = regsp1.sub("1", out)
        out = regsp2.sub("2", out)
        out = regsp3.sub("3", out)
        out = regsp4.sub("4", out)
        out = regsp5.sub("5", out)
        out = regsp6.sub("6", out)
        out = regsp7.sub("7", out)
        out = regsp8.sub("8", out)
        out = regsp9.sub("9", out)
        out = regsp.sub("", out)
        sum += doSomething(out.strip())
    print(sum)

    

def doSomething(string):
    print(string[0] + string[-1])
    return int(string[0] + string[-1])

readInput("./AOC23/day1Input.txt")