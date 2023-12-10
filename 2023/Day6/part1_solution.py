file = open('input.txt', 'r')

lines = file.readlines()

times = [int(x.strip()) for x in lines[0].split(' ') if x.strip().isdigit()]
distances = [int(x.strip()) for x in lines[1].split(' ') if x.strip().isdigit()]


totalWaysToWin = 1

for index, time in enumerate(times):
    recordDistance = distances[index]

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