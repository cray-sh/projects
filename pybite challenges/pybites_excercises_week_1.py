# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:20:21 2023

@author: cray-sh

Pybites challenges in python Week One: Day 1 thru Day 7
"""
#%% Day 1 Bite 1: Sum n numbers
'''
Write a Python function that calculates the sum of a list of numbers:

The function should accept a list of numbers and return the sum of those numbers.
If no argument is provided (that is, numbers is None), return the sum of the numbers 1 to 100 
(Note that this is not the same as an empty list of numbers being passed in. 
 In that case the sum returned will be 0).
''' 
def sum_numbers(numbers=None):
    if numbers == None:
        return sum(range(1,101))
    if numbers == []:
        return 0
    else:
        return sum(numbers)


#%% Day 1 Bite 1: Testing Cases

def test_sum_numbers_default_args():
    assert sum_numbers() == 5050
    assert sum_numbers(numbers=None) == 5050


def test_sum_numbers_various_inputs():
    assert sum_numbers(range(1, 11)) == 55
    assert sum_numbers([1, 2, 3]) == 6
    assert sum_numbers((1, 2, 3)) == 6
    assert sum_numbers([]) == 0  # !! [] not the same as None
    
test_sum_numbers_default_args()
test_sum_numbers_various_inputs()

#%% Day 2 Bite 5: Parse a list of names
'''
1. Write a function that accepts a list of names and title cases them
 and removes duplicates.

2. Next, sort the list in alphabetical descending order by surname.

3. Finally, find the shortest first name.

You can assume that the names in the list are single strings composed of two words:
    one given name and one surname.
'''    
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    title_list = []
    for item in names:
        title_name = item.title()
        if title_name not in title_list:
            title_list.append(title_name)
    return title_list


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names, key=lambda x: x.split()[1], reverse=True)


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    return sorted(names, key= lambda x: len(x.split()[0]))[0].split()[0]
    
    
#%% Day 2 Bite 5: Testing Cases  

PY_CONTENT_CREATORS = ['brian okken', 'michael kennedy', 'trey hunner',
                       'matt harrison', 'julian sequeira', 'dan bader',
                       'michael kennedy', 'brian okken', 'dan bader']


def test_dedup_and_title_case_names():
    names = dedup_and_title_case_names(NAMES)
    assert names.count('Bob Belderbos') == 1
    assert names.count('julian sequeira') == 0
    assert names.count('Brad Pitt') == 1
    assert len(names) == 10
    assert all(n.title() in names for n in NAMES)


def test_dedup_and_title_case_names_different_names_list():
    actual = sorted(dedup_and_title_case_names(PY_CONTENT_CREATORS))
    expected = ['Brian Okken', 'Dan Bader', 'Julian Sequeira',
                'Matt Harrison', 'Michael Kennedy', 'Trey Hunner']
    assert actual == expected


def test_sort_by_surname_desc():
    names = sort_by_surname_desc(NAMES)
    assert names[0] == 'Julian Sequeira'
    assert names[-1] == 'Alec Baldwin'


def test_sort_by_surname_desc_different_names_list():
    names = sort_by_surname_desc(PY_CONTENT_CREATORS)
    assert names[0] == 'Julian Sequeira'
    assert names[-1] == 'Dan Bader'


def test_shortest_first_name():
    assert shortest_first_name(NAMES) == 'Al'


def test_shortest_first_name_different_names_list():
    assert shortest_first_name(PY_CONTENT_CREATORS) == 'Dan'    
    
#%% Day 3 Bite 8: Rotate Names
'''
Write a function that rotates characters in a string in either direction:

- If n is positive, move n characters from beginning to end, 
 e.g.: rotate('hello', 2) would return "llohe".

- If n is negative, move the last n characters to the start of the string,
 e.g.: rotate('hello', -2) would return "lohel".

Take a look at the tests for more details. Have fun!
'''

'''
I was able to get elloh from hello with n = 1 using
word[n:] + word[:n]
I think this will work both ways too!
'''

def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    return string[n:] + string[:n]    
    
#%% Day 3 Bite 8: Testing cases
    
def test_small_rotate():
    assert rotate('hello', 2) == 'llohe'
    assert rotate('hello', -2) == 'lohel'


def test_bigger_rotation_of_positive_n():
    string = 'bob and julian love pybites!'
    expected = 'love pybites!bob and julian '
    assert rotate(string, 15) == expected


def test_bigger_rotation_of_negative_n():
    string = 'pybites loves julian and bob!'
    expected = 'julian and bob!pybites loves '
    assert rotate(string, -15) == expected


def test_rotation_of_n_same_as_len_str():
    string = expected = 'julian and bob!'
    assert rotate(string, len(string)) == expected


def test_rotation_of_n_bigger_than_string():
    """
    Why are there two expected results for this test?

    This Bite can be interpreted in two ways:

    1. A slice of size n moved from one end of the string to the other
    2. A continual rotation, character by character, n number of times

    Both interpretations result in identical output, except in the case
    where the rotation size exceeds the length of the string.

    Case 1) With a slice method, slicing an entire string and placing
    it at either the beginning or end of itself simply results in the
    the original string = expected_solution1

    Case 2) With a continual rotation, rotating the string len(string)
    number of times produces a string identical to the original string.
    This means any additional rotations can be considered equivalent to
    rotating the string by rotations % len(string) = expected_solution2
    """
    string = 'julian and bob!'
    expected_solution1 = 'julian and bob!'
    expected_solution2 = ' bob!julian and'
    assert rotate(string, 100) in (expected_solution1,
                                   expected_solution2)

    mod = 100 % len(string)  # 10
    assert rotate(string, mod) in (expected_solution1,
                                   expected_solution2)    
    
#%% Day 4 Bite 15: Enumerate 2 Sequences
'''    
Iterate over the given names and countries lists,
 printing them prepending the number of the loop (starting at 1).
 Here is the output you need to deliver:

1. Julian     Australia
2. Bob        Spain
3. PyBites    Global
4. Dante      Argentina
5. Martin     USA
6. Rodolfo    Mexico
Notice that the 2nd column should have a fixed width of 11 chars,
 so between Julian and Australia there are 5 spaces,
 between Bob and Spain, there are 8. 
 This column should also be aligned to the left.

Ideally you use only one for loop, but that is not a requirement. See this built-in :)

Good luck and keep calm and code in Python!    
    
'''    

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    output = ''
    list_of_zipped = list(zip(names, countries))
    numbered_list = list(enumerate(list_of_zipped,1))
    for item in numbered_list:
        number = item[0]
        name = item[1][0]
        country = item[1][1]
        output +='{}. {:11}{:<}\n'.format(str(number), name, country)
    return output

#their solution


#%% Day 4 Bite 15: Testing Cases    
    
from textwrap import dedent

expected_output = dedent(
    """\
    1. Julian     Australia
    2. Bob        Spain
    3. PyBites    Global
    4. Dante      Argentina
    5. Martin     USA
    6. Rodolfo    Mexico
