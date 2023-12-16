import re
import numpy as np

file = open('input.txt', 'r')

lines = file.readlines()

maps = {}

directions = ''
startingPoints = []

for row,line in enumerate(lines):
    if row == 0:
        directions += line.strip()
    
    if '=' in line:
        key = re.findall('\S{3}(?= =)', line)[0]
        left = re.findall('\S{3}(?=,)', line)[0]
        right = re.findall('\S{3}(?=\))', line)[0]

        maps[key] = {
            'left': left,
            'right': right
        }

        if key.endswith('A'):
            startingPoints.append(key)

steps = 0
stepFinished = False
trackedSteps = {}

for point in startingPoints:
    nextDirection = point

    while not stepFinished:
        for direction in directions:
            steps += 1

            matchingMap = maps[nextDirection]

            if direction == 'L':
                nextDirection = matchingMap['left']
            
            if direction == 'R':
                nextDirection = matchingMap['right']

            if nextDirection.endswith('Z'):
                stepFinished = True
                break
    
    trackedSteps[point] = steps
    steps = 0
    stepFinished = False
    

finalSteps = np.lcm.reduce(np.array([trackedSteps[x] for x in trackedSteps]))

print(finalSteps)
