# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 23:42:56 2021

@author: TOYGAR AKIN
"""

# read the file
with open('input.txt') as f:
    entries = f.readlines()

# it read as strings, convert to integers
entries = list(map(int, entries))    

# search the numbers that sum up to 2020 and then multiply them

for i in entries:
    required = 2020 - i
    if required in entries:
        print(i)
        print(required)
        result = i*required
        print("Result: ", str(result))
        break
        
        
        