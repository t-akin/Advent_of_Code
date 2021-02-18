# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 22:55:59 2021

@author: TOYGAR AKIN
"""

# read the map. delete the last blank item that comes from splitting
mapp = open('input.txt','r').read().split('\n') 
mapp = mapp[0:-1]   

# count the rows
print("Number of rows: ", len(mapp))
# there are 323 rows

# count the columns
print("Number of columns: ", len(mapp[0]))
# there are 31 columns. 

### Part A ###
##############

# we must go 3 units right per move, so we need 323*3 - 31 = 938 more columns.
# in other words, we should replicate the columns for 938/31 ~ 30.26 times.

mapp_rep = list(map(lambda x: x*32, mapp))
# we need 31 more times of mapp, plus itself, it makes 32.

# label the starting points and assign a counter to count number of encountered
# trees
start_row = 0
start_col = 0
counter = 0

# check if any tree is encountered during travel
for i in range(0, len(mapp_rep)-1):
    start_row += 1
    start_col += 3
    geog = mapp_rep[start_row][start_col]
    if geog == '#':
        counter += 1
        
print("Number of encountered trees is: ", counter)

### Part B ###
##############

# the maximum possible right move is 7 here. so we need 323*7 - 31 ~ 2230 columns
mapp_rep_2 = list(map(lambda x: x*2231, mapp))

import numpy as np
# there are 5 alternatives. store results in arrays
start_rows = np.zeros(5).astype(int)
start_cols = np.zeros(5).astype(int)
counters = np.zeros(5).astype(int)

# same operations in part a
for i in range(0, len(mapp_rep_2)-1):
    start_rows[0] += 1
    start_rows[1] += 1
    start_rows[2] += 1
    start_rows[3] += 1
    
    # heads up! final alternative uses 2 downs per move. we should stay
    # in our limits while indexing
    start_rows[4] = np.minimum(start_rows[4] + 2, 322)
    
    start_cols[0] += 1
    start_cols[1] += 3
    start_cols[2] += 5
    start_cols[3] += 7
    start_cols[4] += 1
    
    geog1 = mapp_rep_2[start_rows[0]][start_cols[0]]
    geog2 = mapp_rep_2[start_rows[1]][start_cols[1]]
    geog3 = mapp_rep_2[start_rows[2]][start_cols[2]]
    geog4 = mapp_rep_2[start_rows[3]][start_cols[3]]
    geog5 = mapp_rep_2[start_rows[4]][start_cols[4]]
    
    if geog1 == '#':
        counters[0] += 1
        
    if geog2 == '#':
        counters[1] += 1
        
    if geog3 == '#':
        counters[2] += 1
        
    if geog4 == '#':
        counters[3] += 1
        
    if geog5 == '#' and i <= 161: # 322/2 = 161
        counters[4] += 1
        
print("Multiplication of number of encountered trees is: ", np.prod(counters))
