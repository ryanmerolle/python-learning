#!/usr/bin/env python

# LPTHW Exercise 19: Functions and Variables
# https://learnpythonthehardway.org/book/e19.html

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the functions numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

## Getting fancy with raw_input:

amount_of_cheese = int(raw_input("How much cheese do you have? "))
amount_of_crackers = int(raw_input("How many crackers do you have? "))
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

## Getting uber fancy with if-statements and more
print "Let's have a real party!"


def party(sandwhich_count, beer_count, guest_count):
    print "You have %d sandwhiches!" % sandwhich_count
    print "You have %d 12-packs of beer, that's %d bottles of beer!" % (beer_count, beer_count * 12)
    print "You are inviting %d guests!\n" % guest_count
    print "Your food to guest ratio is %.1f sandwhiches for each guest." % (sandwhich_count / guest_count)
    if (beer_count * 12 / guest_count) < 4:
        print "Your beer to guest ratio is %.1f bottles of beer for each guest.\nWe need more beer!\n" % (
            beer_count * 12 / guest_count)
    else:
        print "Your beer to guest ratio is %.1f bottles of beer for each guest.\n Perfect!\n" % (
            beer_count * 12 / guest_count)


amount_of_guests = int(raw_input("How many people should we invite to our party? "))
amount_of_sandwhiches = int(raw_input("How many sandwhiches did you order? "))
amount_of_beer = int(raw_input("How many beer 12-packs of beer did you buy? "))

party(amount_of_sandwhiches, amount_of_beer, amount_of_guests)
