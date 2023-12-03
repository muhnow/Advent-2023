import re
from functools import reduce

file  = open('input.txt', 'r')

lines = file.readlines()

total = 0

for line in lines:
    digits = [x for x in line if x.isdigit()]

    if (len(digits) > 0):
        combinedDigits = digits[0] + digits[-1]

        total += int(combinedDigits)


print('Part 1 Answer: ' + str(total))

# ---------------------------------------------------

digitMap = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}

total = 0

def findOccurrences(substr, str):
    matches = re.finditer(substr, str)

    return reduce(lambda x, y: x + [y.start()], matches, [])

def combineMinAndMaxOccurrence(occurrenceMap):
    minDigitMap = {}
    maxDigitMap = {}

    for occurrenceKey in occurrenceMap:
        minDigitMap[occurrenceKey] = min(occurrenceMap[occurrenceKey])
        maxDigitMap[occurrenceKey] = max(occurrenceMap[occurrenceKey])

    minValue = digitMap[min(minDigitMap, key=minDigitMap.get)]
    maxValue = digitMap[max(maxDigitMap, key=maxDigitMap.get)]

    return minValue + maxValue


for line in lines:
    digitMatches = {}

    for digit in digitMap.keys():
        digitOccurrences = findOccurrences(digit, line)

        if (len(digitOccurrences) > 0):
            digitMatches[digit] = digitOccurrences

    calibrationValue = combineMinAndMaxOccurrence(digitMatches)

    total += int(calibrationValue)

print('Part 2 Answer: ' + str(total))