"""
Author: Cray-sh
Date: 2023.02.01

This is problem 3 for course 6 of the python cert
I will try to keep the same format, several blocks that include cases/scenerios that slowly
ramp up in difficulty/complexity.

Problem Description:
Using a JSON file that includes sales data, fill in the script as needed so that it accomplishes the following:
    1. Which car model had the most sales
    (hint says call format_car method for this)
    
    2. Calculate the most popular car_year across all make/models.
    (i.e. find how many cars were sold in each year and out of those which was the most)


This version is tailored straight for the project online
Most of this code is from them since this was a fill out style project
"""
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