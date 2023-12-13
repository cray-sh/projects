# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 19:40:07 2023

@author: cray-sh

Pybites challenges in python Week One: Day 37 thru Day 43
"""
#%% Day 37 Bite 143: Look up a value in 3 dictionaries
'''
In this Bite you are presented with 3 dictionaries. 
Complete get_person_age that takes a name as argument 
and returns the age if in any of the 3 dictionaries. 

The lookup should be case insensitive, so tim, Tim and tiM should all yield 30. 
If not in any of the dictionaries, return Not found.

Note that some persons are in 2 of the 3 dictionaries. 
In that case return the age of the last dictionaries 
(so group3 takes precedence over group2 and group2 takes precedence over group1).
 Check out the standard library ... :) - have fun!
'''
NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}

#Fastest - BUT this might change when the groups get very large
def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    age = NOT_FOUND
    if type(name) == str:  
        name = name.lower()
    else:
        return age
    if name in group1:
        age = group1[name]
    if name in group2:
        age = group2[name]
    if name in group3:
        age = group3[name]
    return age

#Third Fastest
def get_person_age_eff1(name):
    '''The more efficient version of get_person_age'''

#NOTE: You can use the pipes to fuse dictionaries together as well

    group = group1 | group2 | group3
    if type(name) == str:
        name = name.lower()
        if name in group:
            return group[name]
        else:
            return NOT_FOUND
    else:
        return NOT_FOUND
    
#second fastest
def get_person_age_eff2(name):
    '''The more efficient version of get_person_age'''

#NOTE: So what is weird is that if one would print or try and return group below it will return a Nonetype
#I used it as a temporary variable that updates... wait can I just get rid of that variable and have two
#updates?
#UPDATE: Yeah you totally can, I just ditched the temp variable we don't need it

    group1.update(group2)
    group1.update(group3)
    if type(name) == str:
        name = name.lower()
        if name in group1:
            return group1[name]
        else:
            return NOT_FOUND
    else:
        return NOT_FOUND

#%% Day 37 Bite 143: Their Solution

#So this is cool and all and probably does better memory wise but takes twice to four times as long??

from collections import ChainMap

NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age_theirs(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    name = name.lower() if isinstance(name, str) else name
    # search goes in order of addition so as per requirements
    # we insert groups from gt (#3) to lt (#1)

#NOTE: This chainmap object is a new concept, this was another solution to the problem
#that is created by having three dictionairies and wanting to put theminto one but will
#have that priority that the first group passed will be checked first and supercedes the following groups   
    
    m = ChainMap(group3, group2, group1)
    return m.get(name, NOT_FOUND)


#%% Day 37 Bite 143: Testing Cases
#from merge import get_person_age, NOT_FOUND


def test_regular_name():
    assert get_person_age('tim') == 30
    assert get_person_age('helen') == 26
    assert get_person_age('otto') == 44


def test_case_insensitive_lookup():
    assert get_person_age('Tim') == 30
    assert get_person_age('BOB') == 17
    assert get_person_age('BrEnDa') == 17


def test_name_not_found():
    assert get_person_age('timothy') == NOT_FOUND
    assert get_person_age(None) == NOT_FOUND
    assert get_person_age(False) == NOT_FOUND
    assert get_person_age(-1) == NOT_FOUND


def test_duplicate_name():
    assert get_person_age('thomas') == 46
    assert get_person_age('ana') == 26

#%% Day 38 Bite 153: Round a Sequence of Numbers
'''
It's time to get mathematical! In this Bite we ask that you complete the round_up_or_down function that receives a transactions list of floats and an optional up argument.

If up is True (default) you round them up to the nearest full integer, if it is False, you round down to the nearest full integer. Return a new list with the rounded int values.

Use whatever method you see fit, good luck!
'''
def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    new_list = []
    for value in transactions:
        roundma = value % (int(value))
        if roundma > 0:
            if up == True:
                new_list.append(int(value) + 1)
            else:
                new_list.append(int(value))
        elif roundma < 0:
            if up == True:
                new_list.append(int(value))
            else:
                new_list.append(int(value) - 1)
    return new_list

#%% Day 38 Bite 153: Their Solution
import math

def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    func = math.ceil if up else math.floor
    return [func(t) for t in transactions]

#%% Day 38 Bite 153: Testing Cases
import pytest

#from rounding import round_up_or_down

transactions1 = [2.05, 3.55, 4.50, 10.76, 100.25]
transactions2 = [1.55, 9.17, 5.67, 6.77, 2.33]
transactions_including_negatives = transactions2 + [-2.05]


@pytest.mark.parametrize("transactions, up_arg, expected", [
    (transactions1, True, [3, 4, 5, 11, 101]),
    (transactions1, False, [2, 3, 4, 10, 100]),
    (transactions2, True, [2, 10, 6, 7, 3]),
    (transactions2, False, [1, 9, 5, 6, 2]),
    (transactions_including_negatives, False, [1, 9, 5, 6, 2, -3]),
])
def test_round_up_or_down(transactions, up_arg, expected):
    assert round_up_or_down(transactions, up=up_arg) == expected
    
#%% Day 39 Bite 161: Count the number of files and Directories
'''
Complete count_dirs_and_files traversing the passed in directory path.

Return a tuple of (number_of_directories, number_of_files)

Let's use the tree command to show an example:
'''

import os

def count_dirs_and_files(directory = '.'):
    ''' Count the amount of directories and files passed in the directory argument.
        return a tuple (number_of_directories, number_of_files)
    '''
    count_dirs, count_files = 0, 0
    for root, directs, files in os.walk(directory):
        count_dirs += len(directs)
        count_files += len(files)
    return (count_dirs, count_files)
        
#Below was experimenting with some of the isdir and isfile, but was unnecessary.
#I had trouble with t his at first because it would count the root ontop of the directories
#and only count up by one if there was a file in the directory regardless of how many files were in there.
''' Playing around
test_loc = 'C:/Users/ADP55/Desktop/test_direct'
num_dir, num_file = 0, 0
for item in os.walk(test_loc):
    if os.path.isdir(item[0]):
        print('directory')
        num_dir += 1
    elif os.path.isfile(item[0] + item[2][0]):
        print('file')
    num_file += 1
print((num_dir, num_file))

'''
#%% Day 39 Bite 161: Testing Cases

#from tree import count_dirs_and_files


def test_only_files(tmp_path):
    for i in range(1, 6):
        path = tmp_path / f'{i}.txt'
        with open(path, 'w') as f:
            f.write('hello')
    assert count_dirs_and_files(tmp_path) == (0, 5)


def test_only_dirs(tmp_path):
    for i in range(5):
        (tmp_path / str(i)).mkdir()
    assert count_dirs_and_files(tmp_path) == (5, 0)


def test_files_and_dirs(tmp_path):
    for i in range(10):
        if i % 2 == 0:
            target_dir = tmp_path / str(i)
            target_dir.mkdir()
            for j in range(5):
                path = target_dir / f'{j}.txt'
                with open(path, 'w') as f:
                    f.write('hello')
    assert count_dirs_and_files(tmp_path) == (5, 25)

#%% Day 40 Bite 165: Parse an /etc/passwd file output
'''
The /etc/passwd file is a text-based database of information about users that may log into the system or other operating system user identities that own running processes. (Wikipedia).

In this Bite you complete the function get_users_for_shell that takes a /etc/passwd multiline string 
and a shell to filter on (default bash). 
Parse the output returning a list of usernames that match the shell.

So for this truncated /etc/passwd string:

avahi:x:107:108:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
postfix:x:108:112::/var/spool/postfix:/bin/false
ssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash
artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash"""
... the resulting user list would be: ['artagnon', 'ssh-rsa']

