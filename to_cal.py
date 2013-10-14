#coding=utf-8
#! /usr/bin/python
# Creating Google Calendar compatible CSV file to circumvene missing support
# for recurring events
# @author Juha-Matti Santala

import datetime
import csv

# Google Calendar requires certain names to identify columns
HEADER = "Subject,Start Date,Start Time,End Date,End Time".split(',')


CSVFILE = "opinnot.csv"
INFILE = "opinnot_raw.csv"
writer = csv.writer(open(CSVFILE, 'w'))
infile_reader = csv.reader(open(INFILE).readlines()[1:])

# The format for dates that Google Cal likes
DAYFORMAT = "%m/%d/%Y"

# Read in course information
courses = [course for course in infile_reader]

writer.writerow(HEADER)

for course in courses:
    subject = course[0]
    start_date = datetime.datetime.strptime(course[1], DAYFORMAT)
    end_date = datetime.datetime.strptime(course[2], DAYFORMAT)
    start_time = course[3]
    # Lectures end 2 hours after starting time.
    # If lecture starts before 10 am, ending time is also AM, otherwise PM
    if int(start_time[:2]) < 10:
        end_time = "%d:00 AM" % (int(start_time[:2])+2)
    else:
        end_time = "%d:00 PM" % (int(start_time[:2]) + 2)

    # Create an event for each week from starting date to ending date
    # (inclusive)
    moving_date = start_date
    while moving_date <= end_date:
        print_date = moving_date.strftime(DAYFORMAT)
        writer.writerow([subject, print_date, start_time, print_date, end_time])
        moving_date = moving_date + datetime.timedelta(days=7)


