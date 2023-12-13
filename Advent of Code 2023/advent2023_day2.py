# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:46:43 2023

@author: cray-sh

Day 2 Advent 2023
prompt:
The Elf would first like to know which games would have been possible if the bag contained only 
12 red cubes, 13 green cubes, and 14 blue cubes?

format of file:
Game 1: 1 green, 4 blue; 1 blue, 2 green, 1 red; 1 red, 1 green, 2 blue; 1 green, 1 red; 1 green; 1 green, 1 blue, 1 red    
     ID     found in t1            found in t2          found in t3         found in t4  fnd in t5  fnd in t6
For it to be possible, the numbers found in all the trials of that game must make sense/be <= above values
If it is possible add that ID number, at the end return the total of games that were possible.
"""

#load in the input list
path = "C:/Users/ADP55/Desktop/input_day2.txt"
with open(path) as f:
    file_contents = f.readlines()
    content = [line.rstrip('\n') for line in file_contents]
    

#%% Pieces

#for a single line in content:
test = content[0]
game_name, games = test.split(':')
game_id = int(game_name.split()[1])
list_of_games = games.split(';')

for items in list_of_games: 
    comps = items.split(',')
    print(comps)
    
    
def isitpossible(list_of_single_game, red=12, green=13, blue=14):
    flag = True
    for lines in list_of_single_game:
        lines = lines.strip()
        if 'green' in lines:
            number = lines.split()[0]
            test = green
        elif 'red' in lines:
            number = lines.split()[0]
            test = red
        elif 'blue' in lines:
            number = lines.split()[0]
            test = blue
        
        if int(number) > int(test):
            flag = False
    return flag
        
#%% Part 1: 12 red cubes, 13 green cubes, and 14 blue cubes?
#these are the number of cubes in this problem
red, green, blue = 12, 13, 14
total = 0

for line in content:
    game_name, games = line.split(':')
    game_id = int(game_name.split()[1])
    list_of_games = games.split(';')
    
    flag_to_add = True
    
    for items in list_of_games:
        a_game = items.split(',')
        if not isitpossible(a_game):
            flag_to_add = False
    if flag_to_add == True:
        total += game_id
            
        
total        

#%% Part 2: What are the fewest cubes needed per game?
'''
This part now wants you to find the least number of cubes needed per game
i.e.
Game 1: 1 green, 4 blue; 1 blue, 2 green, 1 red; 1 red, 1 green, 2 blue
will need at least 2 green cubes, 4 blue cubes, and 1 red cube to create those.
They then want you to multiply those together, so 1*2*4 = 8
So instead of adding the games id's together, only add that value together for each
'''
total = 0

for line in content:
    _, games = line.split(':')
    blue, green, red = 0, 0, 0
    for item in games.split(';'):
        for lines in item.split(','):
            lines = lines.strip()
            if 'green' in lines:
                number = int(lines.split()[0])
                if number > green:
                    green = number
            elif 'red' in lines:
                number = int(lines.split()[0])
                if number > red:
                    red = number
            elif 'blue' in lines:
                number = int(lines.split()[0])
                if number > blue:
                    blue = number
    total += red*blue*green
    
total
    

#PART 1 AND 2 ARE CORRECT AND COMPLETE
