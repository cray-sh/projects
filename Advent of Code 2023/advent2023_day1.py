# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:03:39 2023

@author: cray-sh
"""
#%% PART 1 - Parse thru the lines in input.txt and add them together for the whole file
#examples:
'''
1abc2                            -> 12
pqr3stu8vwx                      -> 38
a1b2c3d4e5f                      -> 15 (use first and last digit found)
treb7uchet                       -> 77 (double if only one digit)
tsgbzmgbonethreedrqzbhxjkvcnm3   -> 33 (do not convert words to digits)
''' 
#Reads file into a list whilst stripping the newline escape
path = "C:/Users/ADP55/Desktop/input.txt"
with open(path) as f:
    lines_of_file = []
    for lines in f.readlines():
        lines_of_file.append(lines.rstrip('\n'))
lines_of_file

answer = 0
#This chunk will look through the line for digits, keep them left to right and then use first on left
#and first on right to combine for a number and then add that to answer
for lines in lines_of_file:
    number = ''
    for letters in lines:
        if letters.isnumeric():
            number = number + letters
    if len(number) == 1:
        answer = answer + int(2*number)
    else:
        new_number = number[0] + number[-1]
        answer = answer + int(new_number)

answer

#%% PART 2 - Now Convert those words to their digit equivilant and repeat!
#examples:
'''
1abc2                            -> 12
pqr3stu8vwx                      -> 38
a1b2c3d4e5f                      -> 15 (use first and last digit found)
treb7uchet                       -> 77 (double if only one digit)
tsgbzmgbonethreedrqzbhxjkvcnm3   -> 13 (convert words to digits)
''' 

diag_list = []


path = "C:/Users/ADP55/Desktop/input.txt"
with open(path) as f:
    lines_of_file = []
    for lines in f.readlines():
        lines_of_file.append(lines.rstrip('\n'))
lines_of_file

answer = 0

#I'm thinking of first converting the words to digits on each line... hm...
dict_of_numb = {'one':1,
                'two':2,
                'three':3,
                'four':4,
                'five':5,
                'six':6,
                'seven':7,
                'eight':8,
                'nine':9}

for lines in lines_of_file:
    lines = lines.lower()
    temp = ''
    for letter in lines:
        temp = temp + letter
        
        for key in dict_of_numb.keys():
            if key in temp:
                temp = temp.replace(key, str(dict_of_numb[key]))
    diag_list.append(temp)
for lines in diag_list:
    number = ''
    for letters in lines:
        if letters.isnumeric():
            number = number + letters
            
    if len(number) == 0:
        print('what the fuck')
        break 
    
    elif len(number) == 1:
        new_number = int(2*number)
        answer = answer + new_number
        print(answer, number, new_number)
        
    else:
        new_number = int(number[0] + number[-1])
        answer = answer + new_number
        print(answer, number, new_number)
#    print(new_number, number, lines)

'''                
    for letters in temp:
        if letters.isnumeric():
            number = number + letters
        if len(number) == 1:
            new_number = int(2*number)
            answer = answer + new_number
            print(new_number, number, lines)
        
        else:
            new_number = int(number[0] + number[-1])
            answer = answer + new_number
            print(new_number, number, lines)
'''    
answer


#%% Isolated testing ground of the detector - DOES NOT CONVERT 'ONE' TO 1 
#WILL ALSO DOUBLE THE DIGIT IF ONLY ONE NUMERICAL DIGIT IS FOUND

for lines in lines_of_file:
    number = ''
    for letters in lines:
        if letters.isnumeric():
            number = number + letters
    if len(number) == 1:
        answer = answer + int(2*number)
    else:
        new_number = number[0] + number[-1]
        answer = answer + int(new_number)

#%% Isolated testing for detector part 2

test_line = 'eight691seven8cxdbveightzv'

dict_of_numb = {'one':1,
                'two':2,
                'three':3,
                'four':4,
                'five':5,
                'six':6,
                'seven':7,
                'eight':8,
                'nine':9}


for key in dict_of_numb.keys():
    if key in test_line:
        test_line = test_line.replace(str(key), str(dict_of_numb[key]))
test_line
        
'''
problem = 5tg578fldlcxponefourtwonet
turns into
5tg578fldlcxp14tw1t
'''