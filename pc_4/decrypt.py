#!/usr/bin/env python

import urllib
import re
import time

print('')
print('-------------->')
print('')

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
ignore_nothing_text = "and the next nothing is (\d+)"
nothing_number = "12345"

## Fetch url's

opened_url_counter = 1

while True:
    try:
        ## At some point in the url chain there is a question instead of
        ## a following nothing number. The question is to divide the
        ## current nothing_number by 2. So this if else statement was
        ## necessary.
        if nothing_number == "16044":
            nothing_number = str(16044 / 2)
            data = urllib.urlopen(url % nothing_number).read()
        else:
            data = urllib.urlopen(url % nothing_number).read()

        nothing_number = re.search(ignore_nothing_text, data).group(1)

        opened_url_counter = opened_url_counter + 1
    except:
        break

    print ('Next url to open is: linkedlist.php?nothing=' + nothing_number)

## Statistics

print('')
print('-------------->')
print('')

print('Statistics: ')
print('')

print('The total number of "opened pages" : ' + str(opened_url_counter))


opened_url_counter = 1

## Parse solution

print('')
print('-------------->')
print('')

print('The solution is:')
print('')

print urllib.urlopen(url % nothing_number).read()

print('')
print('-------------->')
print('')
