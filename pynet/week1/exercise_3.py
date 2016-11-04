#!/usr/bin/env python

#Exercises 3 PYNET

#Instructions: In the test3.py script, how would you modify this to remove the trailing newline on the end of 192.168.1.1

import fileinput

for line in fileinput.input():
  line = line.strip() 
  print line.split(".")
# echo '192.168.1.1'  | ./exercise_3.py
