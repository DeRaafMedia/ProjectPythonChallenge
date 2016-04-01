#!/usr/bin/env python

from string import maketrans

text_in = 'text.txt'

table_in = 'abcdefghijklmnopqrstuvwxyz'
table_out = 'cdefghijklmnopqrstuvwxyzab'
conversion_table = maketrans(table_in, table_out)

print ('')
print ('<---------------->')

with open(text_in, "r") as text:
    for line in text:
        stripped_line = line.strip()
        if stripped_line:
            print ('')
            print ('Original:')
            print stripped_line.rstrip('\n')
            print ('')
            print ('Translation:')
            print stripped_line.translate(conversion_table).rstrip('\n')
            print ('')
            print ('<---------------->')

        else:
            print ('')
            print ('Empty line')
            print ('')
            print ('<---------------->')
