"""
Author: Cray-sh
Date: 2023.02.06

This is problem 4, the final problem, for the course. 
Again, I will use several blocks to organize all of the pieces of this project before
putting them together in a more organized problem4_final.py

Problem Description:
Automate the resizing/formatting of photos, search through a variety of descriptions, use those two 
to post to a website, then summarize that info in a pdf, have that pdf sent via email, and finally
create a script to monitor the health of the system doing all of this to send an email if it's unhappy
"""
#shebang to be used in linux environments will be below here
#!/usr/bin/env python3

#%% Block 1 - this would be used to create createImage.py, and is becoming a scratch space

#modules/libraries to import

import os
import sys
import shutil
import psutil
from PIL import Image

path_for_linux = '//home//student-04-6808baa0231a//supplier-data//images//'

#%% Block 1b - This is createImage.py
"""
Pretty much the same design as problem1, but tweaked a little,
they wanted 600x400 and to make sure to convert to RGB first
This is exactly createImage.py
"""
#!/usr/bin/env python3


from PIL import Image
import os
import sys

basepath = "//home//student-04-6808baa0231a//supplier-data//images//"
new_path = basepath
new_ext = ".jpeg"

for entry in os.listdir(basepath):
 if os.path.isfile(os.path.join(basepath,entry)):
  fi,ext = os.path.splitext(entry)
  output_file = fi
  try:
   with Image.open(basepath + entry) as start_image:
    start_image_part1 = start_image.convert('RGB')
    start_image_complete = start_image_part1.resize((600,400)).save(new_path+output_file+new_ext,'JPEG')
  except OSError:
   print("Could not convert {}".format(output_file))


#%% Block 2 - This will be used to upload the converted pictures, below is the example they used
#which will need to be adjusted to use them

#!/usr/bin/env python3

import requests
#This example shows how a file can be uploaded using the python requests module
url = "http://localhost/upload"
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})

#%% Block 2b - Modified to use in our scenario, on linux vm

#This is the exact supplier_image_upload.py that was used in the lab

#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
#don't forget that slash at the end of upload!
path_of_pics = ""

