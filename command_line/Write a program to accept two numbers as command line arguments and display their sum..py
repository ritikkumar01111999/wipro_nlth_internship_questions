# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cK-lk0bszIHhM631_8kTbkSM9GsUTIV8
"""

#Write a program to accept two numbers as command line arguments and display their sum.
import sys

"""n1_ADID = (sys.argv[1])
n2_ADID = (sys.argv[2])
print(n1_ADID,n2_ADID)
sum_ADID = n1_ADID + n2_ADID
print(sum_ADID)"""

"""Here the output is 100200 it has not added them because input taken by command line is always a string so if we perform 
add operation on it then in concatinate them insteaded of adding those values"""

n1_ADID = int(sys.argv[1])
n2_ADID = int(sys.argv[2])
print(n1_ADID,n2_ADID)

sum_ADID = n1_ADID + n2_ADID
print("The sum is :",sum_ADID)

print(len(sys.argv))

print("n1_ADID is a type of",type(n1_ADID))
print("n2_ADID is a type of",type(n2_ADID))