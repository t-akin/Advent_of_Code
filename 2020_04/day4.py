# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:32:41 2021

@author: TOYGAR AKIN
"""

### Part A ###
##############

# create an empty list to store all the passports
passports = [] 

# create an empty list to store present fields as a list
pass_line = []

# open the file and combine passport fields
with open('input.txt','r') as file: 
   
    # reading each line     
    for line in file:
        
        # a new line signals for a new passport. store the previous fields
        # the previous person's password
        if line == "\n":
            passports.append(pass_line)
            pass_line = []
        
        # read all the present fields and combine them to label as a passport
        for word in line.split():
            pass_line.append(word)

# append the last line            
passports.append(pass_line)
        
# the passport fields are stored as list of lists right now. make a new
# list to store a passport as one line       
passports_line = list(map(lambda x: ' '.join(x), passports))

# create some counter vriables
all_c = 0 # counts all field present passports
semi_c = 0 # counts semi valid passports: the ones the all fields are present but "cid"
    
for i in range(0, len(passports_line)):
    if len(passports[i]) == 8: # 8 fields present means all fields are present
        all_c += 1
    elif len(passports[i]) == 7: # if only one field is missing, check the missing fields
        if "cid:" not in passports_line[i]: # passport is valid if the missing field is "cid"
            semi_c += 1
         
print("Number of valid passports are: ", all_c + semi_c)

### Part B ###
##############

# for this part, we will read the file from the beginning once more.
# for every line, we will take every single string and split it and
# store as a tuple. then the tuples will be combined to denote the passport 
# and we will convert it to dictionary. after all lines are combined, the 
# list of dictionaries will be converted to a data frame. the data frame format
# will be easier to implement logical expressions.

# my intuition says this is an inconvenient way to do this. data format is
# transformed for 3 times. if you have any suggestions for an easier way, 
# you are welcome.

m["pid"]=m.pid.astype(float) # böyle böyle çevirmemiz gerekecek
len(m["iyr"][0]) # böyle karakter uzunlugu sayariz
m.isnull().sum(axis=1) # satirlik missing saymak icin
m["pid"].isnull()


# reading each line   
big_list = [] 
tuples = []

with open('input.txt','r') as file: 
    for line in file:
        if line != "\n":
            for word in line.split():
                tuples.append(tuple(word.split(":")))
        else:
            big_list.append(dict(tuples))
            tuples = []
big_list.append(dict(tuples))
            
import pandas as pd
df = pd.DataFrame(big_list)
df.head()

# implement the rules as binary variables. 1 if rule is satisfied; 0 if it
# is violated.

# define rule columns as placeholders
df["rule1"] = 1
df["rule2"] = 1
df["rule3"] = 1
df["rule4"] = 1
df["rule5"] = 1
df["rule6"] = 1
df["rule7"] = 1

for i in range(0, len(df)):
    # rule 1
    if pd.isnull(df["byr"][i]) == True:
        df["rule1"][i] = 0
    else:
        df["rule1"][i] = ((len(df["byr"][i]) == 4) 
                          & (float(df["byr"][i]) >= 1920)
                          & (float(df["byr"][i]) <= 2002))*1
        
    # rule 2
    if pd.isnull(df["iyr"][i]) == True:
        df["rule2"][i] = 0
    else:
        df["rule2"][i] = ((len(df["iyr"][i]) == 4) 
                          & (float(df["iyr"][i]) >= 2010)
                          & (float(df["iyr"][i]) <= 2020))*1
    
    # rule 3
    if pd.isnull(df["eyr"][i]) == True:
        df["rule3"][i] = 0
    else:
        df["rule3"][i] = ((len(df["eyr"][i]) == 4) 
                          & (float(df["eyr"][i]) >= 2020)
                          & (float(df["eyr"][i]) <= 2030))*1
        
    # rule 4
    if pd.isnull(df["hgt"][i]) == True:
        df["rule4"][i] = 0
    else:
        if "cm" in df["hgt"][i]:
            df["rule4"][i] = ((float(df["hgt"][i].split("cm")[0]) >= 150) & 
                           (float(df["hgt"][i].split("cm")[0]) <= 193))*1
        elif "in" in df["hgt"][i]:
            df["rule4"][i] = ((float(df["hgt"][i].split("in")[0]) >= 59) & 
                           (float(df["hgt"][i].split("in")[0]) <= 76))*1
        else:
            df["rule4"][i] = 0   

    # rule 5
    if pd.isnull(df["hcl"][i]) == True:
        df["rule5"][i] = 0   
    elif df["hcl"][i][0] != "#":
        df["rule5"][i] = 0
    elif df["hcl"][i][0] == "#":
        if len(df["hcl"][i]) != 7:
            df["rule5"][i] = 0
        else:
            for char in df["hcl"][i].split("#")[1]:
                if (not char in "abcdef") and (not char.isdigit()):
                    df["rule5"][i] = 0
                else:
                    df["rule5"][i] = 1        
      
    # rule 6
    if pd.isnull(df["ecl"][i]) == True:
        df["rule6"][i] = 0
    else:
        df["rule6"][i] = ((df["ecl"][i] == "amb") | 
                          (df["ecl"][i] == "blu") | 
                          (df["ecl"][i] == "brn") | 
                          (df["ecl"][i] == "gry") |
                          (df["ecl"][i] == "grn") | 
                          (df["ecl"][i] == "hzl") | 
                          (df["ecl"][i] == "oth"))*1
    
    # rule 7
    if pd.isnull(df["pid"][i]) == True:
        df["rule7"][i] = 0
    else:
        df["rule7"][i] = (len(df["pid"][i]) == 9)*1
        
# take the minimum of the rules. if any of the rules is violated, then the 
# minimum value will be 0.
df['final'] = df[['rule1','rule2', "rule3", "rule4", "rule5", 
                    "rule6", "rule7"]].min(axis=1)

# the sum of the final column gives the number of valid passports
print("Number of valid passports are: ", df["final"].sum())
