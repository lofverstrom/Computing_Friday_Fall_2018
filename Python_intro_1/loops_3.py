#!/usr/bin/env python

from __future__ import print_function

## OBS, note that some of these output 

items = [int(1.99), 
         float(2),  
         'string',
         True,
         (3,3), 
         [3,3], 
         complex(2., -1.)]

print('\nList of Python data types\n')

for i, item in enumerate(items):
    print('List element', i, ':', item, 'is of type:', type(item))


i = 0
for item in items:
    print(i, item)
    i += 1