Good luck and keep calm and code in Python!

'''
from typing import List

DEFAULT_SHELL = 'bash'
# https://github.com/avar/git-anyonecanedit-etc/blob/master/passwd
PASSWD_OUTPUT = """root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
Debian-exim:x:101:103::/var/spool/exim4:/bin/false
statd:x:102:65534::/var/lib/nfs:/bin/false
sshd:x:103:65534::/var/run/sshd:/usr/sbin/nologin
ftp:x:104:65534::/home/ftp:/bin/false
messagebus:x:105:106::/var/run/dbus:/bin/false
mysql:x:106:107:MySQL Server,,,:/var/lib/mysql:/bin/false
avar:x:1000:1000::/home/avar:/bin/bash
chad:x:1001:1001::/home/chad:/bin/bash
git-svn-mirror:x:1002:1002:Git mirror,,,:/home/git-svn-mirror:/bin/bash
gerrit2:x:1003:1003:Gerrit User,,,:/home/gerrit2:/bin/bash
avahi:x:107:108:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
postfix:x:108:112::/var/spool/postfix:/bin/false
ssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash
artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash"""

#NOTE: The grep_shell is the last value in these strings, i.e. bash -> ends with /bash

#I feel pretty good about this one, I was able to do a really tight and neat list comprehension
#definitely understanding them more and more
#also somehow my solution was neater and more efficient than their solution this time.
def get_users_for_shell(passwd_output: str = PASSWD_OUTPUT,
                        grep_shell: str = DEFAULT_SHELL) -> List[str]:
    """Match the passwd_output string for users with grep_shell.
       Return a list of users.
    """
    list_of_strings = passwd_output.split('\n')
    return [line.split(':')[0] for line in list_of_strings if line.endswith('/' + grep_shell)]
#%% Day 40 Bite 165: Testing Cases

#from passwd import get_users_for_shell

# https://www.ibm.com/support/knowledgecenter/en/ssw_aix_72/com.ibm.aix.security/passwords_etc_passwd_file.htm
OTHER_PASSWD_OUTPUT = """root:!:0:0::/:/usr/bin/ksh
daemon:!:1:1::/etc:
bin:!:2:2::/bin:
sys:!:3:3::/usr/sys:
adm:!:4:4::/var/adm:
uucp:!:5:5::/usr/lib/uucp:
guest:!:100:100::/home/guest:
nobody:!:4294967294:4294967294::/:
lpd:!:9:4294967294::/:
lp:*:11:11::/var/spool/lp:/bin/false
invscout:*:200:1::/var/adm/invscout:/usr/bin/ksh
nuucp:*:6:5:uucp login user:/var/spool/uucppublic:/usr/sbin/uucp/uucico
paul:!:201:1::/home/paul:/usr/bin/ksh
jdoe:*:202:1:John Doe:/home/jdoe:/usr/bin/ksh"""


def test_get_users_for_shell_default_args():
    actual = get_users_for_shell()
    expected = ['artagnon', 'avar', 'chad', 'gerrit2',
                'git-svn-mirror', 'root', 'ssh-rsa']
    assert sorted(actual) == expected


def test_get_users_for_sh_shell():
    actual = get_users_for_shell(grep_shell='sh')
    expected = ['backup', 'bin', 'daemon', 'games', 'gnats', 'irc',
                'libuuid', 'list', 'lp', 'mail', 'man', 'news',
                'nobody', 'proxy', 'sys', 'uucp', 'www-data']
    assert sorted(actual) == expected


def test_get_users_for_false_shell():
    actual = get_users_for_shell(grep_shell='false')
    expected = ['Debian-exim', 'avahi', 'ftp', 'messagebus',
                'mysql', 'postfix', 'statd']
    assert sorted(actual) == expected


def test_get_users_for_different_passwd_output_and_ksh_shell():
    actual = get_users_for_shell(passwd_output=OTHER_PASSWD_OUTPUT,
                                 grep_shell='ksh')
    expected = ['invscout', 'jdoe', 'paul', 'root']
    assert sorted(actual) == expected
    
#%% Day 41 Bite 167: Complete a User class: properties and representation dunder methods
'''
In this Bite you are presented with another class, User this time.

