import re
import math

# Read the input file
with open("input.txt", "r") as f:
    lines = f.read().splitlines()

# Initialize lists to store seed and map information
seeds = []
mapRanges = []

# Parse seed information from the first line of the input
seeds = list(map(int, re.findall(r'[\d]+', lines[0])))

# Remove unnecessary lines from the input
lines = lines[3:]

# Initialize variables for map processing
tempRange = []

# Iterate through the lines to parse map information
for x in lines:
    # New type of map starts
    if re.search(r'map', x):
        mapRanges.append(tempRange)
        tempRange = []
    else:
        if len(x) > 0:
            tempRange.append(list(map(int, re.findall(r'[\d]+', x))))

# Append the last tempRange to mapRanges
mapRanges.append(tempRange)

# Initialize a list to store seed locations after map processing
seedLocations = []

# Map checking for each seed
for x in seeds:
    currentMap = x
    for i in mapRanges:
        print(fr'{currentMap} maps to ', end='')
        for j in i:
            if j[1] <= currentMap < j[1] + j[2]:
                currentMap = j[0] + (currentMap - j[1])
                break
        print(fr'{currentMap}')
    
    # Append the final location of the seed to seedLocations
    seedLocations.append(currentMap)

# Print the minimum seed location
print(min(seedLocations))
