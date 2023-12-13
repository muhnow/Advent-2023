file = open('input.txt', 'r')

lines = file.readlines()

hands = [x.strip() for x in lines]

cardRanks = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

handRanks = {}

handBids = {}

for hand in hands:
    handInfo = hand.split(' ')
    cards = handInfo[0]
    bidAmount = handInfo[1]
    handRank = 0
    pairs = []

    handBids[cards] = int(bidAmount)

    for index, card in enumerate(cards):
        count = cards.count(card)

        if count > 0 and not any(card in cardKey for cardKey in pairs):
            pairs.append({
                card: count
            })

            match count:
                case 2:
                    handRank += 1
                case 3:
                    handRank += 3
                case 4:
                    handRank += 5
                case 5:
                    handRank += 6

    handRanks[cards] = handRank

# Returns true if inner hand ranks higher than the outer hand 
def compareHands(innerHand: str, outerHand: str) -> bool:
    for index, outerCard in enumerate(outerHand):
        innerCard = innerHand[index]

        innerRank = cardRanks[innerCard]
        outerRank = cardRanks[outerCard]

        if innerRank == outerRank:
            continue
        else:
            return innerRank > outerRank
        


def sortHands(hands: list) -> list:
    for outerIndex, outerHand in enumerate(hands):
        innerIndex = outerIndex - 1

        for innerHand in reversed(hands[:outerIndex]):
            innerHandIsHigherRank = compareHands(innerHand, outerHand)

            # Swap the two hands you're comparing
            if innerHandIsHigherRank:
                temp = hands[innerIndex]
                hands[innerIndex] = outerHand
                hands[innerIndex + 1] = temp
            else:
                break

            innerIndex -= 1

    return hands


assert compareHands('KK677', 'KTJJT') == True
assert compareHands('T55J5', 'QQQJA') == False
assert compareHands('TTJJJ', 'JJKKK') == False

handsInOrder = []

for rank in range(0, 7):
    handsWithRank = [hand for hand, handRank in handRanks.items() if handRank == rank]

    if len(handsWithRank) == 0:
        continue

    if len(handsWithRank) == 1:
        handsInOrder += handsWithRank

    if len(handsWithRank) > 1:
        sortedHands = sortHands(handsWithRank)
        handsInOrder += sortedHands 

totalWinnings = 0 

for index, hand in enumerate(handsInOrder):
    totalWinnings += (handBids[hand] * (index + 1))



print(totalWinnings)