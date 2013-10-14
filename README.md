study-calendar
==============

Small script to ease out with the problem of Google Calendar not supporting
recurring events with csv import.

In the *opinnot_raw.csv* file I have starting and ending date for each lecture
plus starting time of each lecture. The script then generates ending time (+2
hrs) and creates event for each lecture between start and end date (inclusive).

Example of input file is in repository and below:

> COURSE,STARTDATE,ENDDATE,STARTTIME

> MPKB,10/30/2013,12/18/2013,12:00 PM

*(All code comments are in Finnish)*
