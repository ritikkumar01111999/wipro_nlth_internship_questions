# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DWoxYoywrECTD7spEiqsMW6Dz6aPqD6Q
"""

#write  a program to count number of upper and lower case letters in the strings

# Python3 program to count upper and
# lower case characters without using
# inbuilt functions
def upperlower(string):
  
    upper = 0
    lower = 0
  
    for i in range(len(string)):
          
        # For lower letters
        if (ord(string[i]) >= 97 and
            ord(string[i]) <= 122):
            lower += 1
  
        # For upper letters
        elif (ord(string[i]) >= 65 and
              ord(string[i]) <= 90):
            upper += 1
  
    print('Lower case characters = %s' %lower,
          'Upper case characters = %s' %upper)
  
# Driver Code
string = 'A noun is a word that functions as the name of a specific object or set of objects, such as living creatures, places, actions, qualities, states of existence, or ideas. '
upperlower(string)