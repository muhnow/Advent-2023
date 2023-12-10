import re

file = open('sample_input.txt', 'r')

lines = file.readlines()

seedToSoilMaps = []
soilToFertilizerMaps = []
fertilizerToWaterMaps = []
waterToLightMaps = []
lightToTemperatureMaps = []
temperatureToHumidityMaps = []
humidityToLocationMaps = []


mapsToBuild = {}
maps = []

totalLines = len(lines)

for index, line in enumerate(lines):
    lineNumbers = []

    if ('seeds:' in line):
        seedNumbers = [int(x) for x in line[line.index(':') + 1:-1].strip().split(' ')]

    if re.match('\d+', line):
        lineNumbers = [int(x.strip()) for x in line.split(' ') if x.strip().isdigit()]

    if (len(lineNumbers) > 0):
        map = {}

        destinationStart = lineNumbers[0]
        sourceStart = lineNumbers[1]
        range = lineNumbers[2]

        map['sourceStart'] = sourceStart

        if range == 0:
            map['sourceEnd'] = sourceStart
        else:
            map['sourceEnd'] = (sourceStart + range) - 1

        map['sourceEnd'] = sourceStart + range
        map['destinationStart'] = destinationStart

        maps.append(map)

    if ('soil-to-fertilizer map' in line):
        seedToSoilMaps = maps.copy()
        maps = []
    
    if ('fertilizer-to-water' in line):
        fertilizerToWaterMaps = maps.copy()
        maps = []

    if ('water-to-light' in line):
        waterToLightMaps = maps.copy()
        maps = []
    
    if ('light-to-temperature' in line):
        lightToTemperatureMaps = maps.copy()
        maps = []
    
    if ('temperature-to-humidity' in line):
        temperatureToHumidityMaps = maps.copy()
        maps = []
    
    if ('humidity-to-location' in line):
        humidityToLocationMaps = maps.copy()
        maps = []



def findLocation(sourceNumber: int, maps: list, layer: int) -> int:
    matchingMaps = [x for x in maps if sourceNumber >= x['sourceStart'] and sourceNumber <= x['sourceEnd']]

    location = sourceNumber

    print(sourceNumber)
    print(matchingMaps)

    if (len(matchingMaps) > 0):
        map = matchingMaps[0]

        distanceFromStart = sourceNumber - map['sourceStart']

        location = map['destinationStart'] + distanceFromStart
    
    layer += 1

    match layer:
        case 1:
            return findLocation(location, soilToFertilizerMaps, layer)
        case 2: 
            return findLocation(location, fertilizerToWaterMaps, layer)
        case 3:
            return findLocation(location, waterToLightMaps, layer)
        case 4:
            return findLocation(location, lightToTemperatureMaps, layer)
        case 5:
            return findLocation(location, temperatureToHumidityMaps, layer)
        case 6:
            return findLocation(location, humidityToLocationMaps, layer)
        case _:
            return location


seedToLocationMap = {}

print(seedNumbers)


for seed in seedNumbers:
    seedToLocationMap[seed] = findLocation(seed, seedToSoilMaps, 0)

    print(seedToLocationMap[seed])




for x in seedToLocationMap:
    print('seed ' + str(x) + ' | location ' + str(seedToLocationMap[x]))
# print(seedToLocationMap)

smallestLocation = seedToLocationMap[min(seedToLocationMap, key=seedToLocationMap.get)]



print(smallestLocation)

# print(seedToSoilMaps)
# print(fertilizerToWaterMaps)