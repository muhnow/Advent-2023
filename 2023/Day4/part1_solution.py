file = open('input.txt', 'r')

lines = file.readlines()

totalValue = 0

for line in lines:
    cardNumsStart = line.index(':') + 1
    winningNumsStart = line.index('|') + 1

    cardNumbers = set([x for x in line[cardNumsStart:winningNumsStart-1].strip().split(' ') if x.isdigit()])
    winningNumbers = set([x for x in line[winningNumsStart:-1].strip().split(' ') if x.isdigit()])

    matchingNumbers = list(cardNumbers & winningNumbers)

    if (len(matchingNumbers) > 0):
        cardValue = 2 ** (len(matchingNumbers) - 1)

        totalValue += cardValue

print(totalValue)