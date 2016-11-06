#!/usr/bin/env python

# LPTHW Exercise 6: Strings and Text
# https://learnpythonthehardway.org/book/ex6.html

# variable containing a string and another variable:
x = "There are %d types of people." % 10
# variable containing a string:
binary = "binary"
# variable containing a string:
do_not = "don't"
# variable containing a string and 2 variables:
y = "Those who know %s and those who %s" % (binary, do_not)

# empty line:
print
# print variable x:
print x
# print variable y:
print y
# empty line:
print
# print a string with a variable referencing the already declared variable x:
print "I said: %r." % x
# print a string with a variable referencing the already declared variable y:
print "I also said: '%s'." % y
# empty line:
print
# variable containing a boolean:
hilarious = False
# variable containing a string and another variable:
joke_evaluation = "Isn't that joke so funny?! %r"
# print a variable (which was declared as a string with a variable) with a variable set as a boolean:
print joke_evaluation % hilarious
# empty line:
print
# declaring a vairable as a string:
w = "This is the left side of..."
# declaring a vairable as a string:
e = "a string with a right side."
# print two vriables strings
print w + e
# empty line:
print

