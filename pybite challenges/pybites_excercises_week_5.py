# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:49:18 2023

@author: cray-sh

Pybites challenges in python Week One: Day 30 thru Day 36
"""
#%% Day 30 Bite 100: Display the last par of a file (unix tail)
'''

Complete the function below simulating Unix' tail, for example:

$ tail -3 test_tail.py
# byte to str conversion and strip off last line's newline char
expected = [line.decode("utf-8") for line in lines]
assert tail(f.name, 10) == expected
Complete the function below which receives (absolute) filepath 

and n lines to filter from the end which is returned in a list.

For example, if we call it on a file - stored in filepath - with this content:

Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!
... and give it n of 2 (= calling it as: tail(filepath, 2)), it should return this:

['Keep calm and code in Python!',
 'Become a PyBites ninja!']
(note: newlines are stripped off)

Have fun and let us know if you have any questions ...
'''
from pathlib import Path
from typing import List


def tail(filepath: Path, n: int) -> List[str]:
    """
    Similate Unix' "tail -n" command:
    - Read in the file ("filepath").
    - Parse it into a list of lines, stripping trailing newlines.
    - Return the last "n" lines.
    """
    with open(filepath) as file:
        #read into a variable
        content = file.read()
        
        #create a list of all the lines within that read into variable
        list_of_lines = content.splitlines()
        
        #create a list that will hold the lines that are not empty
        list_no_blank = []
        for lines in list_of_lines:
            if lines != '':
                list_no_blank.append(lines)
                
        #finally return the list but only the lines the user stated in n, threw negative because its from
        #the bottom
        
    return list_no_blank[-n:]

#%% Day 30 Bite 100: Their Solution
'''
This one went well as well, theres was more efficient but accomplished the same, 
theres would probably work better in longer texts...

They used another list comprehension, man I gotta use these more!

I would be curious to test these two in timeit

They also used open instead of read, I need to look into whyand when you use each of those.
'''

from pathlib import Path
from typing import List


def tailS(filepath: Path, n: int) -> List[str]:
    """
    Similate Unix' "tail -n" command:
    - Read in the file ("filepath").
    - Parse it into a list of lines, stripping trailing newlines.
    - Return the last "n" lines.
    """
    with filepath.open() as f:
        lines = [line.rstrip() for line in f.readlines()]
        return lines[-n:]    
    
#%% Day 30 Bite 100: Testing Cases
import pytest

#from tail import tail

content = b"""Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""


# https://docs.pytest.org/en/latest/tmpdir.html#the-tmpdir-factory-fixture

@pytest.fixture
def my_file(tmp_path):
    f = tmp_path / "some_file.txt"
    f.write_bytes(content)
    return f


def test_tail_various_args(my_file):
    assert tail(my_file.resolve(), 1) == ['Become a PyBites ninja!']
    assert tail(my_file.resolve(), 2) == ['Keep calm and code in Python!',
                                          'Become a PyBites ninja!']


def test_tail_arg_gt_num_lines_files(my_file):
    # n of > file length basically gets the whole file, but need to do some
    # byte to str conversion and strip off last line's newline char
    actual = tail(my_file.resolve(), 10)
    expected = [line.decode("utf-8")
                for line in content.splitlines()]
    assert actual == expected

#%% Day 31 Bite 115: Count leading spaces

'''
A small but interesting Bite: given a string with leading indent spacing,

 calculate the amount of space (literal space, not tab or newline) characters:

'string  ' -> 0 (we only care about leading spacing)
'  string' -> 2
'    string' -> 4
etc...
This can be done in many ways so once done we encourage you to go into the Bite forum 
(Discussion tab that appears upon solving the Bite) to discuss your solution with fellow Pythonistas ... 
Have fun!
'''

def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """
    num = 0
    for char in text:
        if char == ' ':
            num += 1
        else:
            return num

#%% Day 31 Bite 115: Other Solutions

def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """
    # originally we had:
    # import re
    # re.split('\S', s)[0].count(' ')
    # but this is more elegant (credit: https://stackoverflow.com/a/13241465)
    return len(text) - len(text.lstrip(' '))




