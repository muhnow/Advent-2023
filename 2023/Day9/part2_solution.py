file = open('input.txt', 'r')

lines = file.readlines()

def findPredictedValue(values: list) -> int:
    nextHistory = []

    for idx, value in enumerate(values[:-1]):
        nextHistory.append(values[idx + 1] - values[idx])

    if nextHistory[-1] == 0:
        return 0

    return nextHistory[0] - findPredictedValue(nextHistory)

total = 0

for line in lines:
    history = [int(x.strip()) for x in line.split(' ')]

    total += history[0] - findPredictedValue(history)

print(total)