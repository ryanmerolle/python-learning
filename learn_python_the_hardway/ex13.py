#!/usr/bin/env python

# LPTHW Exercise 13: Parameters, Unpacking, Variables
# https://learnpythonthehardway.org/book/e13.html

from sys import argv

# This is a python script with command line arguments.
# This script cannot just run without declaring  the 3  variables as an argument
script, first, second, third = argv

print
fourth = raw_input("Enter a fourth variable: ")
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth
print