#%% Day 31 Bite 115: Testing Cases

import pytest

#from indents import count_indents


@pytest.mark.parametrize("input_string, count", [
   ('string  ', 0),
   ('  string', 2),
   ('    string', 4),
   ('            string', 12),
   ('\t\tstring', 0),
   ('  str  ing', 2),
   ('  str  ', 2),
])
def test_count_indents(input_string, count):
    assert count_indents(input_string) == count

#%% Day 32 Bite 117: Round a number even (a.k.a. banker's rounding)
'''
Bankers Rounding is an algorithm for rounding quantities to integers,
 in which numbers which are equidistant from the two nearest integers are rounded
 to the nearest even integer. Thus, 0.5 rounds down to 0; 1.5 rounds up to 2. - source
 
Complete the function below that takes an float,
 returning it rounded even.
'''
#This was super easy because they inadvertently asked to do the job of a default function within python,
#see below for an alternative way to do it

def round_even(number):
    """Takes a number and returns it rounded even"""
    return round(number)


#%% Day 32 Bite 117: Their Solution
#So this is a weird bite, the solution was a simple built in function that works exactly
#as they wanted it.
#They submitted this as the initial answer, it uses a module called decimal and function called Decimal
from decimal import Decimal     

def round_even_decimalpack(number):
    print(Decimal(number).quantize(0))
 
#note I had to change this from return to print() because the return statement would return a Decimal obj
#why, I have no idea man

#%% Day 32 Bite 117: Testing Cases

import pytest

#from round_even import round_even


@pytest.mark.parametrize("arg, expected", [
    (0.4, 0),
    (0.5, 0),  # nearest even int
    (0.6, 1),
    (1.4, 1),
    (1.5, 2),
    (1.6, 2),
    (2.5, 2),  # nearest even int
])
def test_round_even(arg, expected):
    assert round_even(arg) == expected





#%% Day 33 Bite 128: Work with datetime's strptime and strftime
'''
In this Bite you get some more practice with datetime's useful strptime and stftime.

Complete the two functions: years_ago and convert_eu_to_us_date following 
the instructions in their docstrings.

This is the definition and difference between the two:

strptime: parse (convert) string to datetime object.
strftime: create formatted string for given time/date/datetime object according to specified format.
Reference: 8.1.8. strftime() and strptime() Behavior. Good luck and keep calm and code in Python!

'''
from datetime import datetime

THIS_YEAR = 2018


def years_ago(date):
    """Receives a date string of 'DD MMM, YYYY', for example: 8 Aug, 2015
       Convert this date str to a datetime object (use strptime).
       Then extract the year from the obtained datetime object and subtract
       it from the THIS_YEAR constant above, returning the int difference.
       So in this example you would get: 2018 - 2015 = 3"""
    time = datetime.strptime(date, '%d %b, %Y')
    return THIS_YEAR - time.year


def convert_eu_to_us_date(date):
    """Receives a date string in European format of dd/mm/yyyy, e.g. 11/03/2002
       Convert it to an American date: mm/dd/yyyy (in this case 03/11/2002).
       To enforce the use of datetime's strptime / strftime (over slicing)
       the tests check if a ValueError is raised for invalid day/month/year
       ranges (no need to code this, datetime does this out of the box)"""
    am_form, eu_form = '%m/%d/%Y', '%d/%m/%Y'
    time = datetime.strptime(date, eu_form)
    return time.strftime(am_form)
    
#%% Day 33 Bite 128: Testing Cases

import pytest

#from dt_convert import years_ago, convert_eu_to_us_date


def test_years_ago():
    assert years_ago('8 Aug, 2015') == 3
    assert years_ago('6 Sep, 2014') == 4
    assert years_ago('1 Oct, 2010') == 8
    assert years_ago('31 Dec, 1958') == 60


def test_years_ago_wrong_input():
    with pytest.raises(ValueError):
        # Sept != valid %b value 'Sep'
        assert years_ago('6 Sept, 2014') == 4


