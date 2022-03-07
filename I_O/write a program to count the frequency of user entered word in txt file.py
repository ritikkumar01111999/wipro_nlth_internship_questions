# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cK-lk0bszIHhM631_8kTbkSM9GsUTIV8
"""

# write a program to count the frequency of user entered word in txt file
text = open("sample.txt", "r")
  
# Create an empty dictionary
d = dict()
  
# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()
  
    # Convert the characters in line to 
    # lowercase to avoid case mismatch
    line = line.lower()
  
    # Split the line into words
    words = line.split(" ")
  
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1
  
# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])