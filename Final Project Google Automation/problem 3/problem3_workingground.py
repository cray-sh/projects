"""
Author: Cray-sh
Date: 2023.01.28

This is problem 3 for course 6 of the python cert
I will try to keep the same format, several blocks that include cases/scenerios that slowly
ramp up in difficulty/complexity.

Problem Description:
Using a JSON file that includes sales data, fill in the script as needed so that it accomplishes the following:
    1. Which car model had the most sales
    (hint says call format_car method for this)
    
    2. Calculate the most popular car_year across all make/models.
    (i.e. find how many cars were sold in each year and out of those which was the most)

Using the conclusions found to 1 and 2, construct a PDF report that details this and send it to the given email/details
"""
#shebang will be below here
#!/usr/bin/env python3

#%% Block 1: simple example - Sending a message

#importing

from email.message import EmailMessage
import os.path
import mimetypes
import getpass
import smtplib

message = EmailMessage()

#setting email headers

sender = "me@example.com"
recipient = "you@example.com"
subject = "Example Email Subject"


message["From"] = sender
message["To"] = recipient
message["Subject"] = subject

#setting body of email

body = '''This is a body
            of an email that could be as
            long as you want it to be'''
            
message.set_content(body)

#Below will be setting up to attach a file

attach_path = "C:\\Users\\ADP55\\Desktop\\testfolder\\gobble.jpg"

#Below sets up a way for us to get the mimetype and subtype that will need to be set
#before we can send the message

attach_filename = os.path.basename(attach_path)

#I'm not sure why they recommend/use the underscore below when setting a variable

mime_type, _ = mimetypes.guess_type(attach_path)

#this is a little trick to redefine them quickly

mime_type,mime_subtype = mime_type.split('/',1)

#now we can finally attach the picture/file to the message
#notice we needed the path to open the file, then
#to attach we needed: read the file, maintype(which is mime_type), subtype(which is mime_subtype,
#and the filename

with open(attach_path, 'rb') as ap:
    
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=attach_filename)

#Adding a file will add a HUGE string when printing message, shorten it in oneway or another

#Below are the info to set for the smtp site for outgoing messages, and a password asker to use later

smtp_site = input("what is the smtp address to use")

mail_pass = getpass.getpass("password? ")

#now that we have that info we can open a server using the smtp site, setting debug to 1 is on to see
#debug info

mail_server = smtplib.SMTP_SSL(smtp_site)
mail_server.set_debuglevel(1)

#authenticates the connection using the username (email of sender) and password
#it will ouput a tuple that will have a status code and message

#Note!!! If this autentication fails it will raise a SMTPAuthenticationError exception, you'll need
#to figure out a way to handle those!

mail_server.login(sender, mail_pass)

#finally the message with attachments is sent via the smtp server and then closed upon completion

mail_server.send_message(message)
mail_server.quit()


#%% Block 2 - Generate PDF Simple Example

#I'm going to group all of the import lines together here
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image   #these are the flowables
from reportlab.lib.styles import getSampleStyleSheet                                #this is used for style references for text
from reportlab.lib import colors                                                    #this is used for advanced table design
from reportlab.graphics.shapes import Drawing                                       #this is used for drawing, along with Pie make Pie graphs
from reportlab.graphics.charts.piecharts import Pie                                 #this is used for Pie, along with drawing make Pie graphs
from reportlab.lib.units import inch, cm                                            #this is used for assigning the converted values for inch and cm


#below will be variables needed for later

table_data = []

#this is what creates the blank pdf to build on, you can even give it an abs path + name to be more specific
report = SimpleDocTemplate("C:\\Users\\ADP55\\Desktop\\Master Scripts\\testfolder\\Testreport.pdf")
styles = getSampleStyleSheet()

fruit = {
"elder" : 1,
"apples" : 2,
"strawb" : 4,
"pineap" : 4,
"durian" : 5,
"bluebur": 3
}

#Creating flowables/chunks:

#Text
report_title = Paragraph("This is an Inventory of Available Fruit", styles["h1"])

#Table conversion from dictionary, tables want a list of lists aka 2d array
for k,v in fruit.items():
    table_data.append([k,v])

#Basic Table
report_table = Table(data=table_data)

#Adv Table
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]

report_table2 = Table(data=table_data, style=table_style, hAlign="LEFT")

#Pie Graph
#creates a blank pie graph, needs data and labels
report_pie = Pie(width=3*inch, height=3*inch)

report_pie.data = []
report_pie.labels = []

#sorts data from dictionary fruit into separate lists for data and labels
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

