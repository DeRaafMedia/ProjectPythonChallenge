#!/usr/bin/env python

import urllib2
import re

print ('')
print ('---------------->')

fetch = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
raw_html = fetch.read()

message_limiter_1 = '<!--'
message_limiter_2 = '-->'

raw_data = []

for item in raw_html.split(message_limiter_2):
    if message_limiter_1 in item:
        raw_data.append(item[item.find(message_limiter_1)+len(message_limiter_1) : ])

raw_data_index = len(raw_data) - 1

data = raw_data[raw_data_index].rstrip('\n')

## Raw data

print ('')
print ('Raw data from webpage (http://www.pythonchallenge.com/pc/def/equality.html):')
print ('')
print data
print ('')
print ('---------------->')

## Parsed data plus statistics

print ('')
print ('Parsed data and statistics:')
print ('')

#pattern = re.compile("[A-Z]{3}[a-z][A-Z]{3}")

pattern = re.compile('''
    [^A-Z]    # any character except a capital letter
    [A-Z]{3}  # three capital letters
    [a-z]     # one lowercase letter
    [A-Z]{3}  # three capital letters
    [^A-Z]    # any character except a capital letter
    ''', re.VERBOSE)

found_patterns = []

for item in pattern.findall(data):
    found_patterns.append(item)

print found_patterns

print ('')

print ('There are ' + str(len(found_patterns)) + ' patterns found that fit the criteria.')


print ('')
print ('Criteria being: "One small letter, surrounded by EXACTLY three big bodyguards on each of its sides."')

print ('')
print ('---------------->')

## Parsed solution

print ('')
print ('Parsed solution:')
print ('')

# Take note there are parentheses around ([a-z]). Only lowercase gets passed!
solution = re.compile('''[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]''', re.VERBOSE)

print ''.join(solution.findall(data))

print ('')
print ('---------------->')
print ('')
