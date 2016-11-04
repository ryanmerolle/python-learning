#!/usr/bin/env python

#Exercises 1 PYNET

ipv6_address = 'FE80:0000:0000:0000:0101:A3EF:EE1E:1719'

ipv6_hextets = ipv6_address.split(":")

print
print "IPv6 Address:", ipv6_address
print
print "Exercise 1 - Splits "
print
print "IPv6 Hextets:"
print ipv6_hextets
print
print

raw_input('Press enter to continue to Exercise 2: ') # getting fancy with pausing until the user hits enter

# Exercise 2 PYNET
print
print
print "Exercise 2 - Joins "
print

ipv6_address_rejoined = ":".join(ipv6_hextets)

print "IPv6 Address rejoined: ", ipv6_address_rejoined
print
