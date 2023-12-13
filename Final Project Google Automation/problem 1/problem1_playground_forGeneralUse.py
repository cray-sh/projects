"""
author: cray-sh
date: 2023.01.23

This file is the starting place for the first problem
Problem 1 has a lot to do with manipulating images and/or formating them
Specifically: This code will search the directory/folder given in basepath, manipulate by rotating 90 cw
resizing to 128 x 128, and change the format to jpeg. 
This will have a few examples from the module, then two scenarios broken into block 1 and 2
"""
#%% Example 1 from Module

#from PIL import Image
#im = Image.open(<file_here>)
#new_im = im.resize((640,480))
#new_im.save("example_resized.jpg")

#%% Example 2 from Module
#We can also use typical dot notation antics to chain commands

#from PIL import Image
#im = Image.open(<file_here>)
#im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")

#%% Block 1: One image Case: Will need to perform 4 operations; rotate(90), resize((128,128)), format change to .jpg, and save

##Uncomment single pound signs to get this to work

#from PIL import Image as Im
#import os
#import sys

#new_path = "<path of file you want to convert>"


##opens image at file location
#image0 = Im.open('<file to open>')

##resizes the image opened
#image1 = image0.resize((128,128))

##rotates the image by 90 degrees
#image2 = image1.rotate(90)

##formats from current format to .jpg

#image2_rgb = image2.convert('RGB')
#image2_rgb.save(new_path + '<file to open>')

##The above block 1 works to convert a single file that is given, manipulates as wanted, and then saves it under the jpeg format
##The inbetween convert step is placed just incase an image in RGBA is opened, as RGBA cannot be directly converted to jpeg without ditching the A


#%% Block 2: Now I want to expand to be able to convert all photos in a directory/folder
#This will manipulate all pictures from basepath and save the conversions to new_path
from PIL import Image
import os
import sys
import shutil

#base path is the folder the prephotos live, and new path is where the final location is
#note if using windows remember to slash the right direction, and escape slashes!
basepath = "<path of photos that need processed>"
new_path = "<path of where you want the photos to output to>"
new_ext = ".jpeg"

#I placed all conversions in one line for neatness, but could be separated for better readablility
#Try/Except is to catch hidden files and not images in the directory given since they'll mess it up.

for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath,entry)):
        fi,ext = os.path.splitext(entry)
        output_file = fi
        try:
            with Image.open(basepath + entry) as start_image:
                start_image_complete = start_image.resize((128,128)).rotate(90).convert('RGB').save(new_path+output_file+new_ext,'JPEG')
        except OSError:
            print("Could not convert {}".format(output_file))