#we need to first add a blank drawing (might be considered a flowable) then add our pie graph to it    
report_chart = Drawing()
report_chart.add(report_pie)

#Below here will be the build function that requires all flowables  passed to it in a list

report.build([report_title, report_table2, report_chart])


#%% Block 3 - Simple bring it all together Example
#This is a json example of how the data will be organized, I'm messing with it to see how it might work in the problem
car47 = {
        "id": 47,
        "car": {
                "car_make": "Lamborghini",
                "car_model": "Murciélago",
                "car_year": 2002
        },
        "price": "$13724.05",
        "total_sales": 149
}
print(car47['car']['car_year'])

total_sales_in_cash = float(car47['price'][1:]) * float(car47['total_sales'])
print("The {car_make} made a total of {total_sales_in_cash}".format(car_make=car47['car']['car_model'], total_sales_in_cash=total_sales_in_cash))

#This is the format function they use in process_data

def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(car["car_make"], car["car_model"], car["car_year"])

#%% Block 4 - Messing around with JSON

#Loads JSON
import json

filename = "C:\\Users\\ADP55\\Desktop\\Master Scripts\\Python-Cert-Final-Problems\\Problem 3\\car_sales.json"

def load_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data

#Below simulates one iteration of the for item in car_data loop

pop_years = {}

the_data = load_data(filename)
one_line = the_data[0]
nice_name = format_car(one_line["car"])
number_of_sales = one_line["total_sales"]

car_year = one_line["car"]["car_year"]
no_cars = one_line["total_sales"]

if car_year in pop_years.keys():
    pop_years[car_year] += no_cars
else:
    pop_years[car_year] = no_cars


print(one_line)
print("The {} sold a total of {} units.".format(nice_name,number_of_sales))

#%% Block 5 - Experimenting with Modules Given
#This is how they had it setup copying here for comparison later

reports.generate("/tmp/report.pdf", "A complete Inventory of my fruit","This is all my fruit", table_data)
#make the path above ^equal to the path below  \/


sender = "sender@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = ""
body = "Hi\n\nI'm sending an attachment with my fruit."
message = emails.generate(sender, receiver, subject, body, "/tmp/report.pdf")
emails.send(message)





#%% Block 6 - Shaping Final Code Customized for Problem
#This Code has been taken from Problem 3 "cars.py", the goal is to complete it

#!/usr/bin/env python3

import json
import locale
import sys
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from email.message import EmailMessage
import os.path
import mimetypes
import getpass
import smtplib
import emails
import os
import reports


#below needs to be the path of the car_sales.json file
datafile = "C:\\Users\\ADP55\\Desktop\\Master Scripts\\Python-Cert-Final-Problems\\Problem 3\\car_sales.json"

#below are fully finished functions used in main
def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data
        
def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(car["car_make"], car["car_model"], car["car_year"])

#The above must recieve only the car dictionary portion of the full dictionary or it will be :(


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
    return table_data
        
#Now here is where it get's interesting/is more filled out by me
def process_data(data):
    """Analyzes the data, looking for maximums.
    Will return a list of lines that summarize the information.
    """
    max_revenue = {"revenue" : 0}
    max_sales = 0
    max_make = ""
    pop_years = {}
    
    for item in data:
        item_price = locale.atof(item["price"].strip('$'))
        item_revenue = item["total_sales"] * item_price
        
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item
          
 
        if item["total_sales"] > max_sales:
            max_sales = item["total_sales"]
            max_make = format_car(item["car"])
        
        if item["car"]["car_year"] in pop_years.keys():
            pop_years[item["car"]["car_year"]] += item["total_sales"]
        else:
            pop_years[item["car"]["car_year"]] = item["total_sales"]
        
    most_pop_year = max(pop_years, key=pop_years.get)
    no_pop_year = max(pop_years.values())    
        
        
    summary = ["The {} generated the most revenue: ${}".format(format_car(max_revenue["car"]), max_revenue["revenue"]),
               "The {} had the most sales: {}".format(max_make, max_sales),
               "The most popular year was {} with {} sales.".format(most_pop_year, no_pop_year)]    
        
    return summary    

        
def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data(datafile)
    summary = process_data(data)
    
    supersummary = "{} <br/> {} <br/> {}".format(summary[0],summary[1],summary[2])
    the_table_data = cars_dict_to_table(data)
    
    reports.generate("/tmp/cars.pdf", "Sales summary for last month", supersummary, the_table_data)
    
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Sales summary for last month"
    body = "{}\n{}\n{}".format(summary[0], summary[1], summary[2])
    message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
    emails.send(message)
    

if __name__ == "__main__":
    main(sys.argv)

















