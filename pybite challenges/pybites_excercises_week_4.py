# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 19:24:55 2023

@author: cray-sh

Pybites challenges in python Week One: Day 23 thru Day 29
"""
#%% Day 23 Bite 68:
'''
Complete remove_punctuation which receives an input string and strips out all punctuation characters 
(!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~).

Return the resulting string. 
You can go full loop, list comprehension or maybe some nice stdlib functionality?    
'''
from string import punctuation
    
def remove_punctuation_loop(input_string):
    """Return a str with punctuation chars stripped out"""
    ret_sent = ''
    for word in input_string:
        if word not in punctuation:
            ret_sent += word
    return ret_sent
        

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    ret_sent = ''
    for word in input_string:
        if word not in punctuation:
            ret_sent += word
    return ret_sent

#%% Day 23 Bite 68: Their Solution

from string import punctuation


def remove_punctuation_theirs(input_string):
    """Return a str with punctuation chars stripped out"""
    table = str.maketrans({key: None for key in punctuation})
    return input_string.translate(table)


#%% Day 23 Bite 68: Testing Cases

import pytest

#from clean import remove_punctuation


@pytest.mark.parametrize("input_argument, expected_return", [
    ('Hello, I am Tim.', 'Hello I am Tim'),
    (';String. with. punctuation characters!',
     'String with punctuation characters'),
    ('Watch out!!!', 'Watch out'),
    ('Spaces - should - work the same, yes?',
     'Spaces  should  work the same yes'),
    ("Some other (chars) |:-^, let's delete them",
     'Some other chars  lets delete them'),
])
def test_remove_punctuation(input_argument, expected_return):
    assert remove_punctuation(input_argument) == expected_return

#%% Day 24 Bite 74: What day of the week were you born on?
'''
Complete weekday_of_birth_date which takes a date object of a birthday 
and returns the corresponding weekday string.

For example Bob and Julian's birthdays return Saturday and Monday 
(that's why Bob is meant to relax and Julian to do all the work chuckle).

For this Bite you want to look at the datetime and calendar modules. Have fun!

'''
import calendar

from datetime import date

#created a dictionary to convert from the numeric value of the week to the day of the week name
dict_of_week = {0:'Monday',1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    return dict_of_week[calendar.weekday(date.year, date.month, date.day)]

#%% Day 24 Bite 74: Their Solution
def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    # calendar is nice, but you can also use: date.strftime('%A')
    weekday = date.weekday()
    return calendar.day_name[weekday]

#%% Day 24 Bite 74: Testing Cases

from datetime import date

#from bday import weekday_of_birth_date

def test_leonardo_dicaprio_bday():
    dt = date(1974, 11, 11)
    assert weekday_of_birth_date(dt) == 'Monday'


def test_will_smith_bday():
    dt = date(1968, 9, 25)
    assert weekday_of_birth_date(dt) == 'Wednesday'


def test_robert_downey_bday():
    dt = date(1965, 4, 4)
    assert weekday_of_birth_date(dt) == 'Sunday'
    
#%% Day 25 Bite 77: New places to travel to
'''
You want to find people who have as much exposure to different cultures as yourself.

Complete the uncommon_cities helper that takes the cities you have visited (my_cities) 

and the cities the other person has visited (other_cities) 

and returns the number of cities that both sequences do NOT have in common.

So given [A B C] and [B C D] it should return 2 because only A and D are different.

You can loop through both sequences but maybe there is a more concise way to do it?

'''

def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    return len([city for city in my_cities if city not in other_cities] + [other_city for other_city in other_cities if other_city not in my_cities])

#I originally made a giant for loop, but then tried shortening it / making it more concise using
# a pair of list comprehensions, hopefully that is what they were looking for?

#Edit: Dang no it wasn't they used a set and the ^ operator for not in, see below
#    return len(set(my_cities) ^ set(other_cities))

#%% Day 25 Bite 77: Testing Cases

#from uncommon import uncommon_cities


def test_uncommon_part_overlap():
    my_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']
    other_cities = ['Paris', 'Boston', 'Sydney', 'Madrid', 'Moscow', 'Lima']
    assert uncommon_cities(my_cities, other_cities) == 8


def test_uncommon_all_same():
    my_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']
    other_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']
    assert uncommon_cities(my_cities, other_cities) == 0


def test_uncommon_all_different():
    my_cities = ['Rome', 'Paris', 'Madrid']
    other_cities = ['Chicago', 'Seville', 'Berlin']
    assert uncommon_cities(my_cities, other_cities) == 6

#%% Day 26 Bite 80: Check equality of two lists
'''    
In this Bite we compare two list objects for equality, a fundamental thing to understand in Python.

Complete the check_equality function returning the various Enum values (representing equality scores) 
according to the type of equality of the lists:

return SAME_REFERENCE if both lists reference the same object,
return SAME_ORDERED if they have the same content and order,
return SAME_UNORDERED if they have the same content unordered,
return SAME_UNORDERED_DEDUPED if they have the same unordered content and reduced to unique items,
and finally return NO_EQUALITY if none of the previous cases match.
Note that == and is are not the same in Python!

Have fun and keep calm and code in Python!    
'''

from enum import Enum
from copy import deepcopy

class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
       Use the values in the Equality Enum:
       - return SAME_REFERENCE if both lists reference the same object
       - return SAME_ORDERED if they have the same content and order
       - return SAME_UNORDERED if they have the same content unordered
       - return SAME_UNORDERED_DEDUPED if they have the same unordered content
         and reduced to unique items
       - return NO_EQUALITY if none of the previous cases match"""
    #This first section creates a counter and compares the elements in both lists, if a difference
    #is found it increments counter
    counter = 0
    
    for ele in list1:
        if ele not in list2:
            counter += 1 
    for ele in list2:
        if ele not in list1:
            counter += 1
    
    if list1 is list2 and list1 == list2:
        #return same ref if both lists ref same obj
        return Equality(4)
    
    elif list1 is not list2 and list1 == list2:
        #return same order if they have the same content and order
        return Equality(3)
    
    elif counter == 0 and len(list1) == len(list2):
        #this crazy thing creates a copy of both lists and then subtracts the one list from the other if
        #at the end the second list has any elements then there must be a duplicate and the lists are no equal
        list3 = deepcopy(list1)
        list4 = deepcopy(list2)
        for element in list3:
            if element in list4:
                list4.remove(element)
        if len(list4) == 0:
            return Equality(2)
        else:
            return Equality(0)
    
    elif counter == 0 and len(list1) != len(list2):
        #if the counter is 0 but the lists are different lengths then one must be a condensed version of other
        return Equality(1)
    
    elif counter != 0:
        #if the counter is not 0 then there is a difference and there for no equality
        return Equality(0)
    

