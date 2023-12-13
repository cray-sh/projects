"""
Author: Cray-sh
Date: 2023.01.25

This is problem 2 for course 6 of the python cert
I will try to keep the same format, several blocks that include cases/scenerios that slowly
ramp up in difficulty/complexity.

Problem Description:
Write a program/script that will convert a series of .txt files, which are customer reviews, into python dictionaires,
after which they will be uploaded to the website given (in django) to be seen. In other words,
input .txt reviews grab the info off of them and put them into a format that django will use to
upload to website.

"""
#shebang will be below here
#!/usr/bin/env python3

#%% Block 1: Simple Case
import json
path = "<abs path of single text file>"

with open(path) as file:
    
    name = file.name[-10:]
    
    name = {}
    
    
    a,b,c,d = file.readlines()
    
    name["title"] = a
    name["name"] = b
    name["date"] = c
    name["description"] = d

#will print the dictionary it created
    
    print(name)
    


#%% Block 2: Expanded - will now go through entire folder that you specify
import os
import requests

#path will be the location of the folder, list of files will iterate through each item in the folder

path = "<absolute path of folder>"

list_of_files = os.listdir(path)

#url will be the url that you are posting this info to

url = "<make sure you put the slashes in right>"

for element in list_of_files:
    
    complete_path = path + element
    
#construct full path that includes the file and then iterate through each file
    
    with open(complete_path) as file:
        
        postee = {}
        
#assigns the lines of the file to values and then injects them into postee a dictionary
       
        a,b,c,d = file.readlines()
        
        postee["title"] = a
        postee["name"] = b
        postee["date"] = c
        postee["feedback"] = d

#post the prepared dictionary to the url specified above
        
        response = requests.post(url, data=postee) 
        print(response)
        
#get a 201 and everything is okay, 500 check the syntax, and anything else check http docs
#IF YOU GET A 500 MAKE SURE TO CHECK THAT YOU PUT ALL THE SLASHES IN
#URL MUST END IN SLASH    
        








#%% Block 3: Linux version that first converts the dictionary to a json format and then uses that to post

#!/usr/bin/env python3

import os
import requests
import json


path = "<abs path of folder>"
url = "<url to post to, make sure it has all slashes>"
list_of_files = os.listdir(path)

for element in list_of_files:
 complete_path = path + element
 with open(complete_path) as file:
  postee = {}
  a,b,c,d = file.readlines()
  postee["title"] = a
  postee["name"] = b
  postee["date"] = c
  postee["feedback"] = d
  
#This step converts to json

  superpostee = json.dumps(postee)
  
#prints it for you to look at

  print(superpostee)
  
#posts, notice the change when using json files

  response = requests.post(url, json=superpostee)
  print(response.status_code)

#uncomment below to see more info about the post request

#  print(response.request.body)
#  print(response.request.url)

#%% Block 4:
    