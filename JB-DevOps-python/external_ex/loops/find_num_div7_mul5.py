#!/bin/python3

# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

nl=[]
for x in range(1500, 2700):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))

