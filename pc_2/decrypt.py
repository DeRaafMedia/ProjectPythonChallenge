#!/usr/bin/env python

# Fetch webpage

import urllib2

print ('')
print ('---------------->')

fetch = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
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
print ('Raw data from webpage (http://www.pythonchallenge.com/pc/def/ocr.html):')
print ('')
print data
print ('')
print ('---------------->')

## Statistics

print ('')
print ('Characters in data statistics:')
print ('')

characters_count = {}

for character in data:
    if character in characters_count:
        characters_count[character] = characters_count[character] + 1
    else:
        characters_count[character] = 1

total_characters = 0

for item in characters_count:

    if item == '\n':
        print 'A new linebreak has been counted ' + str(characters_count[item])
        total_characters = total_characters + characters_count[item]
    else:
        print 'The charcter ' + item + ' has been counted ' + str(characters_count[item])
        total_characters = total_characters + characters_count[item]

print ('')
print ('There are a total number of ' + str(total_characters) + ' characters in this data set.')

total_characters = 0

print ('')
print ('---------------->')

## Parsing solution

print ('')
print ('Cleaned up data (remove every character that appears more than twice):')
print ('')

solution = []

for character in data:
    if characters_count[character] <= 2:
        solution.append(character)

print ''.join(solution)

print ('')
print ('---------------->')

print ('')
