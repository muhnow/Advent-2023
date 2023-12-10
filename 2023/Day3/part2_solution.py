file  = open('input.txt', 'r')

lines = file.readlines()


topRow = ''
bottomRow = ''

for rowIndex, line in enumerate(lines):
    if rowIndex != 0:
        topRow = lines[rowIndex - 1]
    
    if rowIndex != (len(lines) - 1):
        bottomRow = lines[rowIndex + 1]

    for colIndex, x in enumerate(line):
        if x == '*':
            # find adjacent numbers in line with the *
            # find adjacent numbers above