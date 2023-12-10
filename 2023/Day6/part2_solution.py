file = open('input.txt', 'r')

lines = file.readlines()

times = [x.strip() for x in lines[0].split(' ') if x.strip().isdigit()]
distances = [x.strip() for x in lines[1].split(' ') if x.strip().isdigit()]


time = int(''.join(times))
recordDistance = int(''.join(distances))
totalWaysToWin = 1
velocity = 0
waysToWinThisRace = 0

for ms in range(1, time + 1):
    velocity += 1

    timeRemaining = time - ms

    endingDistance = timeRemaining * velocity

    if endingDistance > recordDistance:
        waysToWinThisRace += 1

totalWaysToWin *= waysToWinThisRace

print(totalWaysToWin)