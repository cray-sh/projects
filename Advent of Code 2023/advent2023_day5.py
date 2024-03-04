# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:19:50 2023
Advent of Code 2023 Day 5
@author: cray-sh
"""
#%% PROMPT
'''
For example:

seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert numbers
 from a source category into numbers in a destination category. 
That is, the section that starts with seed-to-soil map: describes how to convert
 a seed number (the source) to a soil number (the destination). 
This lets the gardener and his team know which soil to use with which seeds, 
 which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one by one,
 the maps describe entire ranges of numbers that can be converted. 
Each line within a map contains three numbers: the destination range start, 
 the source range start, and the range length.

Consider again the example seed-to-soil map:

50 98 2
52 50 48
The first line has a destination range start of 50, a source range start of 98, 
 and a range length of 2. This line means that the source range starts at 98 and 
 contains two values: 98 and 99. 
The destination range is the same length, but it starts at 50, so its two values are 50 and 51. 
 With this information, you know that seed number 98 corresponds to soil number 50 
 and that seed number 99 corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. 
This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. 
So, seed number 53 corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination number. 
So, seed number 10 corresponds to soil number 10.

So, the entire list of seed numbers and their corresponding soil numbers looks like this:

seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51
With this map, you can look up the soil number required for each initial seed number:

Seed number 79 corresponds to soil number 81.
Seed number 14 corresponds to soil number 14.
Seed number 55 corresponds to soil number 57.
Seed number 13 corresponds to soil number 13.
The gardener and his team want to get started as soon as possible, 
so they'd like to know the closest location that needs a seed. 
Using these maps, find the lowest location number that corresponds to any of the initial seeds. 
To do this, you'll need to convert each seed number through other categories until you can 
find its corresponding location number. 

In this example, the corresponding types are:

Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
So, the lowest location number in this example is 35.
'''
#%% Importma file
path = "C:/Users/ADP55/Desktop/Master Scripts/projects/Advent of Code 2023/input_day5.txt"
with open(path) as f:
    file_contents = f.readlines()
    content = [line.strip('\n') for line in file_contents]

#create the example maps
ex_content = '''
seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''
    
#%% Question 1. 
'''
What is the lowest location number that corresponds to any of the initial seed numbers?
'''
#separating each section from the huge read in content list
seeds = content[0][7:].split()

seed_to_soil_map = content[3:13]

soil_to_fert_map = content[15:24]

fert_to_water_map = content[26:68]

water_to_light_map = content[70:114]

light_to_temp_map = content[116:162]

temp_to_humid_map = content[164:191]

humid_to_loc_map = content[193:221]
#functions
#function created to convert them to ranges
def convert_to_range(line):
    '''Takes a line in the format of number(destination) number(source) number(length)
    and returns two ranges, the destination range and then the source range.
    Using this to convert the maps into their resp ranges'''
    dest, source, length = int(line.split()[0]), int(line.split()[1]), int(line.split()[2])
    dest_range = range(dest, dest+length)
    source_range = range(source, source+length)
    return dest_range, source_range

def convertma_value(value, converted_map):
    '''This will convert the value given into the value that is equivilant in the map given'''
    range_in_q = 5
    for line in converted_map:
        if value in line[1]:
            index = line[1].index(value)
            range_in_q = line[0]
    if range_in_q == 5:
        return(value)
    else:
        return range_in_q[index]
    
#convert maps to their ranges
seed_to_soil_map = [convert_to_range(line) for line in seed_to_soil_map]
soil_to_fert_map = [convert_to_range(line) for line in soil_to_fert_map]
fert_to_water_map = [convert_to_range(line) for line in fert_to_water_map]
water_to_light_map = [convert_to_range(line) for line in water_to_light_map]
light_to_temp_map = [convert_to_range(line) for line in light_to_temp_map]
temp_to_humid_map = [convert_to_range(line) for line in temp_to_humid_map]
humid_to_loc_map = [convert_to_range(line) for line in humid_to_loc_map]

#now we need to use convertma_value to go through each of these in a chain like...
# seed --> soil --> fert --> water --> light --> temp --> humid --> loc

def locationma(seed_value):
    '''Goes through the above chain with the seed_value given, must be seed value!'''
    soil = convertma_value(seed_value, seed_to_soil_map)
    fert = convertma_value(soil, soil_to_fert_map)
    water = convertma_value(fert, fert_to_water_map)
    light = convertma_value(water, water_to_light_map)
    temp = convertma_value(light, light_to_temp_map)
    humid = convertma_value(temp, temp_to_humid_map)
    loc = convertma_value(humid, humid_to_loc_map)
    return loc

initial_seeds = [79, 14, 55, 13]

#firrst it got 2524153621   too high
#second it got 840352400    too high
#%% Q1 testing

seed_to_soil_map[0]

def convert_to_range(line):
    '''Takes a line in the format of number(destination) number(source) number(length)
    and returns two ranges, the destination range and then the source range.
    Using this to convert the maps into their resp ranges'''
    dest, source, length = int(line.split()[0]), int(line.split()[1]), int(line.split()[2])
    dest_range = range(dest, dest+length)
    source_range = range(source, source+length)
    return dest_range, source_range

seed_to_soil_converted = [convert_to_range(line) for line in seed_to_soil_map]

def convertma_value(value, converted_map):
    '''This will convert the value given into the value that is equivilant in the map given'''
    range_in_q = 0
    for line in converted_map:
        if value in line[0]:
            index = line[0].index(value)
            range_in_q = line[1]
    if range_in_q == 0:
        return(value)
    else:
        return range_in_q[index]

def convert_to_next(line):
    '''Takes a line in the format of number(destination) number(source) number(length)'''
    dest, source, length = int(line.split()[0]), int(line.split()[1]), int(line.split()[2])
    dest_range = range(dest, dest+length)
    source_range = range(source, source+length)
    return dest_range, source_range


