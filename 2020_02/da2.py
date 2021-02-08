# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:50:22 2021

@author: TOYGAR AKIN
"""

# read the file. delete the last blank item that comes from splitting    
passes = open('input.txt','r').read().split('\n') 
passes = passes[0:-1]   

# define a function to separate
# i. min & max number of occasions a character can take in a password
# ii. relevant character
# iii. password

def unpack(lst):
    lst1 = []
    lst2 = []
    lst3 = []
    for item in lst:
        splitt = item.split(" ")
        lst1.append(splitt[0])
        lst2.append(splitt[1])
        lst3.append(splitt[2])
    return (lst1, lst2, lst3)

limits, char, passwords = unpack(passes)

# correct char list
char = list(map(lambda x: x.split(":")[0], char))

# separate minimum and maximum values
mins = list(map(int, map(lambda x: x.split("-")[0], limits)))
maxes = list(map(int, map(lambda x: x.split("-")[1], limits)))

# count the number of occurences of the given character in the passwords
occur = []
for i in range(0, len(passwords)):
    number = passwords[i].count(char[i])
    occur.append(number)
    
# store the arrays in a data frame
import pandas as pd

df = pd.DataFrame({"mins": mins,
                   "maxes": maxes,
                   "char": char,
                   "passwords": passwords,
                   "occurences": occur})

# check if the number of occurences is within limits
df["Boolean"] = 1*((df["mins"] <= df["occurences"]) & (df["maxes"] >= df["occurences"]))
df.head()

print("Number of valid passwords are ", str(df["Boolean"].sum()))
