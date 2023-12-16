import re

file = open('input.txt', 'r')

lines = file.readlines()

maps = {}

directions = ''

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

steps = 0
endReached = False
nextDirection = 'AAA'

while not endReached:
    for direction in directions:
        steps += 1
        matchingMap = maps[nextDirection]

        if direction == 'L':
            nextDirection = matchingMap['left']
        
        if direction == 'R':
            nextDirection = matchingMap['right']

        if nextDirection == 'ZZZ':
            print('finished reached')
            endReached = True
            break


print(steps)