for photo in os.listdir(path_of_pics):
    if photo.endswith('.jpeg'):
        with open(path_of_pics + photo, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
            print(r.status_code)
    
    else:
        print("{} was not a jpeg and therefore not uploaded".format(photo))



#%% Block 3 - A script to convert text files to JSON files to be uploaded to fruits
# This is run.py

"""Example Json Object to upload

{"name": "Watermelon",
 "weight": 500,
 "description": "Watermelon is good for relieving heat,
 eliminating annoyance and quenching thirst. It contains a lot of water,
 which is good for relieving the symptoms of acute fever immediately.
 The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation.
 Watermelon also contains substances that can lower blood pressure.",
 "image_name": "010.jpeg"}

"""
#!/usr/bin/env python3

import requests
import os
import json
import regex as re
"""
Line 1 will be name, Line 2 will be weight, Line 3 will be description
Four fields necessary:
-name (L1)
-weight (L2)
-description (L3)
-image_name - will be image that you want with this data
"""
#sets the location of text files and the url, then creates a list of files in location
text_file_location = "~/supplier-data/descriptions/"
url = "http://34.68.221.63/fruits/"
list_of_files = os.listdir(text_file_location)

#now for each file in that list, open it and read it's content to a dict, then
#send dict to json.dumps, send json to url as a post and only notify when not ok
for file in list_of_files:
    if file.endswith('.txt'):
        try:
            with open(text_file_location + file) as reg_file:
                p_dict = {}
#I'm running into a problem, sometimes the file has extra blank lines!
#old                name, weight, desc = reg_file.readlines()
#new is below... this is a cheap way to do it, a better way most likely exists
                name = reg_file.readline().strip('\n')
                weight = reg_file.readline().strip('\n')
                desc = reg_file.readline().strip('\n')

#this should be a little trick to separate the extension
#the document warns that "weight" needs to be an integer, so a re.match was done to only match
#the number portion of the weight and then converted to integer
                fi, ext = file.split('.')
                image_name = fi + '.jpeg'
                pattern = "[0-9]+"
                transform_weight = re.match(pattern,weight)
                calc_weight = int(transform_weight[0])
                p_dict["name"] = name
                p_dict["weight"] = calc_weight
                p_dict["description"] = desc
                p_dict["image_name"] = image_name
#dump to json, post to url, response only if not ok aka http 201            
                p_dict_json = json.dumps(p_dict)
                response = requests.post(url, json=p_dict_json)
#if above doesn't work try below
#                response = requests.post(url,data=p_dict)
                if response.status_code != '201':
                    print(response.status_code)
        except ValueError:
            print("something is wrong with {}".format(file))



#%% Block 4A - Generate PDF Report
#This will become reports.py
"""
Using the descriptions found in ~/supplier-data/descriptions/ create a pdf summarizing that data

pdf format:
    Processed Update on <Today's date>  <------- use a module to put in the date, also in bold
    [blank line]
    Name: Fruit One
    Weight: x00 lbs
    [blank line]
    Name: Fruit Two
    Weight: y00 lbs
    [blank line]
    ....repeat through all fruit found....


It wants this to be called reports.py and be generalized to a function generate_report 
which will take (attachment, title, paragraph)
the name of the pdf should be processed.pdf
"""

#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

def generate_report(attachment, title, info):
    """This creates a report at attachment using title as a title ["h1"], a blank_space 18 units
    high to separate, and as much info that is there in ["Normal"]
    """
    report = SimpleDocTemplate(attachment)
    form_title = Paragraph(title, styles['h1'])
    blank_space = Spacer(1,18)
    form_paragraph = Paragraph(info, styles['Normal'])
    report.build([form_title, blank_space, form_paragraph])

#%% Block 4B - Create and Send Report Email
#This will become report_email.py
#REMEMBER: Set username to your username

#!/usr/bin/env python3

import os
import datetime
import reports
import emails

username = 'student-04-6808baa0231a'

def process_data(text_file_location):
    paragraph = []
    list_of_files = os.listdir(text_file_location)
    for file in list_of_files:
        if file.endswith('.txt'):
            with open(text_file_location + file) as reg_file:
                name = reg_file.readline()
                weight = reg_file.readline()
#had to switch to <br/>, use those when dealing in the pdf, use the other in python
                new_line = "name: {}<br/>weight: {}<br/>".format(name,weight)
                paragraph.append(new_line)
    return paragraph
    
if __name__ == "__main__":
    paragraph_in_question = process_data("~/supplier-data/descriptions/")
#below gets the current time and converts it to usr/local date either MM/DD/YYYY or DD/MM/YYYY     
    attachment = "/tmp/processed.pdf"
    today_date = datetime.datetime.now().strftime('%x')
    
    title = "Processed Update on {}\n".format(today_date)
    
    
    
    superparagraph = "<br/><br/>".join(paragraph_in_question)
    reports.generate_report(attachment, title, superparagraph)
    
    subject = "Upload Completed - Online Fruit Store"
    sender = "automation@example.com"
    recipient = "{}@example.com".format(username)
    body = "All Fruits are uploaded to our website successfully. A detailed list is attached to this email."
    
    message = emails.generate_email(sender,recipient,subject,body,attachment)
    emails.send_email(message)



#%% Block 4C - emails.py
#This will become emails.py, we are separating into several modules
#This should be complete
#A lot of this is grabbed from P3
#!/usr/bin/env python3

from email.message import EmailMessage
import os.path
import mimetypes
import smtplib

def generate_email(sender,recipient,subject,body,attachment):
    """Creates an Email message to be sent with send_email, requires:
        sender = sender email
        recipient = recipient email
        subject = subject of email
        body = body of email
        attachment = path of attachment
    """
    
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    
    attach_filename = os.path.basename(attachment)
    mime_type, _ = mimetypes.guess_type(attachment)
    mime_type,mime_subtype = mime_type.split('/',1)
    
    with open(attachment, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attach_filename)
    return message


def send_email(message):
    """Given message is message from generate_email and is organized according to it, this
    will send the message as an email over a SMTP server ran on the localhost
    """
    smtp_site = smtplib.SMTP('localhost')
    smtp_site.set_debuglevel(1)
    smtp_site.send_message(message)
    smtp_site.quit()

def generate_error_email(sender,recipient,subject,body):
    """Creates an Email message when an error occurs to be sent with send_email, requires:
        sender = sender email
        recipient = recipient email
        subject = subject of email
        body = body of email
    """  
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    
    return message




#%% Block 5 - Healthcheck.py

#!/usr/bin/env python3
"""
This needs to check the running computer for a few things:
    1. Report Error if cpu usage is over 80%
    2. Report Error if available disk space is lower than 20%
    3. Report Error if available memory is less than 500MB
    4. Report an error if the hostname "localhost" cannot be resolved to 127.0.0.1
If an error is raised, it will need to send an email with following info:
    1. From: automation@example.com
    2. To: username@example.com replace username with username given in connection details on coursera
    3. Subject Line: Should vary depending on error:
        a. If CPU over 80% , subj_line = Error - CPU usage is over 80%
        b. If Disk Space Low, subj_line = Error - Available disk space is less than 20%
        c. If available memory is low, subj_line = Error - Available memory is less than 500MB
        d. If hostname problem, subj_line = Error - localhost cannot be resolved to 127.0.0.1
    4. Body: Please check your system and resolve the issue as soon as possible.

This can then be added as a crontab and executed every minute
* * * * * <path of program> 
above is the line you need for it to execute every minute
"""
import psutil
import shutil
import emails
import socket

#do a buncha checks
total_flags = ""
cpu_flag = ""
disk_flag = ""
mem_flag = ""
net_flag = ""

if psutil.cpu_percent() > 80:
    cpu_flag = "Error - CPU usage is over 80%"
    total_flags = total_flags + ', ' + cpu_flag
    
if shutil.disk_usage('/').free / shutil.disk_usage('/').total < 0.20:
    disk_flag = "Error - Available disk space is less than 20%"
    total_flags = total_flags + ', ' + disk_flag

if psutil.virtual_memory()[4]/1000000 < 500:
    mem_flag = "Error - Available memory is less than 500MB"
    total_flags = total_flags + ', ' + mem_flag

if socket.gethostbyname('localhost') != '127.0.0.1':
    net_flag = "Error - localhost cannot be resolved to 127.0.0.1"
    total_flags = total_flags + ', ' + net_flag

#which checks failed? Make note of those.
subject_line = total_flags
body_to_send_if_bad_stuff_happening = "Please check your system and resolve the issue as soon as possible."

#create email to send

sender = "automation@example.com"
recipient = "student-04-6808baa0231a@example.com"

if total_flags != "":
    emails.generate_error_email(sender,recipient,subject_line,body_to_send_if_bad_stuff_happening)
    









