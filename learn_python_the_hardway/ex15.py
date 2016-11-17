#!/usr/bin/env python

# LPTHW Exercise 15: Reading Files
# https://learnpythonthehardway.org/book/e15.html

# import the argv function
from sys import argv

# set the argv permaters (script_name, and argument)
script, filename = argv

# declares a variable equal to the argv filename
txt = open(filename)

# print a string with a variable pulled from the argv filename entry 
print"Here's your file %r:" % filename
# print file contents based on variable txt which is defined as the argv argument declared as filename
print txt.read()

# print a string
print "Type the filename again:"
file_again = raw_input ("> ")
# print file contents again based on a in script raw_input method
txt_again = open(file_again)

# print file contents based on variable txt_again which is provided as as a raw_input
print file_again.read()