def test_convert_eu_to_us_date():
    assert convert_eu_to_us_date('11/03/2002') == '03/11/2002'
    assert convert_eu_to_us_date('18/04/2008') == '04/18/2008'
    assert convert_eu_to_us_date('12/12/2014') == '12/12/2014'
    assert convert_eu_to_us_date('1/3/2004') == '03/01/2004'


def test_convert_eu_to_us_date_invalid_day():
    with pytest.raises(ValueError):
        convert_eu_to_us_date('41/03/2002')


def test_convert_eu_to_us_date_invalid_month():
    with pytest.raises(ValueError):
        convert_eu_to_us_date('11/13/2002')


def test_convert_eu_to_us_date_invalid_year():
    with pytest.raises(ValueError):
        convert_eu_to_us_date('11/13/year')    
    
#%% Day 34 Bite 130: Analyze some basic Car Data
'''
In this exercise you will analyze some basic car data. 

Here is the (fake) JSON data we created with Mockeroo - snippet below / full output here:

  [{"id":1,"automaker":"Dodge","model":"Ram Van 1500","year":1999},
   {"id":2,"automaker":"Chrysler","model":"Town & Country","year":2002},
   {"id":3,"automaker":"Porsche","model":"Cayenne","year":2008},
   ... 997 car entries more ...
  ]
First you will write most_prolific_automaker to find out which automaker 
produces the most new models for a particular year.

Secondly you will write get_models which filters the data set down to car models 
produced by a particular automaker and year (as passed into the function).

To keep it a Beginner Bite we'll pause here, but if you like this data set,
 let us know and we make a follow-up Bite, maybe we can add some financial data :)

Check out the docstrings and pytests and give it a shot. Good luck and keep calm keep and code in Python.
'''
from collections import Counter
#The new function we are using from package collections is a counter that acts as a countainer
#that will count a list that you give it, I had some trouble directly sending a dictionary to it,
#so an intermediate step that appended the values to a list happened. I also needed to do this because it 
#was splitting the entries by letter instead of keeping the full name, I suspect there is a way to do that
#directly and will probably pop up in their solution.

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    temp_list = []
    for item in data:
        if item['year'] == year:
            temp_list.append(item['automaker'])
    countma = Counter(temp_list)
    return countma.most_common(1)[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    temp_list = []
    for item in data:
        if item['year'] == year and item['automaker'] == automaker:
            temp_list.append(item['model'])
    countma = Counter(temp_list)
    return set(countma)

#%% Day 34 Bite 130: Their Solution
#The big difference was using list comprehension (which I should have done), instead of loops

from collections import Counter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    cnt = Counter(row["automaker"] for row in data
                  if row["year"] == year).most_common()
    return cnt[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    return set([row["model"] for row in data
                if row["automaker"] == automaker and
                row["year"] == year])

#%% Day 34 Bite 130: Testing Cases

#from cars import most_prolific_automaker, get_models


def test_most_prolific_automaker_1999():
    assert most_prolific_automaker(1999) == 'Dodge'


def test_most_prolific_automaker_2008():
    assert most_prolific_automaker(2008) == 'Toyota'


def test_most_prolific_automaker_2013():
    assert most_prolific_automaker(2013) == 'Hyundai'


def test_get_models_volkswagen():
    models = get_models('Volkswagen', 2008)
    # sets are unordered
    assert len(models) == 2
    assert 'Jetta' in models
    assert 'Rabbit' in models


def test_get_models_nissan():
    assert get_models('Nissan', 2000) == {'Pathfinder'}


def test_get_models_open():
    # not in data set
    assert get_models('Opel', 2008) == set()


def test_get_models_mercedes():
    models = get_models('Mercedes-Benz', 2007)
    assert len(models) == 3
    assert 'SL-Class' in models
    assert 'GL-Class' in models
    assert 'CL-Class' in models

#%% Day 35 Bite 133: Convert an Amazon URL into an affiliation link
'''
Can you help PyBites automate their Amazon affiliation link creation?

Complete the generate_affiliation_link(url) function below which should convert the following links:

https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/?keywords=war+of+art
https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/ref=sr_1_1
https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/?qid=1537226234
https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X
https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/1449340377/
... into the following affiliation links respectively:

http://www.amazon.com/dp/1936891026/?tag=pyb0f-20
http://www.amazon.com/dp/1936891026/?tag=pyb0f-20
http://www.amazon.com/dp/1936891026/?tag=pyb0f-20
http://www.amazon.com/dp/020161622X/?tag=pyb0f-20
http://www.amazon.com/dp/1449340377/?tag=pyb0f-20
Hint: regex might be overkill here! Have fun and remember, keep calm and code in Python!
'''
#I really condensed this one, but also thought about breaking it up into parts such as gen_aff_link for read
#ability
    
def generate_affiliation_link(url):
    return 'http://www.amazon.com/dp/' + url.split('/')[5] + '/?tag=pyb0f-20'

def gen_aff_link(url):
    beginning_url = 'http://www.amazon.com/dp/'
    middle_url = url.split('/')[5]
    end_url = '/?tag=pyb0f-20'
    return beginning_url + middle_url + end_url



#%% Day 35 Bite 133: Testing Cases

import pytest

#from affiliation import generate_affiliation_link

original_links = [
    ('https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/'
     '?keywords=war+of+art'),
    ('https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/'
     'ref=sr_1_1'),
    ('https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/'
     '?qid=1537226234'),
     'https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X',
    ('https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/'
     '1449340377/'),
    ('https://www.amazon.com/fake-book-with-longer-asin/dp/'
     '1449340377000/'),
]  # noqa E501
result_links = [
    'http://www.amazon.com/dp/1936891026/?tag=pyb0f-20',
    'http://www.amazon.com/dp/1936891026/?tag=pyb0f-20',
    'http://www.amazon.com/dp/1936891026/?tag=pyb0f-20',
    'http://www.amazon.com/dp/020161622X/?tag=pyb0f-20',
    'http://www.amazon.com/dp/1449340377/?tag=pyb0f-20',
    'http://www.amazon.com/dp/1449340377000/?tag=pyb0f-20',
]


@pytest.mark.parametrize('amz_link, affil_link', zip(original_links,
                                                     result_links))
def test_get_word_max_vowels(amz_link, affil_link):
    assert generate_affiliation_link(amz_link) == affil_link


#%% Day 36 Bite 136: Bloodtypes
'''
Check red blood cell compatibility between donor and recipient.

For simplicity, only eight basic types of blood are considered.

The input of blood type can be in the form of:

Bloodtype enumeration
An integer value between 0 and 7
Textual representation e.g. "0-", "B+", "AB+", ...
There are 8 basic blood types based on presence or absence of three antigens: A, B, and Rh-D.

0- no antigens
0+ Rh-D antigen
A- antigen A
A+ antigen A and Rh-D
B- antigen B
B+ antigen B and Rh-D
AB- antigen A and B
AB+ all 3 antigens (A, B, Rh-D)
General rule:

An individual who does not have a certain antigen cannot receive a blood from someone who has that antigen.
Blood group 0 individuals do not have A or B antigens. 
Therefore, a group 0 individual can receive blood only from a group 0 individual, 
but can donate blood to individual with types A, B, 0 or AB.

Blood group A individuals have the A antigen. 
Therefore, a group A individual can receive blood only from individuals of groups A or 0, 
and can donate blood to individuals with type A or AB.

Blood group B individuals have the B antigen. 
Therefore, a group B individual can receive blood only from individuals of groups B or 0, 
and can donate blood to individuals with type B or AB.

Blood group AB individuals have both A and B antigens. 
Therefore, an individual with type AB blood can receive blood from AB0, 
but cannot donate blood to any group other than AB.

Rh-D negative individuals do not have Rh-D antigen. 
Therefore, Rh-D negative can receive blood only from other Rh-D negative individuals.

Rh-D positive individuals have Rh-D antigen. 
Therefore, Rh-D positive individual can receive blood from both Rh-D negative or positive individuals.

Individuals with 0- are universal donors. Individuals with AB+ are universal recipients.

The rules described are general. In practice, there are over 340 different blood-group antigens.

Tasks Complete the function check_bt()
The function should check red blood cell compatibility between a donor and a recipient.

Return True for compatibility between the donor and the recipient, False otherwise.

If the input value is not a required type raise TypeError .

If the input value is not in the defined interval raise ValueError .
'''
"""
Write a function which checks the red blood cell compatibility between donor and recipient.
https://en.wikipedia.org/wiki/Blood_type#Red_blood_cell_compatibility
For simplicity, the appearance of 8 basic types of blood is considered.
The input of blood type can be in the form of:
    pre defined Bloodtype enum e.g.: Bloodtype.ZERO_NEG
    value of the pre-defined Bloodtype 0..7
    pre defined text  e.g. "0-", "B+", "AB+", ...
    If input value is not a required type TypeError is raised.
    If input value is not in defined interval ValueError is raised.
Keywords: enum, exception handling, multi type input
"""

from enum import Enum


class Bloodtype(Enum):
    ZERO_NEG = 0
    ZERO_POS = 1
    B_NEG = 2
    B_POS = 3
    A_NEG = 4
    A_POS = 5
    AB_NEG = 6
    AB_POS = 7


blood_type_text = {
    "0-": Bloodtype.ZERO_NEG,
    "0+": Bloodtype.ZERO_POS,
    "B-": Bloodtype.B_NEG,
    "B+": Bloodtype.B_POS,
    "A-": Bloodtype.A_NEG,
    "A+": Bloodtype.A_POS,
    "AB-": Bloodtype.AB_NEG,
    "AB+": Bloodtype.AB_POS,
}

# complete :
def check_bt(donor, recipient):
    """ Checks red blood cell compatibility based on 8 blood types
        Args:
        donor (int | str | Bloodtype): red blood cell type of the donor
        recipient (int | str | Bloodtype): red blood cell type of the recipient
        Returns:
        bool: True for compatability, False otherwise.
    """
#Check format of donor, reformat to number for the _partiuclar antigen comp function
#if the format is not in the three types accepted raise TypeError

    if type(donor) == str:
        if donor not in blood_type_text.keys():
            raise ValueError('That is not a recognized blood type')
        d_type = blood_type_text[donor].value
        
    elif type(donor) == int:
        if donor not in range(0,8):
            raise ValueError('That is not a recognized blood type')
        d_type = donor
        
    elif type(donor) == Bloodtype:
        d_type = donor.value
    
    else:
        raise TypeError('It must be in str, int or Bloodtype format')

#check format of recipient, reformat to number, if not one of three acceptable types raise TypeError

    if type(recipient) == str:
        if recipient not in blood_type_text.keys():
            raise ValueError
        r_type = blood_type_text[recipient].value
        
    elif type(recipient) == int:
        if recipient not in range(0,8):
            raise ValueError
        r_type = recipient
        
    elif type(recipient) == Bloodtype:
        r_type = recipient.value
    else:
        raise TypeError('It must be in str, int, or Bloodtype format')

#This checks for a negative number within the tuple returned by _particular_antigen_comp,
#if a negative number is in there it means an incompatability which needs to return False    

    for number in _particular_antigen_comp(d_type, r_type):
        if number < 0:
            return False
    return True
    


# hint
def _particular_antigen_comp(donor: int, recipient: int) -> tuple:
    """Returns a particalar antigen compatibility, where each tuple member
    marks a compatibility for a particular antigen  (A, B, Rh-D).
    If tuple member is non-negative there is a compatibility.
    For red blood cell compatibility is required that 
    all tuple members are non-negative (i.e. compatibility for all 3 antigens).
    0- bloodtype is represented as 0 ; AB+ is represented as 7; see Bloodtype enum
    Examples:
    _particular_antigen_comp(0, 7) -> (1, 1, 1)    0- can donate to AB+
    _particular_antigen_comp(1, 3) -> (0, 1, 0)    0+ can donate to B+
    _particular_antigen_comp(2, 5) -> (1, -1, 1)   B+ cannot donate to A+
    _particular_antigen_comp(7, 0) -> (-1, -1, -1) AB+ cannot donate to 0-
    """
    return (
        ((recipient // 4) % 2) - ((donor // 4) % 2),
        ((recipient // 2) % 2) - ((donor // 2) % 2),
        (recipient % 2) - (donor % 2),
    )
    

#%% Day 36 Bite 136: Their Solution
'''Although I should have also used a second function, they also snuck in the _particular_antigen_comp into
the check function instead of having it separate which shortens and quickens things too.
I liked how I kept some of the checks separate for debugging, but probably could condense too'''

# possible solution:
def check_bt(donor, recipient):
    """ Checks red blood cell compatibility based on 8 blood types
        Args:
        donor (int | str | Bloodtype): red blood cell type of the donor
        recipient (int | str | Bloodtype): red blood cell type of the recipient
        Returns:
        bool: True for compatability, False otherwise.
    """
    donor = _check_convert_input(donor)
    recipient = _check_convert_input(recipient)
    d = donor.value
    r = recipient.value
    anti_gen_comp = (r // 4 % 2 - d // 4 % 2, r // 2 % 2 - d // 2 % 2, r % 2 - d % 2)
    return all(agc >= 0 for agc in anti_gen_comp)


def _check_convert_input(inpval):
    """ Checks onput data type and value,
        if necessary and possible it converts it to Bloodtype.
        Arg:
        inpval (int | str | Bloodtype)
        Returns:
        (Bloodtype): converted (if needed) impval
    """
    if isinstance(inpval, Bloodtype):
        return inpval
    if isinstance(inpval, int):
        if 0 <= inpval <= 7:
            return Bloodtype(inpval)
        else:
            raise ValueError
    if isinstance(inpval, str):
        if inpval in blood_type_text.keys():
            return blood_type_text[inpval]
        else:
            raise ValueError
    else:
        raise TypeError    
        
#%% Day 36 Bite 136: Testing Cases

import pytest
#from bt import check_bt, Bloodtype


def test_universal_donor():
    donor = Bloodtype.ZERO_NEG
    for i in range(8):
        recipient = Bloodtype(i)
        assert check_bt(donor, recipient)


def test_universal_recipient():
    recipient = Bloodtype.AB_POS
    for i in range(8):
        donor = Bloodtype(i)
        assert check_bt(donor, recipient)


def test_AB_POS_can_donate_to_own_group_only_numeric_input():
    donor = 7
    for i in range(7):
        recipient = i
        assert check_bt(donor, recipient) is False


def test_ZERO_NEG_can_recieve_from_own_group_only_numeric_input():
    recipient = 0
    for i in range(1, 8):
        donor = i
        assert check_bt(donor, recipient) is False


def test_red_blood_cell_compatibility():
    assert check_bt(Bloodtype.A_NEG, Bloodtype.A_NEG)  # own
    assert check_bt(Bloodtype.B_NEG, Bloodtype.B_POS)
    assert check_bt(Bloodtype.A_NEG, Bloodtype.AB_NEG)


def test_red_blood_cell_incompatibility():
    assert check_bt(Bloodtype.B_POS, Bloodtype.B_NEG) is False
    assert check_bt(Bloodtype.A_NEG, Bloodtype.B_NEG) is False
    assert check_bt(Bloodtype.AB_NEG, Bloodtype.B_POS) is False
    assert check_bt(Bloodtype.B_NEG, Bloodtype.A_POS) is False


def test_red_blood_cell_compatibility_text_input():
    assert check_bt("0+", "A+")
    assert check_bt("0+", "B+")
    assert check_bt("B-", "B+")
    assert check_bt("A-", "AB-")


def test_red_blood_cell_incompatibility_text_input():
    assert check_bt("0+", "A-") is False
    assert check_bt("0+", "B-") is False
    assert check_bt("B-", "0-") is False
    assert check_bt("AB-", "A+") is False


def test_invalid_value_text_input():
    with pytest.raises(ValueError):
        check_bt("X-", "Y+")
    with pytest.raises(ValueError):
        check_bt("0", "A+")


def test_invalid_value_numeric_input():
    with pytest.raises(ValueError):
        check_bt(8, 1)
    with pytest.raises(ValueError):
        check_bt(3, -1)


def test_invalid_type():
    with pytest.raises(TypeError):
        check_bt(1.0, 1)
    with pytest.raises(TypeError):
        check_bt(3, ["AB", "Rh+"])    


