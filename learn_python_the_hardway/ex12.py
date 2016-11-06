#!/usr/bin/env python

# LPTHW Exercise 12: Prompting People
# https://learnpythonthehardway.org/book/e12.html

print
age = raw_input("How old are you? ")
height = raw_input("How tall are you in inches? ")
weight = raw_input("How much do you weigh in pounds? ")
print

print "So, you're %r years old, %r inches tall, and %r lbs heavy." % (age, height, weight) 
print