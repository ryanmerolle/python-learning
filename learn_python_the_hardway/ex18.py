#!/usr/bin/env python

# LPTHW Exercise 18: Names, Variables, Code, Functions
# https://learnpythonthehardway.org/book/e18.html

# this one is like your scripts with argv

# spacing:
print

#define a function called print_two
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this one takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothing'."

# calls above defined functions which are all set to print based on the arguments defined while calling the function
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# spacing:
print