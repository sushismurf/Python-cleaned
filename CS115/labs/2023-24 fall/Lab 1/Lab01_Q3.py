#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 16:25:05 2023

"""

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 60 * SECONDS_IN_MINUTE
SECONDS_IN_DAY = 24 * SECONDS_IN_HOUR

seconds = int(input("Enter number of seconds: "))

if seconds <= 0:
    print("The number of seconds must be positive.")
else:
    if seconds < SECONDS_IN_MINUTE:
        print(f'{seconds} secs')
    elif seconds < SECONDS_IN_HOUR:
        minutes = seconds // SECONDS_IN_MINUTE
        seconds = seconds % SECONDS_IN_MINUTE
        print(f'{minutes} mins {seconds} secs')
    elif seconds < SECONDS_IN_DAY:
        hours = seconds // SECONDS_IN_HOUR
        minutes = (seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
        seconds = (seconds % SECONDS_IN_HOUR) % SECONDS_IN_MINUTE
        print(f'{hours} hours {minutes} mins {seconds} secs')
    else:
        days = seconds // SECONDS_IN_DAY
        hours = (seconds % SECONDS_IN_DAY) // SECONDS_IN_HOUR
        minutes = ((seconds % SECONDS_IN_DAY) % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
        seconds = ((seconds % SECONDS_IN_DAY) % SECONDS_IN_HOUR) % SECONDS_IN_MINUTE
        print(f'{days} days {hours} hours {minutes} mins {seconds} secs')
