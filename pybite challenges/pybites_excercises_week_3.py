# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 15:33:36 2023

@author: cray-sh

Pybites challenges in python Week One: Day 15 thru Day 22
"""
#%% Day 15 Bite 45: Keep a Queue of last n items
'''
How about writing a queue that holds the last 5 items?

Queue follows First-In-First-Out methodology, i.e., the data item stored first will be accessed first.
 A real-world example of queue can be a single-lane one-way road, where the vehicle enters first,
 exits first. More real-world examples can be seen as queues at the ticket windows and bus-stops. [source]
 
Complete the my_queue function to return a queue-like data type that keeps the last n items.

Check the standard library to see how you can do this in the shortest/most efficient way.

See an example output below and the tests that check for various values of n. Have fun!

'''

from collections import deque


def my_queue(n=5):
    return deque(maxlen=n)


if __name__ == '__main__':
    mq = my_queue()
    for i in range(10):
        mq.append(i)
        print((i, list(mq)))

    """Queue size does not go beyond n int, this outputs:
    (0, [0])
    (1, [0, 1])
    (2, [0, 1, 2])
    (3, [0, 1, 2, 3])
    (4, [0, 1, 2, 3, 4])
    (5, [1, 2, 3, 4, 5])
    (6, [2, 3, 4, 5, 6])
    (7, [3, 4, 5, 6, 7])
    (8, [4, 5, 6, 7, 8])
    (9, [5, 6, 7, 8, 9])
    """
'''
I had to look up the solution because I had no idea what was going wrong,
see above for the solution, I literally just needed to give one of the parameters a value...
The other piece of code was correct and can stay

#I got this to work earlier just have to turn it into a function
def my_queue(n=5):
    q = deque()
    l = []
    for i in range(7):          #i'm not sure if this should be n or 10
        q.append(i)
        if len(list(q)) > n:
            q.popleft()
        l.append((i, list(q)))
    return l
#this is showing returning a nonetype, I must have to do something with the fact that
#it wants the function to return a list of tuples, not a deque... must be something else we can do beyond returning q
'''

#%% Day 15 Bite 45: Testing Cases
import pytest

#from fifo import my_queue

q1 = my_queue(5)
q2 = my_queue(3)
q3 = my_queue(7)


@pytest.mark.parametrize('fn_in,expected_result', [
    (0, [0]),
    (1, [0, 1]),
    (2, [0, 1, 2]),
    (3, [0, 1, 2, 3]),
    (4, [0, 1, 2, 3, 4]),
    (5, [1, 2, 3, 4, 5]),
    (6, [2, 3, 4, 5, 6]),
])
def test_queue_default_arg(fn_in, expected_result):
    q1.append(fn_in)
    assert list(q1) == expected_result


@pytest.mark.parametrize('fn_in,expected_result', [
    (0, [0]),
    (1, [0, 1]),
    (2, [0, 1, 2]),
    (3, [1, 2, 3]),
    (4, [2, 3, 4]),
    (5, [3, 4, 5]),
    (6, [4, 5, 6]),
])
def test_queue_less_items(fn_in, expected_result):
    q2.append(fn_in)
    assert list(q2) == expected_result


@pytest.mark.parametrize('fn_in,expected_result', [
    (0, [0]),
    (1, [0, 1]),
    (2, [0, 1, 2]),
    (3, [0, 1, 2, 3]),
    (4, [0, 1, 2, 3, 4]),
    (5, [0, 1, 2, 3, 4, 5]),
    (6, [0, 1, 2, 3, 4, 5, 6]),
])
def test_queue_more_items(fn_in, expected_result):
    q3.append(fn_in)
    assert list(q3) == expected_result

#%% Day 16 Bite 46: You are a programmer! Code Fizz Buzz 
'''
Here is a beginner Bite to write Fizz Buzz:

Fizz buzz is a group word game for children to teach them about division. 

Players take turns to count incrementally, replacing any number divisible by three with the word "fizz",
 and any number divisible by five with the word "buzz".
...
For example, a typical round of fizz buzz would start as follows:
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz,
 Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ..
 
Complete the fizzbuzz function below, it should take a number and return the right str or int.

If you want to write this TDD-style, consider doing Code Challenge 45 instead.

See also Coding Horror's Why Can't Programmers.. Program? for a fun read.
'''

from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:    
    if num % 5 == 0 and num % 3 == 0:
        return 'Fizz Buzz'
    if num % 5 == 0:
        return 'Buzz'
    if num % 3 == 0:
        return 'Fizz'
    else:
        return num
    
    
    
#%% Day 16 Bite 46: Testing Cases
'''
These are hidden for this problem!

I got this one pretty easily and will put the testing cases below:
'''

import pytest

#from fizzbuzz import fizzbuzz


@pytest.mark.parametrize("arg, ret",[
    (1, 1),
    (2, 2),
    (3, 'Fizz'),
    (4, 4),
    (5, 'Buzz'),
    (6, 'Fizz'),
    (7, 7),
    (8, 8),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (11, 11),
    (12, 'Fizz'),
    (13, 13),
    (14, 14),
    (15, 'Fizz Buzz'),
    (16, 16),
])
def test_fizzbuzz(arg, ret):
    assert fizzbuzz(arg) == ret

#%% Day 17 Bite 54: Nicer formatting of a poem or text
'''
In this Bite you complete print_hanging_indents to print a poem (or text) in a nicer way.

For example calling it on (part of) Christina Rosetti's Remember it should convert:

                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
to:

Remember me when I am gone away,
    Gone far away into the silent land;
    When you can no more hold me by the hand,
Nor I half turn to go yet turning stay.
Remember me when no more day by day
    You tell me of our future that you planned:
    Only remember me; you understand
print the resulting poem (don't return it)! The tests include another text snippet from Shakespeare. 

Have fun!
'''

#there needs to be someway of the if/elif to tell what the ending character of the line was 

INDENTS = 4 * ' '

def print_hanging_indents(poem):
    '''This is the complete version that adds indents when appropriate to the text within poem'''
    flagma = False                     #starts False which means no indent on first line
    troubled_chars = ',:;'              #these are the chars that if the line ends with it do not flip flagma
    for line in poem.split('\n'):      #if flagma is flipped, next line will have no indent
        if flagma and line.strip() != '':
            line = INDENTS + line.strip()
            print('{}'.format(line))
            if line[-1] not in troubled_chars:
                flagma = False
        elif line.strip() == '':
            flagma = False
        elif line.strip() != '':
            print('{}'.format(line.strip()))
            if line.endswith('.'):
                flagma = False
            else: 
                flagma = True

def print_hanging_indents_diagnostic_mode(poem):
    '''This version parses a poem and adds indents in like print_hanging_indents,
    but also includes the line number'''
    i = 0
    flagma = False                     #starts False which means no indent on first line
    troubled_chars = ',:;'              #these are the chars that if the line ends with it do not flip flagma
    for line in poem.split('\n'):      #if flagma is flipped, next line will have no indent
        if flagma and line.strip() != '':
            line = INDENTS + line.strip()
            print('{}:{}'.format(i, line))
            i += 1
            if line[-1] not in troubled_chars:
                flagma = False
        elif line.strip() == '':
            flagma = False
        elif line.strip() != '':
            print('{}:{}'.format(i,line.strip()))
            i += 1
            if line.endswith('.'):
                flagma = False
            else: 
                flagma = True
    
#%% Day 17 Bite 54: Testing Cases

#from poem import print_hanging_indents

# part of William Shakespeare's play Hamlet
shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """

