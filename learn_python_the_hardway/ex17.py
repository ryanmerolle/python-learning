#!/usr/bin/env python

# LPTHW Exercise 17 More Files
# https://learnpythonthehardway.org/book/e17.html

# import the argv and exists and function

from sys import argv
from os.path import exists

script, from_file, to_file = argv

# spacing:
print

print "Copying from %s to %s" % (from_file, to_file)

# Combining old lines into 1:
indata = open(from_file).read()
# old 2 lines:
# in_file = open(from_file)
# indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)

# removing needless user prompts before copying:
# print "Ready, hit RETURN to continue, CTRL-C to abort"
# raw_input()

# Combining old lines into 1:
out_file = open(to_file, 'w').write(indata)
# old 2 lines:
# out_file = open(to_file, 'w')
# out_file.write(indata)

print "Alright, all done."

# updated file closure
open(to_file).close()
open(from_file).close()
# old 2 lines
# out_file.close()
# in_file.close()

# spacing:
print