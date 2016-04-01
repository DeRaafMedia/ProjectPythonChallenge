#!/usr/bin/env python

import pickle

## Unpickle banner.p
data = pickle.load(open( "banner.p", "rb" ))

print('')
print('------------------>')

## Raw data

print('')
print('Unpickeled raw data: ')
print('')

print data

print('')
print('------------------>')

## Parse data

print('')
print('Parsed data (solution?): ')
print('')

print('What is it?:')
print type(data)
print('')

'''
single_row = []
multiple_rows = []
counter = 0
for item in data:
    for list_item in item:
        if counter <= 95:
            for character in range(list_item[1]):
                single_row.append(list_item[0])
                multiple_rows.append(single_row)
        else:
            counter = 0
        single_row =[]
for item in multiple_rows:
    print item
'''

file = open("solution.txt", "w")

for item in data:

    print>>file, ''.join([character[1] * character[0] for character in item])

file.close()

print('Solution has been written to solution.txt')

print('')
print('------------------>')
print('')
