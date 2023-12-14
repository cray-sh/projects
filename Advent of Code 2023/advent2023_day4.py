# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:53:35 2023
Advent of Code 2023 Day 4
@author: cray-sh
"""
'''
PROMPT:
As far as the Elf has been able to figure out, 
you have to figure out which of the numbers you have appear in the list of winning numbers. 
The first match makes the card worth one point and each match after the first doubles
 the point value of that card.

For example:

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and 
eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53). 

Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers! 
That means card 1 is worth 8 points 
(1 for the first match, then doubled three times for each of the three matches after the first).

Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
Card 4 has one winning number (84), so it is worth 1 point.
Card 5 has no winning numbers, so it is worth no points.
Card 6 has no winning numbers, so it is worth no points.
So, in this example, the Elf's pile of scratchcards is worth 13 points.
'''

#%% Loadma File

path = "C:/Users/ADP55/Desktop/Master Scripts/projects/Advent of Code 2023/input_day4.txt"
with open(path) as f:
    file_contents = f.readlines()
    content = [line.strip('\n') for line in file_contents]

#%% QUESTION 1.
'''
Take a seat in the large pile of colorful cards. How many points are they worth in total?
'''
new_cont = [line[10:] for line in content]

#returns the points from that game
def return_if_win(line_from_new_cont):
    win, mine = line_from_new_cont.split(sep = '|')
    
    win = win.split()
    mine = mine.split()
    
    count = 0
    
    for number in mine:
        if number in win:
            count += 1
    return what_are_my_points(count)

#this creates a dictionary that will spit out a point equivilant of the number counted
def what_are_my_points(counted_number):
    list_count = [num for num in range(100)]
    points = [0] + [2**num for num in list_count]
    dict_of_points = dict(zip(list_count, points))
    return dict_of_points[counted_number]

total = 0

for games in new_cont:
    total += return_if_win(games)
    
total

#CORRECT!

#%% QUESTION 2.
''' NEW PROMPT EXTENSION
This time, the above example goes differently:

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
Your copy of card 2 also wins one copy each of cards 3 and 4.
Your four instances of card 3 (one original and three copies) have two matching numbers,
 so you win four copies each of cards 4 and 5.
Your eight instances of card 4 (one original and seven copies) have one matching number,
 so you win eight copies of card 5.
Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers
 and win no more cards.
Your one instance of card 6 (one original) has no matching numbers 
 and wins no more cards.

Once all of the originals and copies have been processed, you end up with:
    1 instance of card 1, 4 winners
    2 instances of card 2, 2 winners   + 
    4 instances of card 3, 2 winners  + - -
    8 instances of card 4, 1 winner   + - - ) ) ) ) 
    14 instances of card 5, no winner + ) ) ) ) - - - - - - - - 
    1 instance of card 6. no winner 
    
In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards!

Process all of the original and copied scratchcards until no more scratchcards are won. Including the original set of scratchcards, how many total scratchcards do you end up with?
'''
def number_win(line_from_new_cont):
    'returns number of winners in a line of scratcer game'
    win, mine = line_from_new_cont.split(sep = '|')
    
    win = win.split()
    mine = mine.split()
    
    count = 0
    
    for number in mine:
        if number in win:
            count += 1
    return count

#creates a list as long as the new_cont list that is all 1, these represent how many copies of each game
init = [1 for num in range(len(new_cont))]

#initializing some stuff to use later
sup_list = []
i = 0
j = 0

#this creates a list of lists by adding the init value for that index and appends to superlist
while i < len(new_cont):
    sup_list.append([number_win(new_cont[i]), init[i]])
    i += 1
    

#this goes through superlist and adds the copies to each game as appropriate
while j < len(sup_list):
    if sup_list[j][0] > 0:
        for number in range(sup_list[j][0]):
            added = number + 1
            sup_list[j + added][1] += sup_list[j][1]*1
    j += 1

#%% This will output how many copies were used in the game
total = 0
for items in sup_list:
    total += items[1]

print(total)

#%% Testma 2
test_block = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

test_list = test_block.split(sep = '\n')

#I made a really dumb mistake when splicing here and made a lot of confusion for myself.
#the example only has 8 spaces between the beginning of the line and the relevant numbers
#wheras the input data set used for the problem has 10

test_cont = [line[8:] for line in test_list]

init = [1 for num in range(len(test_cont))]

#creates a list of lists containing the game in slot 1 and the number of duplicates in s

sup_list = []

i = 0

#I'm going to keep this version as it removes the confusing look of keeping it in the original format.
while i < len(test_cont):
    sup_list.append([number_win(test_cont[i]), init[i]])
    i += 1
    
    
''' 
#old method, looked confusing changed it.
while i < len(test_cont):
    sup_list.append([test_cont[i], init[i]])
    i += 1
'''
'''
[4, 1]
[2, 1]   
[2, 1]   
[1, 1]   
[0, 1]   
[0, 1]   
'''
#now it needs to convert these games into how many copies are there.
j = 0
k = 0

while j < len(sup_list):
    if sup_list[j][0] > 0:
        for number in range(sup_list[j][0]):
            added = number + 1
            sup_list[j + added][1] += sup_list[j][1]*1
    j += 1

#%%the final check for testma 2:
    
total = 0
for items in sup_list:
    total += items[1]

print(total)
assert total == 30

#%% Test graveyard
j = 0    
for game in sup_list:
    for number in range(0 , number_win(game[0])):
        sup_list[j+(number+1)][1] = sup_list[j+(number+1)][1] + (1 * sup_list[j][1])
    j += 1




j = 0    
for game in sup_list:
    if number_win(game[0]) > 0:
        for number in range(0 , number_win(game[0])):
            sup_list[j+(number+1)][1] = sup_list[j+(number+1)][1] + (1 * sup_list[j][1])
    j += 1

j = 0
for game in sup_list:
    if number_win(game[0]) > 0:
        for num in range(1, number_win(game[0])+1):
            sup_list[j+num][1] += 1*(sup_list[j][1])

for game in sup_list:
    print(number_win(game[0]), game[1])
    if number_win(game[0]) > 0:
        for number in range(1, number_win(game[0])):
         



#for number in range(1, number_win(sup_list[0][0])+1):
#    print(number)


#creates a dictionary with the info... might not be the right move
#dict_of_games = dict(zip(test_cont, zeros))

#for keys in dict_of_games.keys():
#    print(dict_of_games[keys])


#test_win, test_mine = test_cont[0].split(sep = '|')

#test_win = test_win.split()
#test_mine = test_mine.split()

