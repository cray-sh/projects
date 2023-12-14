# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:50:16 2023

@author: cray-sh

Day 3 Advent 2023
prompt:
The engine schematic (your puzzle input) consists of a visual representation of the engine. 
There are lots of numbers and symbols you don't really understand, but apparently any number 
adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. 
(Periods (.) do not count as a symbol.)    
    
format of file:
    
"""
#%% Loadma File
#load in the input list
path = "C:/Users/ADP55/Desktop/Master Scripts/projects/Advent of Code 2023/input_day3.txt"
with open(path) as f:
    file_contents = f.readlines()
    content = [line.strip('\n') for line in file_contents]
    
#%% Testing 
import numpy as np

special_vals = ['#','$','%','&','*','+','-','/','=','@']


line = []
for chars in content[0]:
    line.append(chars)

test1 = np.array(line)



'''
line = []
for chars in content[1]:
    line.append(chars)

test2 = np.array(line)

test3 = np.stack([test1, test2])
'''





#%% np array

line = []
for chars in content[0]:
    line.append(chars)
begin = np.array(line)
    
    
for line in content[1:]:
    temp_line = []
    for chars in line:
        temp_line.append(chars)
    temp_array = np.array(temp_line)
    begin = np.vstack((begin,temp_array))

#Alright right now begin is in the form of a 140 by 140 matrix containing all the elements
begin    
    
#so smoething like check the above and below situations like -1 to the index and +1 to the index
#but put in a check that if the index goes negative count that as not near a special char    
for row in begin:
    for value in row:
        print(value.index)


#%% nested lists


superline = []
for lines in content:
    segment = []
    for chars in lines:
        if chars.isnumeric():
            segment.append(int(chars))
        else:
            segment.append(chars)
    superline.append(segment)

#it is now in a list of lists, nested lists if you will        
superline

test = superline[0]
test


def checknear(SingleRowOfList):
    i = 0
    keepme = []
    while i < len(SingleRowOfList):
        if i == 0:
            if SingleRowOfList[i+1] in special_vals:
               keepme.append(SingleRowOfList[i]) 
        else:
            if SingleRowOfList[i-1] in special_vals or SingleRowOfList[i+1] in special_vals:
               keepme.append(SingleRowOfList[i])
    return keepme



#%% Part 1: The sum of all the valid