#%% Day 26 Bite 80: Their Solution
#Although I like my complicated solution that utilizes several concepts, their solution is more elgent and
#efficient
from enum import Enum


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
       Use the values in the Equality Enum:
       - return SAME_REFERENCE if both lists reference the same object
       - return SAME_ORDERED if they have the same content and order
       - return SAME_UNORDERED if they have the same content unordered
       - return SAME_UNORDERED_DEDUPED if they have the same unordered content
         and reduced to unique items
       - return NO_EQUALITY if none of the previous cases match"""
    if list1 is list2:
        return Equality.SAME_REFERENCE

    if list1 == list2:
        return Equality.SAME_ORDERED

    if sorted(list1) == sorted(list2):
        return Equality.SAME_UNORDERED

    if set(list1) == set(list2):
        return Equality.SAME_UNORDERED_DEDUPED

    return Equality.NO_EQUALITY
#%% Day 26 Bite 80: Testing Cases
#from equality import Equality, check_equality


def test_same_reference():
    a = [1, 2, 3, 4]
    b = a
    # shallow copy (do not change original), alternatively use the copy module
    c = a[:]
    assert check_equality(a, b) == Equality.SAME_REFERENCE
    assert check_equality(a, c) != Equality.SAME_REFERENCE


def test_same_ordered():
    a = [1, 2, 3, 4]
    b = a[:]
    c = a
    assert check_equality(a, b) == Equality.SAME_ORDERED
    assert check_equality(a, c) != Equality.SAME_ORDERED  # SAME_REFERENCE


def test_same_unordered():
    a = [1, 2, 3, 4]
    b = a[::-1]
    c = b[:] + [5]
    assert check_equality(a, b) == Equality.SAME_UNORDERED
    assert check_equality(a, c) != Equality.SAME_UNORDERED

#this is the only one currently failing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def test_same_with_dup_items():
    a = [1, 2, 2, 3]
    b = [1, 2, 3, 3]
    assert check_equality(a, b) != Equality.SAME_UNORDERED


def test_same_unordered_deduped():
    a = [1, 2, 2, 3, 4]
    b = a[:] + [1, 3, 4, 4]
    c = b[:] + [5]
    assert check_equality(a, b) == Equality.SAME_UNORDERED_DEDUPED
    assert check_equality(a, c) != Equality.SAME_UNORDERED_DEDUPED


def test_not_same():
    a = [1, 2, 3]
    b = [4, 5, 6]
    assert check_equality(a, b) == Equality.NO_EQUALITY
    
#%% Day 27 Bite 83: At what time does PyBites live?
'''
Get to know pytz! pytz brings the Olson tz database into Python (docs). 

Let's see how many hours Bob and Julian have to bridge in order to deliver you PyBites. 

It differs depending on whether it's Winter or Summer in their relative hemispheres.

Complete the what_time_lives_pybites function which receives a naive / not timezone aware datetime object:

There are two kinds of date and time objects: naive and aware: 
    an aware object has sufficient knowledge of applicable algorithmic and political time adjustments,
    such as time zone and daylight saving time information, to locate itself relative to other aware objects.
    
    An aware object is used to represent a specific moment in time that is not open to interpretation.
    - docs
    
First convert the passed in naive_utc_dt to a aware datetime,
 then convert it to AUSTRALIA and SPAIN localized datetimes returning them in a tuple. 
 
 For a bit more advanced pytz Bite try Bite 73 ...

Have fun and keep coding in Python!
'''

from pytz import timezone, utc

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')

def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    #I am going to use two pieces: First localize to set up naive_utc_dt as the utc time refrenece that
    #then astimezone will use to offset them to the proper timezone
    utc_dt = utc.localize(naive_utc_dt)
    aus_loc, es_loc = utc_dt.astimezone(AUSTRALIA), utc_dt.astimezone(SPAIN)
    return aus_loc, es_loc

#%% Day 27 Bite 83: Testing Cases

from datetime import datetime

#from timezone import what_time_lives_pybites


def test_what_time_lives_pybites_spanish_summertime():
    # AUS is 8 hours ahead of ES
    naive_utc_dt = datetime(2018, 4, 27, 22, 55, 0)
    aus_dt, es_dt = what_time_lives_pybites(naive_utc_dt)

    assert aus_dt.year == 2018
    assert aus_dt.month == 4
    assert aus_dt.day == 28
    assert aus_dt.hour == 8
    assert aus_dt.minute == 55

    assert es_dt.year == 2018
    assert es_dt.month == 4
    assert es_dt.day == 28
    assert es_dt.hour == 0
    assert es_dt.minute == 55


def test_what_time_lives_pybites_spanish_wintertime():
    # AUS is 10 hours ahead of ES
    naive_utc_dt = datetime(2018, 11, 1, 14, 10, 0)
    aus_dt, es_dt = what_time_lives_pybites(naive_utc_dt)

    assert aus_dt.year == 2018
    assert aus_dt.month == 11
    assert aus_dt.day == 2
    assert aus_dt.hour == 1
    assert aus_dt.minute == 10

    assert es_dt.year == 2018
    assert es_dt.month == 11
    assert es_dt.day == 1
    assert es_dt.hour == 15
    assert es_dt.minute == 10

#%% Day 28 Bite 91: Matching multiple strings
'''
Catching up after #PyCon2018 ... 

in this Bite you do multiple string matching. 

Complete contains_only_vowels, 
         contains_any_py_chars, 
         and 
         contains_digits below. 

See more info in the docstrings and the tests. Have fun!

'''
VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    for letter in input_str:
        if letter.lower() not in VOWELS:
            return False
    return True


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    for letter in input_str:
        if letter.lower() in PYTHON:
            return True
    return False


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    for letter in input_str:
        if letter.lower().isnumeric():
            return True
    return False


#%% Day 28 Bite 91: Their Solution
import re

VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return all(c in VOWELS for c in input_str.lower())


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    # return any(c in PYTHON for c in input_str.lower())
    return re.search(rf'[{PYTHON}]', input_str.lower())


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    return re.search(r'\d+', input_str)
    
#%% Day 28 Bite 91: Testing Cases

import pytest

#from anyall import (contains_only_vowels,
#                    contains_any_py_chars,
#                    contains_digits)


@pytest.mark.parametrize("arg, expected", [
    ('aioue', True),
    ('EoUia', True),
    ('aaAiIee', True),
    ('AEIOU', True),
    ('aaeeouu', True),
    ('abcde', False),
    ('AE123', False),
    ('AiOuef', False),
])
def test_contains_only_vowels(arg, expected):
    assert bool(contains_only_vowels(arg)) is expected


@pytest.mark.parametrize("arg, expected", [
    ('Python', True),
    ('pycharm', True),
    ('PYTHON', True),
    ('teaser', True),
    ('bob', True),
    ('julian', True),
    ('yes', True),
    ('no', True),
    ('america', False),
    ('B@b', False),
    ('Jules', False),
    ('agua', False),
    ('123', False),
    ('', False),
])
def test_contains_any_py_chars(arg, expected):
    assert bool(contains_any_py_chars(arg)) is expected


@pytest.mark.parametrize("arg, expected", [
    ('yes1', True),
    ('123', True),
    ('hello2', True),
    ('up2date', True),
    ('yes', False),
    ('hello', False),
    ('', False),
])
def test_contains_digits(arg, expected):
    assert bool(contains_digits(arg)) is expected


#%% Day 29 Bite 96: Build Unix' wc program in Python
'''
In this Bite you will convert Unix' wc command into Python. 

Your function takes a file (absolute path), 
reads it in and calculates the lines/words/chars. 

It returns a string of these numbers and the filename, like as a typical wc output, for example:

# Unix command
$ wc wc.py
      22      85     771 wc.py

# your script
$ python wc.py  wc.py
22	85	771 wc.py

Don't worry about the amount of white space between the columns, you can use tabs or spaces.

Unix files add an extra newline to the end so for content Hello\nworld Unix' wc would return 12 (not 11):

$ cat hello
hello
world
$ wc hello
       2       2      12 hello
       
As this is a Beginner Bite we can save you some head aches by suggesting you to use splitlines for the line counts!

See the tests for more info. Thanks Brian for introducing us to pytest's tmp_path fixture!

Have fun and keep coding in Python!

'''
test_location = 'C:/Users/ADP55/Desktop/test_doc.txt'

def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    linema = 0
    wordma = 0 
    
#ran into a problem that was fixed in this way and a different way below in their solution
#but we need to use the file for more than one purpose, and we will need to use the contents in different ways
#this problem was solved by me by re-opening the file later (you can only read a file once!)
#they solved it by making a single content=f.read() and then using content in different ways like
# content.splitlines(), content.split() and content instead of     
    with open(file_) as f:
        charma = len(f.read())
       
    with open(file_) as f:
        contents = f.readlines()
        for line in contents:
            linema += 1 
            line_in_question = line.splitlines(keepends=True) #will spit out a line that has the \n at end
            for words in line_in_question[0].split():
                wordma += 1 
                
    return f'{linema} {wordma} {charma} {file_}'

''' This block creates an error unless you are running this as a script
if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))    
'''    

#%% Day 29 Bite 96: Their Solution

#For this one we both came to a similar solution but they fixed the reading problem I had by making f.read()
#and then using copies of it
#there way is also better because it keeps the read in information in its current state with all the esc chars

def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_) as f:
        content = f.read()
        # num_lines = len(content.split('\n'))
        # better:
        # num_lines = len(content.rstrip().split('\n'))
        # or:
        num_lines = len(content.splitlines())
        num_words = len(content.split())
        num_chars = len(content)
        numbers = f'{num_lines}\t{num_words}\t{num_chars}'
        return f'{numbers} {file_}'
    
#%% Day 29 Bite 96: Testing Cases
from urllib.request import urlretrieve

import pytest

#from wc import wc

lines = [b'Hello world',
         b'Keep calm and code in Python',
         b'Have a nice weekend']
py_file = 'https://bites-data.s3.us-east-2.amazonaws.com/driving.py'


@pytest.mark.parametrize("some_text, expected", [
    (lines[0], '1 2 11'),
    (b'\n'.join(lines[:2]), '2 8 40'),
    (b'\n'.join(lines), '3 12 60'),
])
def test_wc(some_text, expected, tmp_path):
    f = tmp_path / "some_file.txt"
    f.write_bytes(some_text)
    output = wc(f.resolve())
    # replace tabs / multiple spaces by single space
    counts = ' '.join(output.split()[:3])
    assert counts == expected
    # file with/without path allowed
    assert f.name in output


def test_wc_on_real_py_file(tmp_path):
    f = tmp_path / "driving.py"
    urlretrieve(py_file, f)
    output = wc(f.resolve())
    counts = ' '.join(output.split()[:3])
    # https://twitter.com/pybites/status/1175795375904628736
    expected = "7 29 216"  # not 8!
    assert counts == expected
    assert f.name in output    
    
    
    
