#!/usr/bin/env python

# LPTHW Exercise 7: More Printing
# https://learnpythonthehardway.org/book/e7.html

print # print an empty line
print "Mary had a little lamb." # print a string
print "Its fleece was whist as %s" % 'snow' # print a string with a variable
print "And everywhere that Mary went." # print a string
print "." * 10 # what'd that do? Print the string 10 times

# declare 12 variables:
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6, # the comma signifies the two lines will be printed on a single line with a space
print end7 + end8 + end9 + end10 + end11 + end12 # prints variables with no spaces in between