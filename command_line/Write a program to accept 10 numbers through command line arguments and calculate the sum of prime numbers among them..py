# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cK-lk0bszIHhM631_8kTbkSM9GsUTIV8
"""

#Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.
import sys

nums = sys.argv


def with_loop():
    total = 0   # to collect the prime numbers
    count = 1   # a counter for the numbers that you entered
    for i in range(10):
        num = int(input("{}. Please enter a number: ".format(count)))
        if num > 1:  # if number is larger than 1, we need to check
            for j in range(2, num):
                if (num % j) == 0:
                    break
            else:
                total += num
        elif num == 1:   # 1 is a prime number
            total += num
        else:   # otherwise the number is negative so we skip.
            pass
        count += 1
    print("\nTotal : {}".format(total))