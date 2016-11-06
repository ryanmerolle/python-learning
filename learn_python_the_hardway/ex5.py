#!/usr/bin/env python

# LPTHW Exercise 5: More Variables and Printing
# https://learnpythonthehardway.org/book/ex5.html

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74.0 # inches
my_weight = 180.0 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print
print "Let's talk about %s." % my_name
print "He's %d inchdes tall." % my_height
print "He's %d centimeters tall." % ( my_height * 2.54 )
print "He's %d pounds heavy." % my_weight
print "He's %d kilograms heavy." % ( my_weight * 0.453592 )
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( my_age, my_height, my_weight,  my_age + my_height + my_weight )
print