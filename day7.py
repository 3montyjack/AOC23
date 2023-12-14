import re
types = ["5ofK", "4ofK", "Full", "3ofK", "2pair", "1pair", "High"]
orderOfCards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def readInput(string):
    sum = 0
    dictOfCards= []
    lines = []

    for i in open(string):
        itemps = i.strip().split(" ")
        cards = itemps[0]
        value = itemps[1]
        dictOfCards.append(convertCards(cards, int(value)))
    
    dictOfCards.sort()
    # print(dictOfCards)

    sum = 0
    for i in range(len(dictOfCards)):
        sum += dictOfCards[i].value * (i+1)
    print(sum)
        

def convertCards(cards:str, value:int):
    indivigual = cards
    convertingDict = {}
    card = Card(cards, value)
    while len(indivigual) != 0:
        char = indivigual[0]
        firstLen = len(indivigual)
        indivigual = re.sub(char, "",indivigual)
        secondLength = len(indivigual)
        convertingDict[char] = firstLen - secondLength
    
    maxPair = 0
    maxsecondPair = 0
    for key in convertingDict:
        if (key != 'J'):
            if convertingDict[key] >= maxPair:
                maxsecondPair = maxPair
                maxPair = convertingDict[key]
            elif convertingDict[key] > maxsecondPair:
                maxsecondPair = convertingDict[key]
    


    if (maxPair == 5):
        card.cardType = types.index("5ofK")
    elif (maxPair == 4):
        card.cardType = types.index("4ofK")
    elif (maxPair == 3):
        if (maxsecondPair == 2):
            card.cardType = types.index("Full")
        else:
            card.cardType = types.index("3ofK")
    elif (maxPair == 2):
        if (maxsecondPair == 2):
            card.cardType = types.index("2pair")
        else:
            card.cardType = types.index("1pair")
    else:
        card.cardType = types.index("High")
    if ('J' in convertingDict):
        delta = 0
        if (convertingDict['J'] == 1):
            delta = 2
            if card.cardType == types.index("High"):
                delta = 1
        if (convertingDict['J'] == 2):
            delta = 3
            if card.cardType == types.index("1pair"):
                delta = 4
        if (convertingDict['J'] == 3):
            delta = 5
        if (convertingDict['J'] == 4):
            card.cardType = types.index("5ofK")
        if (convertingDict['J'] == 5):
            card.cardType = types.index("5ofK")
        card.cardType -= delta
        if card.cardType < 0:
            card.cardType = 0

    # print(card)
    return card

class Card:
    cardType = -1
    def __init__(self, card, value):
       self.card = card
       self.value = int(value) 

    def __repr__(self):
        return self.card + " " + types[self.cardType] + " " + str(self.value)
    
    def __lt__(self, other):
        if (self.cardType != other.cardType):
            return other.cardType < self.cardType
        for i in range(len(self.card)):
            if (orderOfCards.index(self.card[i]) != orderOfCards.index(other.card[i])):
                return orderOfCards.index(other.card[i]) < orderOfCards.index(self.card[i])
        return False
readInput("./AOC23/day7Input.txt")