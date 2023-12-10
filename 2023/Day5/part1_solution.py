import re

file = open('input.txt', 'r')

lines = file.readlines()

seedToSoilMap = {}
soilToFertilizerMap = {}
fertilizerToWaterMap = {}
waterToLightMap = {}
lightToTemperatureMap = {}
temperatureToHumidityMap = {}
humidityToLocationMap = {}

mapToBuild = {}
seedNumbers = []

totalLines = len(lines)

for index, line in enumerate(lines):
    lineNumbers = []

    if ('seeds:' in line):
        seedNumbers = [int(x) for x in line[line.index(':') + 1:-1].strip().split(' ')]

    if re.match('\d+', line):
        lineNumbers = [int(x.strip()) for x in line.split(' ') if x.strip().isdigit()]
        # print(lineNumbers)

    if (len(lineNumbers) > 0):
        destinationStart = lineNumbers[0]
        sourceStart = lineNumbers[1]

        print('building map')

        for x in range(0, lineNumbers[2]):
            mapToBuild[sourceStart] = destinationStart

            sourceStart += 1
            destinationStart += 1

        print('done building map')

    print('copying map')

    if ('soil-to-fertilizer map' in line):
        seedToSoilMap = dict(mapToBuild)
        mapToBuild = {}
    
    if ('fertilizer-to-water' in line):
        fertilizerToWaterMap = dict(mapToBuild)
        mapToBuild = {}

    if ('water-to-light' in line):
        waterToLightMap = dict(mapToBuild)
        mapToBuild = {}
    
    if ('light-to-temperature' in line):
        lightToTemperatureMap = dict(mapToBuild)
        mapToBuild = {}
    
    if ('temperature-to-humidity' in line):
        temperatureToHumidityMap = dict(mapToBuild)
        mapToBuild = {}
    
    if ('humidity-to-location' in line):
        humidityToLocationMap = dict(mapToBuild)
        mapToBuild = {}

    print('finished line ' + str(index) + '/' + str(totalLines))

seedToLocationMap = {}

print(seedToSoilMap)

for seed in seedNumbers:
    soilLocation = seed if seed not in seedToSoilMap else seedToSoilMap[seed]

    print('seed: ' + str(seed) + ' at soil: ' + str(soilLocation))

    fertilizerlocation = soilLocation if soilLocation not in soilToFertilizerMap else soilToFertilizerMap[soilLocation]
    waterLocation = fertilizerlocation if fertilizerlocation not in fertilizerToWaterMap else fertilizerToWaterMap[fertilizerlocation]
    lightLocation = waterLocation if waterLocation not in waterToLightMap else waterToLightMap[waterLocation]
    temperatureLocation = lightLocation if lightLocation not in lightToTemperatureMap else lightToTemperatureMap[lightLocation]
    humidityLocation = temperatureLocation if temperatureLocation not in temperatureToHumidityMap else temperatureToHumidityMap[temperatureLocation]
    finalLocation = humidityLocation if humidityLocation not in humidityToLocationMap else humidityToLocationMap[humidityLocation]

    seedToLocationMap[seed] = finalLocation


print(min(seedToLocationMap, key=seedToLocationMap.get))