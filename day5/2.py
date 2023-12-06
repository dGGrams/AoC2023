import re
import math

def read_input_file(file_path):
    with open(file_path, "r") as f:
        lines = f.read().splitlines()
    return lines

def parse_seed_information(seed_line):
    seeds = list(map(int, re.findall(r'[\d]+', seed_line)))
    seed_ranges = []
    for x in range(0, len(seeds), 2):
        seed_ranges.append([seeds[x], seeds[x + 1]])
    return seed_ranges

def parse_map_information(map_lines):
    map_ranges = []
    temp_range = []
    map_types = 0

    for x in map_lines:
        if re.search(r'map', x):
            map_ranges.append(temp_range)
            temp_range = []
        else:
            if len(x) > 0:
                temp_range.append(list(map(int, re.findall(r'[\d]+', x))))
    
    map_ranges.append(temp_range)
    return map_ranges

def find_lowest_location(seed_ranges, map_ranges):
    map_ranges.reverse()
    x = -1
    found = False

    while not found:
        x += 1
        current_map = x

        for i in map_ranges:
            for j in i:
                if j[0] <= current_map < j[0] + j[2]:
                    current_map = j[1] + (current_map - j[0])
                    break

        for i in seed_ranges:
            if i[0] <= current_map < i[0] + i[1]:
                found = True

    return x

def main():
    file_path = "input.txt"
    lines = read_input_file(file_path)

    seed_ranges = parse_seed_information(lines[0])
    map_ranges = parse_map_information(lines[3:])

    result = find_lowest_location(seed_ranges, map_ranges)

    print(result)

if __name__ == "__main__":
    main()
import re
import math

def read_input_file(file_path):
    # Function to read the contents of the input file and return a list of lines
    with open(file_path, "r") as f:
        lines = f.read().splitlines()
    return lines

def parse_seed_information(seed_line):
    # Function to parse seed information from a line and return a list of seed ranges
    seeds = list(map(int, re.findall(r'[\d]+', seed_line)))
    seed_ranges = []
    
    # Extracting seed ranges from the seed information
    for x in range(0, len(seeds), 2):
        seed_ranges.append([seeds[x], seeds[x + 1]])
    
    return seed_ranges

def parse_map_information(map_lines):
    # Function to parse map information and return a list of map ranges
    map_ranges = []
    temp_range = []

    # Iterating through the map lines to extract map ranges
    for x in map_lines:
        if re.search(r'map', x):
            # New type of map starts, so append the current temp_range to map_ranges
            map_ranges.append(temp_range)
            temp_range = []
        else:
            if len(x) > 0:
                # Extracting map range information and appending to temp_range
                temp_range.append(list(map(int, re.findall(r'[\d]+', x))))
    
    # Appending the last temp_range to map_ranges
    map_ranges.append(temp_range)
    return map_ranges

def find_lowest_location(seed_ranges, map_ranges):
    # Function to find the lowest location number corresponding to any of the initial seed numbers
    map_ranges.reverse()  # Reversing the map to perform a reverse lookup
    x = -1
    found = False

    while not found:
        x += 1
        current_map = x

        # Iterating through map_ranges to find the corresponding location for each seed
        for i in map_ranges:
            for j in i:
                if j[0] <= current_map < j[0] + j[2]:
                    current_map = j[1] + (current_map - j[0])
                    break

        # Checking if the current_map corresponds to any seed range
        for i in seed_ranges:
            if i[0] <= current_map < i[0] + i[1]:
                found = True

    return x

def main():
    file_path = "input.txt"
    lines = read_input_file(file_path)

    # Parsing seed information from the first line
    seed_ranges = parse_seed_information(lines[0])

    # Parsing map information from lines starting from index 3
    map_ranges = parse_map_information(lines[3:])

    # Finding the lowest location number
    result = find_lowest_location(seed_ranges, map_ranges)

    print(result)

if __name__ == "__main__":
    main()
