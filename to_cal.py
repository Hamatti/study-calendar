#coding=utf-8
#! /usr/bin/python

# 2. periodin opintojen csv-tiedoston luominen Google-kalenteria varten
# Juha-Matti Santala

import datetime, time
import csv

# Google-kalenteri vaatii tietynlaisesti nimetyt otsikot
HEADER = "Subject,Start Date,Start Time,End Date,End Time".split(',')


CSVFILE = "opinnot.csv"
INFILE = "opinnot_raw.csv"
writer = csv.writer(open(CSVFILE, 'w'))
infile_reader = csv.reader(open(INFILE).readlines()[1:])


# Google-kalenteri tykkää tästä formaatista päivämäärille<
DAYFORMAT = "%m/%d/%Y"

# Luetaan sisään kurssi-informaatio
courses = [course for course in infile_reader]

# Kirjoitetaan otsikot
writer.writerow(HEADER)

# Laajennetaan kurssit kattamaan koko väli START_DATE - END_DATE
for course in courses:
    subject = course[0]
    start_date = datetime.datetime.strptime(course[1], DAYFORMAT)
    end_date = datetime.datetime.strptime(course[2], DAYFORMAT)
    start_time = course[3]
    # Luennon päättymisaika 2h luennon alkamisen jälkeen. Mikäli luento alkaa
    # ennen klo 10, on päättymisaika AM, muuten PM
    if int(start_time[:2]) < 10:
        end_time = "%d:00 AM" % (int(start_time[:2])+2)
    else:
        end_time = "%d:00 PM" % (int(start_time[:2]) + 2)

    # Luodaan tapahtumia päättymispäivään asti
    moving_date = start_date
    while moving_date <= end_date:
        print_date = moving_date.strftime(DAYFORMAT)
        writer.writerow([subject, print_date, start_time, print_date, end_time])
        # Luento toistuu viikon välein
        moving_date = moving_date + datetime.timedelta(days=7)


