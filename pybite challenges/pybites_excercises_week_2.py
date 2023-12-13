# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 20:24:37 2023

@author: cray-sh

Pybites challenges in python Week One: Day 8 thru Day 14
"""
#%% Day 8 Bite 26: Dictionary Comprehensions are Awesome
'''
A dictionary comprehension is like a list comprehension, but it constructs a dict instead of a list. 
They are convenient to quickly operate on each (key, value) pair of a dict.
 And often in one line of code, maybe two after checking PEP8 ;)

We think they are elegant, that's why we want you to know about them!

In this Bite you are given a dict and a set. 
Write a dictionary comprehension that filters out the items in the set and returns the resulting dict,
 so if your dict is 
 {1: 'bob', 2: 'julian', 3: 'tim'}
 and your set is {2, 3},
 the resulting dict would be {1: 'bob'}.

Check out the tests for more details. Have fun!
'''


from typing import Dict, Set

DEFAULT_BITES = {
    6: "PyBites Die Hard",
    7: "Parsing dates from logs",
    9: "Palindromes",
    10: "Practice exceptions",
    11: "Enrich a class with dunder methods",
    12: "Write a user validation function",
    13: "Convert dict in namedtuple/json",
    14: "Generate a table of n sequences",
    15: "Enumerate 2 sequences",
    16: "Special PyBites date generator",
    17: "Form teams from a group of friends",
    18: "Find the most common word",
    19: "Write a simple property",
    20: "Write a context manager",
    21: "Query a nested data structure",
}
EXCLUDE_BITES = {6, 10, 16, 18, 21}


def filter_bites(bites: Dict[int, str] = DEFAULT_BITES,
                 bites_done: Set[int] = EXCLUDE_BITES) -> Dict[int, str]:
    """
    Return the bites dict with bites_done filtered out.
    The dict comprehension forme
    """
    return {a:b for (a,b) in zip(bites.keys(),bites.values()) if a not in bites_done}


def filter_bites2(bites: Dict[int, str] = DEFAULT_BITES,
                 bites_done: Set[int] = EXCLUDE_BITES) -> Dict[int, str]:
    """
    Return the bites dict with bites_done filtered out.
    The for loop forme
    """
    for num in bites_done:
        del bites[num]
    return bites
    


#%% Day 8 Bite 26: Testing Cases
#from exclude import filter_bites


def test_filter_bites_default_arguments():
    actual = filter_bites()
    expected = {
        7: "Parsing dates from logs",
        9: "Palindromes",
        11: "Enrich a class with dunder methods",
        12: "Write a user validation function",
        13: "Convert dict in namedtuple/json",
        14: "Generate a table of n sequences",
        15: "Enumerate 2 sequences",
        17: "Form teams from a group of friends",
        19: "Write a simple property",
        20: "Write a context manager",
    }
    assert actual == expected


def test_filter_bites_different_outputs():
    bites = {
        26: "Dictionary comprehensions are awesome",
        15: "Enumerate 2 sequences",
        21: "Query a nested data structure",
        105: "Slice and dice",
    }
    excluded_bites = {21, 105}
    actual = filter_bites(bites, excluded_bites)
    expected = {
        26: "Dictionary comprehensions are awesome",
        15: "Enumerate 2 sequences",
    }
    assert actual == expected
    

#%% Day 9 Bite 29: Martin's IQ Test
'''
Martin is preparing to pass an IQ test.

The most frequent task in this test is to find out which one of the given characters differs from the others. 
He observed that one char usually differs from the others in being alphanumeric or not.

Please help Martin! To check his answers, 
he needs a program to find the different one (the alphanumeric among non-alphanumerics or vice versa) 
among the given characters.

Complete get_index_different_char to meet this goal. 
It receives a chars list and returns an int index (zero-based).

Just to be clear, alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

Examples:

['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)   
'''    
    
def get_index_different_char(chars):
    '''Returns the index of the odd char out. Chars are organized by alphanumeric or not, whichever rarer return the index.'''
    #this creates two variables that old the most current char that satisfies that requirement(alphanum or not)
    
    alphanum = ''
    nonalphanum = ''
    #these are the counters, for each char found in each group add one to the counter
    
    alpha_i = 0 
    nonalpha_i = 0
    
    #next check the list given and see which of those are alnum or not, and then iterate resp counter
    
    for char in chars:
        if str(char).isalnum():
            alpha_i += 1 
            alphanum = char
        else:
            nonalpha_i += 1 
            nonalphanum = char
    #finally, whichever counter is lower return that most recent char
    
    if alpha_i < nonalpha_i:
        return chars.index(alphanum)
    else:
        return chars.index(nonalphanum)
            
#%% Day 9 Bite 29: Testing Cases
import pytest

#from wrong_char import get_index_different_char


@pytest.mark.parametrize("arg, expected", [
    (['A', 'f', '.', 'Q', 2], 2),
    (['.', '{', ' ^', '%', 'a'], 4),
    ([1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'], 1),
    (['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'], 5),
    (list(range(1, 9)) + ['}'] + list('abcde'), 8),
    ([2, '.', ',', '!'], 0),
])
def test_wrong_char(arg, expected):
    error = (f"get_index_different_char({arg}) should "
             f"return index {expected}")
    assert get_index_different_char(arg) == expected, error
    
#%% Day 10 Bite 32: Don't let mutability fool you
'''
In this Bite you are presented with a function that copies
 the given items data structure.

There is a problem though, the tests fail. Can you fix it?

This can be done in a one liner. 
If you know which module to use it will be easy,
 if not you will learn something new today.

Regardless we want you to think about Python's mutability.
 Have fun!
'''
import copy
#code from site:
items = [{'id': 1, 'name': 'laptop', 'value': 1000},
         {'id': 2, 'name': 'chair', 'value': 300},
         {'id': 3, 'name': 'book', 'value': 20}]
'''
This excerise has made me advertently fall into a classic
pitfall in programming. 

Actually its made me fall into two, but one that I have been
making and just now realized.

The first pitfall:
It's about the concept of greedy importing, typically when I
import new functions/libraries/packages I have been importing
the full package/library when in reality it is much
more effiecient and faster to import only the one you need.
example
import copy     #very greedy, imports all from copy

vs

from copy import deepcopy  #only imports what we need, shorter
                                notation too!

The second pitfall:
From dvr on stackoverflow:
This is programming 101. Remember lists are stored in heap,
with pointers to them.

So really the variable board points to the place
in heap where that array is stored, when you assign
temp (or another vaiable name to a list),
you are making a new pointer which points to the same
array in memory.

This is a concept known as shallow copyiing, we have
two different ways to combat this problem,
1. Utilizing the package copy creating a deep copy.
2. Using the code that dvr created, which is most likely the 
source or near the source of copy.

example from dvr
def deep_copy(board):
    temp = []
    for i in range(len(board)):
        row_copy = []
        for j in range(len(board[0])):
            row_copy.append(board[i][j])
        temp.append(row_copy)
    return temp
'''
def duplicate_items(items):
    new_copy = copy.deepcopy(items)
    return new_copy

#%% Day 10 Bite 32: Best Case with Avoiding those pitfalls
#takes care of the lazy importing
from copy import deepcopy

items = [{'id': 1, 'name': 'laptop', 'value': 1000},
         {'id': 2, 'name': 'chair', 'value': 300},
         {'id': 3, 'name': 'book', 'value': 20}]

def duplicate_items(items):
    return deepcopy(items)

#%% Day 10 Bite 32: Testing Cases
#we donot need the below line unless you save them as two .py
#from inventory import items, duplicate_items

def test_change_copy_only():
    items_copy = duplicate_items(items)
    assert items == items_copy

    # modify the copy
    items_copy[0]['name'] = 'macbook'
    items_copy[1]['id'] = 4
    items_copy[2]['value'] = 30


    # only copy should have been updated, check original items values
    assert items[0]['name'] == 'laptop'
    assert items[1]['id'] == 2
    assert items[2]['value'] == 20

#%% Day 11 Bite 37: Rewrite a for loop using recursion

def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    '''Uses recursion to countdown from the given number, if nothing given it will start at 10.'''
    if start > 0:
        #while start is greater than 0 print what start is and then recurse one
        print(start)
        start = countdown_recursive(start-1)
    else:
        #when it hits zero print the statement
        #I had to use print here instead of return because of how stdoutput works.
        start = 'time is up'
        print(start)

#%% Day 11 Bite 37: Testing Cases
import inspect

import pytest

#from countdown import countdown_for, countdown_recursive

expected = '''10
9
8
7
6
5
4
3
2
1
time is up
'''
expected_other_start_arg = '''13
12
11
'''
expected_other_start_arg += expected


def test_countdown_for(capfd):
    countdown_for()
    out, _ = capfd.readouterr()
    assert out == expected

# 
def test_countdown_recursive(capfd):
    countdown_recursive()
    out, _ = capfd.readouterr()
    assert out == expected

#
def test_test_countdown_recursive_different_start(capfd):
    countdown_recursive(13)
    out, _ = capfd.readouterr()
    assert out == expected_other_start_arg


def test_recursion_used():
    func = countdown_recursive
    err = f'expecting {func.__name__} twice in your answer'
    assert inspect.getsource(func).count(func.__name__) == 2, err


def test_countdown_from_zero_prints_time_is_up(capfd):
    countdown_for(0)
    out, _ = capfd.readouterr()
    assert out.strip() == "time is up"

#
def test_countdown_recursive_from_zero_prints_time_is_up(capfd):
    try:
        countdown_recursive(0)
    except RecursionError:
        pytest.fail("countdown_recursive(0) raised a RecursionError exception")
    out, _ = capfd.readouterr()
    assert out.strip() == "time is up"
    
#%% Day 12 Bite 38: Using ElementTree to parse XML
'''
In this Bite you will use ElementTree to parse some Nolan movies we extracted from OMDb.

Luckily most APIs switched to JSON, but sometimes XML is all there is, 
so at least learn to parse some! 
Complete the get_tree, 
get_movies and get_movie_longest_runtime functions below. 

See the docstrings and tests for more info.
Have fun and remember:
Keep calm and code in Python!
'''

import xml.etree.ElementTree as ET

# from OMDB
xmlstring = '''<?xml version="1.0" encoding="UTF-8"?>
<root response="True">
  <movie title="The Prestige" year="2006" rated="PG-13" released="20 Oct 2006" runtime="130 min" genre="Drama, Mystery, Sci-Fi" director="Christopher Nolan" />
  <movie title="The Dark Knight" year="2008" rated="PG-13" released="18 Jul 2008" runtime="152 min" genre="Action, Crime, Drama" director="Christopher Nolan" />
  <movie title="The Dark Knight Rises" year="2012" rated="PG-13" released="20 Jul 2012" runtime="164 min" genre="Action, Thriller" director="Christopher Nolan" />
  <movie title="Dunkirk" year="2017" rated="PG-13" released="21 Jul 2017" runtime="106 min" genre="Action, Drama, History" director="Christopher Nolan" />
  <movie title="Interstellar" year="2014" rated="PG-13" released="07 Nov 2014" runtime="169 min" genre="Adventure, Drama, Sci-Fi" director="Christopher Nolan"/>
</root>'''  # noqa E501


def get_tree():
    """You probably want to use ET.fromstring"""
    return ET.fromstring(xmlstring)


def get_movies():
    """Call get_tree and retrieve all movie titles, return a list or generator"""
    movie_titles = []
    for item in get_tree():
        movie_titles.append(item.attrib['title'])
    return movie_titles


def get_movie_longest_runtime():
    """Call get_tree again and return the movie title for the movie with the longest
       runtime in minutes, for latter consider adding a _get_runtime helper"""
    max_val = ''
    for item in get_tree():
        if item.attrib['runtime'] > max_val:
            max_val = item.attrib['runtime']
    for item in get_tree():
        if item.attrib['runtime'] == max_val:
            return item.attrib['title']
        
'''
scratch  - this works, figure out how to turn it into a function/loop!
for item in get_tree():
    if item.attrib['runtime'] == '169 min':
        print(item.attrib['title'])
'''

#%% Day 12 Bite 38: Testing Cases

import xml.etree.ElementTree as ET

#from nolan import get_tree, get_movies, get_movie_longest_runtime


def test_get_tree():
    tree = get_tree()
    assert type(tree) in (ET.ElementTree, ET.Element)
    assert len(list(tree.iter(tag='movie'))) == 5


def test_get_movies():
    assert list(get_movies()) == ['The Prestige', 'The Dark Knight',
                                  'The Dark Knight Rises', 'Dunkirk',
                                  'Interstellar']


def test_get_movie_longest_runtime():
    assert get_movie_longest_runtime() == 'Interstellar'

#%% Day 13 Bite 43: Force Keyword Arguments
'''
Write a function called get_profile that only allows 2 keyword arguments:
    name        which default to julian
    and 
    profession  and programmer respectively.

The function does nothing fancy, just return a str: name is a profession.

The point is to limit the interface of this function and you'll see Python makes it very easy ... have fun!
'''

#new concept here: using this format when defining variables in the function
#you force types for each variable as well as give it a default variable,
#the final arrow to str means the returning sentence will be of type str.

def get_profile(*, name:str='julian', profession:str='programmer') -> str:
    return '{} is a {}'.format(name, profession) 

#note! above we added the * as the first argument, doing so limits the function to NOT ACCEPT POS ARGS!

#%% Day 13 Bite 43: Testing Cases
import pytest

#from kwargs import get_profile


def test_no_arguments():
    assert get_profile() == 'julian is a programmer'


def test_one_positional_arg():
    with pytest.raises(TypeError):
        get_profile('julian')


def test_wrong_single_kw():
    with pytest.raises(TypeError):
        get_profile(test=True)


def test_wrong_additional_kw():
    with pytest.raises(TypeError):
        get_profile(name='bob', profession='software developer',
                    another_flag=False)


def test_correct_kw_second_default():
    assert get_profile(name='bob') == 'bob is a programmer'


def test_two_correct_kws():
    ret = get_profile(name='bob', profession='software developer')
    assert ret == 'bob is a software developer'


#%% Day 14 Bite 44: License Key Generator
'''
Write a function called gen_key that creates a license key with this format:
    KI80OMZ7-5OGYC1AC-735LDPT1-4L11XU1U

The key consists of a combination of upper case letters and digits.

It takes two arguments: parts and chars_per_part which default to 4 and 8 respectively, 
so you can call the function like:

gen_key() to get a similar key as above, or
as gen_key(parts=3, chars_per_part=4) to get a shorter one, e.g. 54N8-I70K-2JZ7
Before you default to random, check if Python >= 3.6 has a better option available for this task ...
'''

#import standard library modules here
import secrets
import string

#we can use secret to pick things from a list at random, might use that.
#we can also use a new module called string to construct an alphabet to use, 
#we could also just define one, idk which is faster
#printing string.ascii_upper took 2.08 us +-82 ns, they all took about the same time
#when you take into account their error. just use ascii_upper


def gen_key(parts: int = 4, chars_per_part: int = 8) -> str:
    """
    Generate and return a random license key containing
    upper case characters and digits.

    Example with default "parts" and "chars_per_part"
    being 4 and 8: KI80OMZ7-5OGYC1AC-735LDPT1-4L11XU1U

    If parts = 3 and chars_per_part = 4 a random license
    key would look like this: 54N8-I70K-2JZ7
    """
    password = ''                                   #creates a empty string
    dig = 0                                         #while loop digit
    chars = string.ascii_uppercase + string.digits  #creates string with all legal chars
    
    while dig < parts:                              
        word = ''.join(secrets.choice(chars) for i in range(chars_per_part))
                                                    #very slick list comp, steal again!
        if dig == 0:
            password = password + word
        else:
            password = password + '-' + word
        dig += 1 
    return password



#%% Day 14 Bite 44: Testing Cases

import re

#from license import gen_key

default_key = re.compile(r'^([A-Z0-9]{8}-){3}[A-Z0-9]{8}$')
shorter_key = re.compile(r'^([A-Z0-9]{4}-){2}[A-Z0-9]{4}$')
longer_key = re.compile(r'^([A-Z0-9]{10}-){9}[A-Z0-9]{10}$')


def test_gen_default_key():
    assert default_key.match(gen_key())


def test_gen_shorter_key():
    assert shorter_key.match(gen_key(parts=3, chars_per_part=4))


def test_gen_longer_key():
    assert longer_key.match(gen_key(parts=10, chars_per_part=10))