Like last Bite you are asked to complete it, see the TODOs in the code below:

Complete the get_full_name property (more on properties here) that prints first and last name 
separated by a space.

Complete the username property following its docstring.

Complete the special representation dunder methods: __str__ and __repr__. 
Look at the tests what they should return. 
Brace yourself for some bonus learning for a twist we added in __repr__ 
(but as it's a Beginner Bite we give you a hint!)

Apart from Ned's awesome answer on SO, to give you an idea about the 
difference between __str__ and __repr__, check out how datetime implements them:

>>> from datetime import datetime
>>> dt = datetime.now()
>>> str(dt)
'2019-02-04 23:05:27.376407'
>>> repr(dt)
'datetime.datetime(2019, 2, 4, 23, 5, 27, 376407)'
Good luck and keep calm and code in Python!
'''
class User:
    """A User class
       (Django's User model inspired us)
    """

    def __init__(self, first_name, last_name):
        """Constructor, base values"""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def get_full_name(self):
        """Return first and last name separated by a whitespace
           and using title case for both.
        """
        # TODO 1: you code                                                      DONE
        return f'{self.first_name.title()} {self.last_name.title()}'

    @property
    def username(self):
        """A username consists of the first char of
           the user's first_name and the first 7 chars
           of the user's last_name, both lowercased.

           If this is your first property, check out:
           https://pybit.es/property-decorator.html
        """
        # TODO 2: you code                                                      DONE
        #turned this into one line for efficiency but originally had each part separately
        return self.first_name.lower()[0] + self.last_name.lower()[:7]


    # TODO 3: you code                                                          DONE
    #
    # add a __str__ and a __repr__
    # see: https://stackoverflow.com/a/1438297
    # "__repr__ is for devs, __str__ is for customers"
    #
    # see also TESTS for required output

    def __str__(self):
        return f'{self.get_full_name} ({self.username})'

#NEW: You can return the name of the class being used by chaining __class__ with __name__
#this is too avoid hardcoding the class name.
#This "for the devs" property added below returns a string representation of what was used to 
#create the object, so in this instance it will return User(firstnameused, lasatnameused)
    def __repr__(self):
        """Don't hardcode the class name, hint: use a
           special attribute of self.__class__ ...
        """
        return f'{self.__class__.__name__}("{self.first_name}", "{self.last_name}")'


#%% Day 41 Bite 167: Testing Cases
#from user import User


def test_bob_lowercase():
    bob = User("bob", "belderbos")
    assert bob.get_full_name == "Bob Belderbos"
    assert bob.username == "bbelderb"  # lowercase!
    assert str(bob) == "Bob Belderbos (bbelderb)"
    assert repr(bob) in [
        'User("bob", "belderbos")',
        "User('bob', 'belderbos')",
    ]


def test_julian_mixed_case():
    bob = User("julian", "Sequeira")
    assert bob.get_full_name == "Julian Sequeira"
    assert bob.username == "jsequeir"  # lowercase!
    assert str(bob) == "Julian Sequeira (jsequeir)"
    assert repr(bob) in [
        'User("julian", "Sequeira")',
        "User('julian', 'Sequeira')",
    ]


def test_tania_title_name():
    bob = User("Tania", "Courageous")
    assert bob.get_full_name == "Tania Courageous"  # aka PyBites Ninja
    assert bob.username == "tcourage"  # lowercase!
    assert str(bob) == "Tania Courageous (tcourage)"
    assert repr(bob) in [
        'User("Tania", "Courageous")',
        "User('Tania', 'Courageous')",
    ]


def test_noah_use_dunder_in_repr():
    """Make sure repr does not have the class
    name hardcoded.
    Also tests for a shorter surname.
    """

    class SpecialUser(User):
        pass

    noah = SpecialUser("Noah", "Kagan")
    assert noah.get_full_name == "Noah Kagan"
    assert noah.username == "nkagan"  # lowercase!
    assert str(noah) == "Noah Kagan (nkagan)"
    # it should show the subclass!
    assert repr(noah) in [
        'SpecialUser("Noah", "Kagan")',
        "SpecialUser('Noah', 'Kagan')",
    ]
#%% Day 42 Bite :
    
#%% Day 42 Bite : Testing Cases
    
#%% Day 43 Bite :
    
#%% Day 43 Bite : Testing Cases
