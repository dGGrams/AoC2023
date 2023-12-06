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