shakespeare_formatted = """
To be, or not to be, that is the question:
    Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
    Or to take Arms against a Sea of troubles,
"""

# part of Remember, by Christina Rosetti
rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """


rosetti_formatted = """
Remember me when I am gone away,
    Gone far away into the silent land;
    When you can no more hold me by the hand,
Nor I half turn to go yet turning stay.
Remember me when no more day by day
    You tell me of our future that you planned:
    Only remember me; you understand
"""


def test_shakespeare_text(capfd):
    print_hanging_indents(shakespeare_unformatted)
    output = capfd.readouterr()[0]
    assert output.strip() == shakespeare_formatted.strip()


def test_rosetti_poem(capfd):
    print_hanging_indents(rosetti_unformatted)
    output = capfd.readouterr()[0]
    assert output.strip() == rosetti_formatted.strip()
    
#%% Day 18 Bite 55: Get the latest game releases from Steam's RSS feed
'''
The Steam gaming platform has an RSS feed of their latest game releases. 

In this Bite, you'll pull down and parse that feed.

Specifically, pull out the names of the games in the feed as well as their URLs. 

Use the Game namedtuple provided.

To make sure you work with a static feed we copied today's version so use the URL defined in FEED_URL. 

Enjoy!    

'''
from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')             #this is new, the named tuple allows us to organize
                                                    #the imported feed, we will give Game two items the 'Game' Name
                                                    #and the link of the game
def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    steam = feedparser.parse(FEED_URL)              #stores the RSS feed imported as steam
    listma = []                                     #the feedparser.parse imports RSS feeds give it a URL
    for item in steam.entries:                      #I figured out this name by for item in steam return item
        listma.append(Game(item.title, item.link))
    return listma

#%% Day 18 Bite 55: Their Solution to get_games()
#they used list comprehsnsion which is considerably faster but less readable, be mindful of the balance

def get_games_lc():
    """Same as get_games() but uses list comprehension"""
    feed = feedparser.parse(FEED_URL)
    return [Game(entry.title, entry.link)
            for entry in feed.entries]

#%% Day 18 Bite 55: Testing Cases

#from steam import get_games

# should mock this out but let's call feedparser for real
# for a feedparser mocking see the AttrDict (advanced) Bite 50's tests
games = get_games()


def test_assert_number_of_entries():
    assert len(games) == 30


def test_all_list_items_are_namedtuples():
    assert all(isinstance(game, tuple) for game in games)


def test_assert_all_links_contain_store():
    assert all('store.steampowered.com' in game.link for game in games)


def test_title_and_url_first_entry():
    first_game = games[0]
    assert first_game.title == 'Midweek Madness - RiME, 33% Off'
    assert first_game.link == 'http://store.steampowered.com/news/31695/'


def test_title_and_url_last_entry():
    last_game = games[-1]
    assert last_game.title == 'Now Available on Steam - Loco Dojo, 35% off!'
    assert last_game.link == 'http://store.steampowered.com/news/31113/'

#%% Day 19 Bite 56: Add a command line interface to our BMI Calculator
'''
Complete create_parser below so that our BMI program can be called like this:

$ python bmi.py -h
usage: bmi.py [-h] [-w WEIGHT] [-l LENGTH]

Calculate your BMI.

optional arguments:
  -h, --help            show this help message and exit
  -w WEIGHT, --weight WEIGHT
                        Your weight in kg
  -l LENGTH, --length LENGTH
                        Your length in cm

$ python bmi.py -w 80 -l 187
Your BMI is: 22.88
Please note that calc_bmi and handle_args are given, you only need to code create_parser!

We have two more Bites to practice argparse: 57 and 58.
'''
import argparse


def calc_bmi(weight, length):
    """Provided/DONE:
       Calc BMI give a weight in kg and length in cm, return the BMI
       rounded on 2 decimals"""
    bmi = int(weight) / ((int(length) / 100) ** 2)
    return round(bmi, 2)


def create_parser():
    """TODO:
       Create an ArgumentParser adding the right arguments to pass the tests,
       returns a argparse.ArgumentParser object"""
    # creates parser object and gives it a description in help
    parser = argparse.ArgumentParser(description="Calculate your BMI.")

    # adds arguments to the parser
    parser.add_argument("-w",                         #the single dash is shorthand
                        "--weight",                   #longhand version of var, also double means optional
                        action = 'store',             #there are a couple different ones, this stores the val
                        default = None,               #you can use this to set the default value to thsee vars
                        help="Your weight in kg")     #the message that will appear when help is used

    parser.add_argument("-l",
                        "--length",
                        action = 'store',
                        default = None,
                        help="Your length in cm")
#NOTE: You have to make sure you do not add args = parser.parse_args() prematurely here, it will be called
# later
#NOTE: You have to run this via command line or it won't work because it is sys args we are using
    
    return parser


def handle_args(args=None):
    """Provided/DONE:
       Call calc_bmi with provided args object.
       If args are not provided get them from create_parser"""
    if args is None:
        parser = create_parser()
        args = parser.parse_args()

    if args.weight and args.length:
        bmi = calc_bmi(args.weight, args.length)
        print(f"Your BMI is: {bmi}")
    else:
        print("Need both weight and length args")


if __name__ == "__main__":
    handle_args()    
    
#%% Day 19 Bite 56: Testing Cases

import pytest

#from bmi import create_parser, handle_args


@pytest.fixture
def parser():
    return create_parser()


def test_help_flag_exits(parser):
    with pytest.raises(SystemExit):
        parser.parse_args(["-h"])


def test_no_args_exits(parser, capfd):
    args = parser.parse_args([])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert output.strip() == "Need both weight and length args"


def test_only_width_exits(parser, capfd):
    args = parser.parse_args(["-w", "80"])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert output.strip() == "Need both weight and length args"


def test_only_length_exits(parser, capfd):
    args = parser.parse_args(["-l", "187"])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert output.strip() == "Need both weight and length args"


def test_two_arg(parser, capfd):
    args = parser.parse_args(["-w", "80", "-l", "187"])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert "Your BMI is: 22.88" in output


def test_two_arg_reversed_order(parser, capfd):
    args = parser.parse_args(["-l", "187", "-w", "80"])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert "Your BMI is: 22.88" in output


def test_different_args(parser, capfd):
    args = parser.parse_args(["-l", "200", "-w", "100"])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert "Your BMI is: 25.0" in output


#%% Day 20 Bite 64: Fix a truncating zip function
'''
Bert is in charge of organizing an event and got the attendees names, 
locations and confirmations in 3 lists. 

Assuming he got all data and being Pythonic he used zip to stitch them together (see template code) 
but then he sees the output:

('Tim', 'DE', False)
('Bob', 'ES', True)
('Julian', 'AUS', True)
('Carmen', 'NL', False)
('Sofia', 'BR', True)

What?! Mike, Kim, and Andre are missing! 
You heard somebody mention itertools the other day for its power to work with iterators. 
Maybe it has a convenient way to solve this problem? 
Check out the module and patch the get_attendees function for Bert so it returns all names again. 
For missing data use dashes (-). After the fix Bert should see this output:

('Tim', 'DE', False)
('Bob', 'ES', True)
('Julian', 'AUS', True)
('Carmen', 'NL', False)
('Sofia', 'BR', True)
('Mike', 'US', '-')
('Kim', '-', '-')
('Andre', '-', '-')

Good luck, Bert will be grateful if you fix this bug for him! 
By the way, this won't be the last itertools Bite, 
it is a power tool you want to become familiar with!

This was actually very easily solved using the package itertools module zip_longest
that function allows one to specify a value (fillvalue) to insert if one of the lists being zipped
is not of the same length, it will use the length of the longest list and then fill the value specified.
'''

import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
    for participant in itertools.zip_longest(names, locations, confirmed, fillvalue='-'):
        print(participant)


if __name__ == '__main__':
    get_attendees()


#%% Day 20 Bite 64: Testing Cases
#from event import get_attendees
#since this is a readoutter check this will have to be done via running the script instead of inside console

def test_get_attendees(capfd):
    get_attendees()
    output = capfd.readouterr()[0].strip().split("\n")

    assert len(output) == 8
    assert "('Kim', '-', '-')" in output
    assert "('Andre', '-', '-')" in output
    
#%% Day 21 Bite 66: Calculate the running average of a sequence
'''
Write a function that takes a sequence of items and returns the running average, so for example this:

running_mean([1, 2, 3])
returns:

[1, 1.5, 2]
You can assume all items are numeric so no type casting is needed.

Round the mean values to 2 decimals (4.33333 -> 4.33). See the tests for more info.

Bonus: use a function of itertools + make it a generator, but this is not required to get this working.
'''
from itertools import accumulate

def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
#so I took the approach of an itertool function and list comprehension, I think it did well
#but does not use a generator :( I'll have to add their solution below.       
    result = [x for x in accumulate(sequence)]
    final_result = []
    i = 1
    for number in result:
        final_result.append(round(number/i, 2))
        i += 1
    return final_result

#NOTE Currently I have a problem where two values are repeated, because I used index it finds the first
#instance of it instead of whichever instance it is on.
#EDIT I have fixed that problem but had to use a for loop with a count, this works but I'm sure there
#is a better way that they'll definitely do.

#%% Day 21 Bite 66: Their Solution

#I was so close, they fixed the problem introduced by .index() which was the way I was attempting to use
#in order to get the number of items within to calculate the average, by using enuemrate which will return
# a zipped list of an iterable and the item. This is kind of what I did but with less steps and
#is most likely more pythonable or whatever it's called.
from itertools import accumulate


def running_mean_old(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    if not sequence:
        return []

    total = 0
    running_mean = []

    for i, num in enumerate(sequence, 1):
        total += num
        mean = round(total/i, 2)
        running_mean.append(mean)

    return running_mean


def running_mean2(sequence):
    """Same functionality as above but using itertools.accumulate
       and turning it into a generator"""
    for i, num in enumerate(accumulate(sequence), 1):
        yield round(num/i, 2)

#%% Day 21 Bite 66: Testing Cases
import pytest

#from running_mean import running_mean


@pytest.mark.parametrize("input_argument, expected_return", [
    ([1, 2, 3], [1, 1.5, 2]),
    ([2, 6, 10, 8, 11, 10],
     [2.0, 4.0, 6.0, 6.5, 7.4, 7.83]),
    ([3, 4, 6, 2, 1, 9, 0, 7, 5, 8],
     [3.0, 3.5, 4.33, 3.75, 3.2, 4.17, 3.57, 4.0, 4.11, 4.5]),
    ([], []),
])
def test_running_mean(input_argument, expected_return):
    ret = list(running_mean(input_argument))
    assert ret == expected_return
    
#%% Day 22 Bite 67: Working with Datetimes
'''
This Bite involves solving two problems using datetime:

We kicked off our 100 Days of Code project on March 30th, 2017. 
Calculate what date we finished the full 100 days!
PyBites was founded on the 19th of December 2016. 
We're attending our first PyCon together on May 8th, 2018. 
Can you calculate how many days from PyBites' inception to our first PyCon meet up?
'''

from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    hun_days = start_100days + timedelta(days=100)      #recall you can use timedelta to add or remove time
    return hun_days.isoformat()                         #from any type of datetime.date, isoformat gives it the
                                                        #requested format
def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    diff = pycon_date - pybites_founded                 #you can also subtract any two datetimes to get a 
    return int(diff.days)                               #time delta which you can then attribute pull the days

#%% Day 22 Bite 67: Their solution
'''I am adding this solution because it is a good example making it more efficient/trimming down
'''
def get_hundred_days_end_date_them():
    """Return a string of yyyy-mm-dd"""
    return str(start_100days + timedelta(days=100))


def get_days_between_pb_start_first_joint_pycon_them():
    """Return the int number of days"""
    return (pycon_date - pybites_founded).days
#%% Day 22 Bite 67: Testing Cases
#from calc_dts import (get_hundred_days_end_date,
#                      get_days_between_pb_start_first_joint_pycon)


def test_get_hundred_days_end_date():
    assert get_hundred_days_end_date() == '2017-07-08'


def test_get_days_till_pycon_meetup():
    assert get_days_between_pb_start_first_joint_pycon() == 505