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

### Part A ###
##############

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

### Part B ###
##############

# rename columns for convenience
df = df.rename(columns = {'mins': 'firstPos', "maxes": "secondPos"})

# for every row, find the characters in the password for the given positions.
# if they match with the given char, return 1; else 0.
# i believe python should have an easier way to do this.
for i in range(0, len(df)):
   fp = df["firstPos"][i]
   sp = df["secondPos"][i]
   
   firstC = df["passwords"][i][fp-1]
   secondC = df["passwords"][i][sp-1]
   
   df["firstPosBool"][i] = 1*(firstC == df["char"][i])
   df["secondPosBool"][i] = 1*(secondC == df["char"][i])

# sum two boolean values. if result is 1, then it means exactly one position
# contains the given char.
df['final'] = df.loc[:,['firstPosBool','secondPosBool']].sum(axis=1)

print("Number of valid passwords are ", 1*(df["final"] == 1).sum())
