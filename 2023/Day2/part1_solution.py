import re

file  = open('input.txt', 'r')

lines = file.readlines()

validGame = {
    'red': 12,
    'green': 13,
    'blue': 14
}

gameCount = 0
    
for line in lines:
    gameNumber = re.findall('[0-9]+(?=:)', line)[0]

    reveals = line[line.index(':') + 1:].split(';')

    gameIsValid = True
        
    for reveal in reveals:
        greenMatch = re.findall('\d+(?= green)', reveal)
        blueMatch = re.findall('\d+(?= blue)', reveal)
        redMatch = re.findall('\d+(?= red)', reveal)
    
        greenCount = int(greenMatch[0]) if len(greenMatch) > 0 else 0
        redCount = int(redMatch[0]) if len(redMatch) > 0 else 0
        blueCount = int(blueMatch[0]) if len(blueMatch) > 0 else 0
        
        gameIsValid = gameIsValid and ((greenCount <= validGame['green']) and (blueCount <= validGame['blue']) and (redCount <= validGame['red']))

        if not gameIsValid: 
            break
        
    if gameIsValid:
        gameCount += int(gameNumber)

print(gameCount)