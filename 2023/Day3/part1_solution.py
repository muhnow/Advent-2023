file  = open('input.txt', 'r')

lines = file.readlines()

topRow = ''
currentRow = ''
bottomRow = ''

partNumbers = []

def isSymbol(strToCheck: str) -> bool:
    return strToCheck != '.' and (not strToCheck.isdigit()) and strToCheck != ''

def checkLeftAndRight(colIndex: int, strToCheck: str) -> bool: 
    symbolIsAdjacent: bool = False
    
    if colIndex > 0:
            # Check top left
            symbolToCheck = strToCheck[colIndex - 1]
            symbolIsAdjacent |= isSymbol(symbolToCheck)

    if colIndex < len(strToCheck) - 1:
        # Check top right
        symbolToCheck = strToCheck[colIndex + 1]
        symbolIsAdjacent |= isSymbol(symbolToCheck)

    return symbolIsAdjacent
    

def checkSurroundingsForSymbol(char: str, colIndex: int, currentString: str, topString: str, bottomString: str):
    # Need to check left, right, top, bottom, top left, top right, bottom left, bottom right
    symbolIsAdjacent = False

    if topString != '':
        # Check above
        symbolToCheck = topString[colIndex]
        symbolIsAdjacent |= isSymbol(symbolToCheck)

        symbolIsAdjacent |= checkLeftAndRight(colIndex, topString)

    if bottomString != '':
        # Check below
        symbolToCheck = bottomString[colIndex]
        symbolIsAdjacent |= isSymbol(symbolToCheck)

        symbolIsAdjacent |= checkLeftAndRight(colIndex, bottomString)

    symbolIsAdjacent |= checkLeftAndRight(colIndex, currentString)
            
    return symbolIsAdjacent


for rowIndex, line in enumerate(lines):
    if rowIndex != 0:
        topRow = lines[rowIndex - 1]
    
    if rowIndex != (len(lines) - 1):
        bottomRow = lines[rowIndex + 1]
    
    trackedNumber = ''
    isValidPartNumber = False

    for colIndex, x in enumerate(line):
        if (x.isdigit()):
            trackedNumber += x

            isValidPartNumber |= checkSurroundingsForSymbol(x, colIndex, line.strip(), topRow.strip(), bottomRow.strip())
        else:
            if isValidPartNumber:
                partNumbers.append(int(trackedNumber))

            trackedNumber = ''
            isValidPartNumber = False

    topRow = ''
    bottomRow = ''

print(sum(partNumbers))