"""
)


def test_enumerate_names_countries(capsys):
    enumerate_names_countries()
    output = capsys.readouterr().out
    assert output == expected_output    
       
#%% Day 5 Bite 16: Pybites Date Generator
'''
Write a generator that returns every 100th day counting forward from the PYBITES_BORN date.

Here is how the generator would work if you import and use it in your REPL:

>>> from itertools import islice
>>> from pprint import pprint as pp
>>> from gendates import gen_special_pybites_dates
>>> gen = gen_special_pybites_dates()
>>> pp(list(islice(gen, 5)))
[datetime.datetime(2017, 3, 29, 0, 0),
 datetime.datetime(2017, 7, 7, 0, 0),
 datetime.datetime(2017, 10, 15, 0, 0),
 datetime.datetime(2018, 1, 23, 0, 0),
 datetime.datetime(2018, 5, 3, 0, 0)]
'''


from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    '''Each generate will yield a date 100 days after PYBITES_BORN up to 100 generations'''
    for i in range(100):
        yield PYBITES_BORN + (i+1)*timedelta(days=100)

#note this passed all tests below! Generators work when you need to call a function more than once
#and also needs to get a previous state.

#%% Day 5 Bite 16: Testing Cases

from datetime import datetime
from itertools import islice

def test_gen_special_pybites_dates():
    gen = gen_special_pybites_dates()
    dates = list(islice(gen, 10))
    expected = [datetime(2017, 3, 29, 0, 0),
                datetime(2017, 7, 7, 0, 0),
                datetime(2017, 10, 15, 0, 0),
                datetime(2018, 1, 23, 0, 0),
                datetime(2018, 5, 3, 0, 0),
                datetime(2018, 8, 11, 0, 0),
                datetime(2018, 11, 19, 0, 0),
                datetime(2019, 2, 27, 0, 0),
                datetime(2019, 6, 7, 0, 0),
                datetime(2019, 9, 15, 0, 0)]
    assert dates == expected

#%% Day 6 Bite 19: Write a Property
'''
Write a simple Promo class. Its constructor receives two variables:
    name (which must be a string) 
    and 
    expires (which must be a datetime object).

Add a property called expired which returns a boolean value indicating 
whether the promo has expired or not.

Checkout the tests and datetime module for more info. Have fun!
'''

from datetime import datetime

#creates the moment we will be the spot everything is in refrence to
NOW = datetime.now()


class Promo:
    ''' Creates an object that contains the name of the promotion website,
    as well as the time it expires.
    Using .name will return the name given
          .expires will return when it will expire
          .expired will return if it has expired or not, True if expired.
    '''
    
    def __init__(self, name, expires):
#This defintes what the class arguements that will become the objects attributes
#note unlike functions where we place it in the name, during class defines it is in this

#this part was unneeded but it does a check that a string was the type of the first arg and datetime for second    
        if isinstance(name, str) == True:
            self.name = name
        if isinstance(expires, datetime) == True:
            self.expires = expires
#I believe this creates the function that we will use when calling the property        
    def expired(self):
         if self.expires >= NOW:
             return False
         else:
             return True
#and this is the line that gives this class and eventually it's object the property of expired         
    expired = property(fget = expired)    
#%% Day 6 Bite 19: Their Solution:
#I've decided to add another block here for their solution as it is more simple and faster to compare
#note the big difference is that they desided to use the @property decorador I read about wheras I used
#the function

from datetime import datetime

NOW = datetime.now()


class Promo:

    def __init__(self, name, expires=NOW):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        return datetime.now() > self.expires
#%% Day 6 Bite 19: Testing Cases - the last one will fail in spyder but not on their site
#it fails because we used property() instead of @property the decorator

from datetime import timedelta
import inspect

#from simple_property import Promo, NOW


def test_promo_expired():
    past_time = NOW - timedelta(seconds=3)
    twitter_promo = Promo('twitter', past_time)
    assert twitter_promo.expired


def test_promo_not_expired():
    future_date = NOW + timedelta(days=1)
    newsletter_promo = Promo('newsletter', future_date)
    assert not newsletter_promo.expired


def test_uses_property():
    assert 'property' in inspect.getsource(Promo)

#%% Day 7 Bite 21: Query a nested data structure
''' Prompt
Given the provided cars dictionary:

Get all Jeeps
Get the first car of every manufacturer.
Get all vehicles containing the string Trail in their names (should work for other grep too)
Sort the models (values) alphabetically
See the docstrings and tests for more details. Have fun!

Update 18th of Sept 2018: as concluded in the forum it is better to pass the cars dict into each function to make its scope local.

Update 9th of March 2022: doing this exercise again ourselves today, we concluded that adding type hints would be quite beneficial here so we added them.

'''

from typing import Dict, List


cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}
DEFAULT_SEARCH = "trail"
CarsType = Dict[str, List[str]]


def get_all_jeeps(cars: CarsType = cars) -> str:
    """
    Retrieve the 'Jeep' models from the cars dict and join them by a
    comma and space (', '). Leave the original ordering intact.
    """
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer(cars: CarsType = cars) -> List[str]:
    """
    Loop through the cars dict filtering out the first model for each
    manufacturer. Return the matching models in a list leaving the original
    ordering intact.
    """
    car_list = []
    for key in cars.keys():
        car_list.append(cars[key][0])
    return car_list


def get_all_matching_models(
    cars: CarsType = cars, grep: str = DEFAULT_SEARCH
) -> List[str]:
    """
    Return a list of all models containing the case insensitive
    'grep' string which defaults to DEFAULT_SEARCH ('trail').
    Sort the resulting sequence alphabetically
    """
#My plan was to create two lists, one list with all of the car makers on it and a second to return
#we were able to use a comparison 'in' instead of regex here
#make sure to get that .sort() in either a dot chain or in it's own line,I kept finding errors

    list_to_return = []
    list_of_all = []
    for car in cars.values():
        for ind_car in car:
            list_of_all.append(ind_car)
    for car in list_of_all:
        if grep.lower() in car.lower():
            list_to_return.append(car)
    list_to_return.sort()
    return list_to_return


def sort_car_models(cars: CarsType = cars) -> CarsType:
    """
    Loop through the cars dict returning a new dict with the
    same keys and the values sorted alphabetically.
    """
#get that separate .sort again
#also!!!! If you decided to use the testing cases make sure you do them in order because this changes
#cars and some of the tests want the original order
  
    
    for key in cars.keys():
        new_list = cars[key]
        new_list.sort()
        cars[key] = new_list
    return cars

#%% Day 7 Bite 21: Their Solution
#They went wild with list comprehension here, I got it to work but again at a slower more lengthy way

from itertools import chain
from typing import Dict, List

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}
DEFAULT_SEARCH = "trail"
CarsType = Dict[str, List[str]]


def get_all_jeeps(cars: CarsType = cars) -> str:
    """
    Retrieve the 'Jeep' models from the cars dict and join them by a
    comma and space (', '). Leave the original ordering intact.
    """
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer(cars: CarsType = cars) -> List[str]:
    """
    Loop through the cars dict filtering out the first model for each
    manufacturer. Return the matching models in a list leaving the original
    ordering intact.
    """
    return [models[0] for models in cars.values()]


def get_all_matching_models(
    cars: CarsType = cars, grep: str = DEFAULT_SEARCH
) -> List[str]:
    """
    Return a list of all models containing the case insensitive
    'grep' string which defaults to DEFAULT_SEARCH ('trail').
    Sort the resulting sequence alphabetically
    """
    grep = grep.lower()
    # flatten list of lists (less obvious way: "sum(cars.values(), [])")
    models = list(chain.from_iterable(cars.values()))
    matching_models = [model for model in models
                       if grep in model.lower()]
    return sorted(matching_models)


def sort_car_models(cars: CarsType = cars) -> CarsType:
    """
    Loop through the cars dict returning a new dict with the
    same keys and the values sorted alphabetically.
    """
    return {manufacturer: sorted(models) for
            manufacturer, models in cars.items()}


#%% Day 7 Bite 21: Testing Cases

''' only needed if testing cases is saved as a second script
from cars import (get_all_jeeps, get_first_model_each_manufacturer,
                  get_all_matching_models, sort_car_models)
'''

def test_get_all_jeeps():
    expected = 'Grand Cherokee, Cherokee, Trailhawk, Trackhawk'
    actual = get_all_jeeps()
    assert type(actual) == str
    assert actual == expected


def test_get_first_model_each_manufacturer():
    actual = get_first_model_each_manufacturer()
    expected = ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
    assert actual == expected


def test_get_all_matching_models_default_grep():
    expected = ['Trailblazer', 'Trailhawk']
    assert get_all_matching_models() == expected


def test_get_all_matching_models_different_grep():
    expected = ['Accord', 'Commodore', 'Falcon']
    assert get_all_matching_models(grep='CO') == expected


def test_sort_dict_alphabetically():
    actual = sort_car_models()
    # Order of keys should not matter, two dicts are equal if they have the
    # same keys and the same values.
    # The car models (values) need to be sorted here though
    expected = {
        'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
        'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
        'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
        'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk'],
        'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
    }
    assert actual == expected