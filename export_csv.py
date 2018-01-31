#this is a template for you to write a csv file

import csv

# create a file to open
# 'w' = write mode
# new line = blank
with open('name your csv file', 'w', newline = '') as fp:
    # create var
    a = csv.writer(fp, delimiter = ',')
    data = [['Name', 'Age'],
            ['Blair', '24'],
            ['Natalie', '33'],
            ['Annika', '5']]
    a.writerows(data)

# IMPORTANT THINGS TO NOTE:
# 1. do not save your csv files in Sublime Text as csv.py
# 2. make sure there are no csv.py files running in folder of execution
