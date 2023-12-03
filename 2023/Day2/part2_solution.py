import re

file  = open('input.txt', 'r')

lines = file.readlines()

validGame = {
    'red': 12,
    'green': 13,
    'blue': 14
}

totalGamePower = 0 
    
for line in lines:
    gameNumber = re.findall('[0-9]+(?=:)', line)[0]

    reveals = line[line.index(':') + 1:].split(';')
    
    maxGreen = 0
    maxBlue = 0
    maxRed = 0
        
    for reveal in reveals:
        greenMatch = re.findall('\d+(?= green)', reveal)
        blueMatch = re.findall('\d+(?= blue)', reveal)
        redMatch = re.findall('\d+(?= red)', reveal)
    
        greenCount = int(greenMatch[0]) if len(greenMatch) > 0 else 0
        redCount = int(redMatch[0]) if len(redMatch) > 0 else 0
        blueCount = int(blueMatch[0]) if len(blueMatch) > 0 else 0
        
        maxGreen = greenCount if greenCount > maxGreen else maxGreen
        maxBlue = blueCount if blueCount > maxBlue else maxBlue
        maxRed = redCount if redCount > maxRed else maxRed

    gamePower = maxGreen * maxRed * maxBlue    

    totalGamePower += gamePower

print(totalGamePower)