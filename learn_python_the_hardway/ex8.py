#!/usr/bin/env python

# LPTHW Exercise 8: Printing, Printing
# https://learnpythonthehardway.org/book/e8.html

formatter = "%r %r %r %r"

print
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
print