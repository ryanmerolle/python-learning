#!/usr/bin/env python

# LPTHW Exercise 16: Reading and Writing Files
# https://learnpythonthehardway.org/book/e16.html

# import the argv function
from sys import argv

script, filename = argv

# prints a string with the filename given as an argument for this python script
print "We're going to erase %r." % filename
# prints a string prompting the user to quit the script using CTRl-C
print "If you don't want that, hit CTRL-C (^C)."
# prints a string prompting the user to hit enter (really anything can be inputed before enter)
print "If you do want that, hit RETURN."

# provides a raw_input for the user to enter
raw_input ("?")

# prints a string
print "Opening the file..."
# opens a file for writing
target = open(filename, 'w')

# prints a string
print "Truncating the file.  Goodbye!"
# deletes the contents of the file (not needed as this happens on write mode)
target.truncate()

# sets variables based on user inputs
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

# prints a string
print "I'm going to write these to file."

# writes each line gathered from the user raw inouts to the file as a new line
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# prints a string
print "And finally, we close it."
# closes the file being written to
target.close()

# opens a file to read (there has to be a way to combine)
target = open(filename)
# prints a string
print "Now let's read the contents of this file back to you:"
# reads the file
print target.read()