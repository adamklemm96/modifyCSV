#!/usr/bin/env python3
import pandas as pd
import sys, os, csv, random

def clean():
    os.system("clear")

path1 = sys.argv[1]

while True:
    try:
        password_lenght = int(input("What is the minimum lenght of hash?:"))
    except:
        print("You didn't enter integer")
        continue
    else:
        break

print("Looking for passwords longer then", password_lenght, "chars")

#open sample
with open(path1) as file:
    sample_data = random.sample(file.readlines(), 10000)

#Variable to store potentional hashes
hashes = []

for line in sample_data:
    try:
        sec_column = line.split(":",1)[1]
        if len(sec_column) > 20:
            hashes.append(sec_column)
    except:
        continue

display_hashes = 10

clean()
#Show hashes
print(hashes[:display_hashes])
#Store variable 
new_position = []

while True:
    keep_going = input("Show 10 more hashes? [y/n]: ")
    if keep_going == 'y' :
        display_hashes += 10 
        print(hashes[display_hashes:display_hashes+10])
    else:
        clean()
        break

option = 0
for x in hashes[display_hashes:display_hashes+10]:
    new_position.append(x)
    print(option," ", x)
    option += 1
choice = int(input("What position has the desired hash?(0-9): "))

clean()
print("your choice is:", new_position[choice])