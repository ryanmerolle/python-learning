#!/usr/bin/env python

# LPTHW Exercise 11: Asking Questions
# https://learnpythonthehardway.org/book/e11.html

print
print "How old are you?",
age = raw_input()
print "How tall are you in inches?",
height = raw_input()
print "How much do you weigh in pounds?",
weight = raw_input()
print

print "So, you're %r old, %r inches tall, and %r lbs heavy." % (age, height, weight) 
print