"""
author: cray-sh
date: 2023.01.23

This file is the starting place for the first problem
Problem 1 has a lot to do with manipulating images and/or formating them
"""


#%% Block 2: Now I want to expand to be able to convert all photos in a directory/folder
#This will manipulate all pictures from basepath and save the conversions to new_path
from PIL import Image
import os


#base path is the folder the prephotos live, and new path is where the final location is
basepath = "/home/cray-sh/images/"
new_path = "/opt/icons/"
new_ext = ".jpeg"

#will first find which files are in the directory given, then will resize/convert/etc
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath,entry)):
        fi,ext = os.path.splitext(entry)
        output_file = fi
        try:
            with Image.open(basepath + entry) as start_image: 
                start_image_complete = start_image.resize((128,128)).rotate(90).convert('RGB').save(new_path+output_file,'JPEG')
        except OSError:
            print("Could not convert {}".format(output_file))
    