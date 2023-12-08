file = open('input.txt', 'r')

lines = file.readlines()

winningCardCounts = {}

for index, line in enumerate(lines):
    winningCardCounts[index + 1] = 1

for index, line in enumerate(lines):
    cardNumsStart = line.index(':') + 1
    winningNumsStart = line.index('|') + 1

    cardNumbers = set([x for x in line[cardNumsStart:winningNumsStart-1].strip().split(' ') if x.isdigit()])
    winningNumbers = set([x for x in line[winningNumsStart:-1].strip().split(' ') if x.isdigit()])

    matchingNumbers = list(cardNumbers & winningNumbers)

    numberOfMatches = len(matchingNumbers)

    if (numberOfMatches > 0):
        if ((index + 1) in winningCardCounts):
            existingCardCount = winningCardCounts[index + 1]
        else:
            existingCardCount = 1

        for y in range(0, existingCardCount):
            for x in range(index + 2, (index + 1) + numberOfMatches + 1):
                winningCardCounts[x] += 1
        
totalValue = 0

for cardNumber in winningCardCounts:
    totalValue += winningCardCounts[cardNumber]

print(totalValue)