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
#my version that returned it in either a list with \n escapes or in a nicely formatted list
#I could not get it to pass and had to look at the solution which is below as well

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


#vs. 
#Their version
names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries2():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    for i, (name, country) in enumerate(zip(names, countries), 1):
        print(f"{i}. {name:<11}{country}")