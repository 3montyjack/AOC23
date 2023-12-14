import copy
maperson = []

def readFileNerd(string):


    for line in open(string):
        maperson.append([])
        for char in line.strip():
            maperson[-1].append(char)
    # for i in maperson:
    #     tempString = ""
    #     for chat in i:
    #         tempString += chat

    #     print(tempString)
    # counter = 0
    # for i in maperson:
    #     for char in i:
    #         if char == "O":
    #             counter += 1
    tempBackup = copy.deepcopy(maperson)
    for i in range(10000000):

        if i == 100:
            tempBackup = copy.deepcopy(maperson)
        elif (i > 100):
            equal = True
            for y in range(len(maperson)):
                if equal:
                    for x in range(len(maperson[0])):
                        if (maperson[y][x] != tempBackup[y][x]):
                            equal = False
            if equal:
                print(i)
            
        if i % 1000 == 0 and i != 0:
            print(i)
            # equal = True
            # for y in range(len(maperson)):
            #     if equal:
            #         for x in range(len(maperson[0])):
            #             if (maperson[y][x] != tempBackup[y][x]):
            #                 equal = False
            # if equal:
            #     break
            # else:
            #     tempBackup = copy.deepcopy(maperson)
        # North
        for x in range(len(maperson[0])):
            listOfMovable = []
            for y in reversed(range(len(maperson))):
                if maperson[y][x] == "O":
                    maperson[y][x] = "." 
                    listOfMovable.append("O")
                if maperson[y][x] == "#":
                    for i in range(len(listOfMovable)):
                        maperson[y + i + 1][x] = listOfMovable[i]
                    listOfMovable = []
            if listOfMovable != []:
                for i in range(len(listOfMovable)):
                    maperson[i][x] = listOfMovable[i]
        # tempCounter = 0
        # for i in maperson:
        #     for char in i:
        #         if char == "O":
        #             tempCounter += 1

        # if (tempCounter != counter):
        #     print("Issue with north")
        #     counter = tempCounter
        # for i in maperson:
        #     tempString = ""
        #     for chat in i:
        #         tempString += chat

        #     print(tempString)
        # print()

        # West 
        for y in range(len(maperson)):
            listOfMovable = []
            for x in reversed(range(len(maperson[y]))):
                if maperson[y][x] == "O":
                    maperson[y][x] = "." 
                    listOfMovable.append("O")
                if maperson[y][x] == "#":
                    for i in range(len(listOfMovable)):
                        maperson[y][x + i + 1] = listOfMovable[i]
                    listOfMovable = []
            if listOfMovable != []:
                for i in range(len(listOfMovable)):
                    maperson[y][i] = listOfMovable[i]
        # for i in maperson:
        #     tempString = ""
        #     for chat in i:
        #         tempString += chat

        #     print(tempString)
        # print()
        # tempCounter = 0
        # for i in maperson:
        #     for char in i:
        #         if char == "O":
        #             tempCounter += 1

        # if (tempCounter != counter):
        #     print("Issue with west")
        #     counter = tempCounter


        # South
        for x in range(len(maperson[0])):
            listOfMovable = []
            for y in range(len(maperson)):
                if maperson[y][x] == "O":
                    maperson[y][x] = "." 
                    listOfMovable.append("O")
                if maperson[y][x] == "#":
                    for i in range(len(listOfMovable)):
                        maperson[y - i - 1][x] = listOfMovable[i]
                    listOfMovable = []
            if listOfMovable != []:
                for i in range(len(listOfMovable)):
                    maperson[len(maperson) - i - 1][x] = listOfMovable[i]
        # for i in maperson:
        #     tempString = ""
        #     for chat in i:
        #         tempString += chat

        #     print(tempString)
        # print()
        # tempCounter = 0
        # for i in maperson:
        #     for char in i:
        #         if char == "O":
        #             tempCounter += 1

        # if (tempCounter != counter):
        #     print("Issue with south")
        #     counter = tempCounter

        
        # East 
        for y in range(len(maperson)):
            listOfMovable = []
            for x in range(len(maperson[y])):
                if maperson[y][x] == "O":
                    maperson[y][x] = "." 
                    listOfMovable.append("O")
                if maperson[y][x] == "#":
                    for i in range(len(listOfMovable)):
                        maperson[y][x - i - 1] = listOfMovable[i]
                    listOfMovable = []
            if listOfMovable != []:
                for i in range(len(listOfMovable)):
                    maperson[y][len(maperson[0]) - i -1] = listOfMovable[i]
        # for i in maperson:
        #     tempString = ""
        #     for chat in i:
        #         tempString += chat

        #     print(tempString)
        # print()
        # tempCounter = 0
        # for i in maperson:
        #     for char in i:
        #         if char == "O":
        #             tempCounter += 1

        # if (tempCounter != counter):
        #     print("Issue with east")
        #     counter = tempCounter

    for i in maperson:
        tempString = ""
        for chat in i:
            tempString += chat

        print(tempString)
    summerson = 0
    for y in range(len(maperson)):
        for x in range(len(maperson[y])):
            if maperson[y][x] == "O":
                summerson += len(maperson) - y
    print(summerson)

    

readFileNerd("./AOC23/day14Input.txt")