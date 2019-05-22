#!/usr/bin/python
# Author: Amit Sharma Copyright 2019
#
# Python script that determines if a string contains balanced parentheses
#
# TODO:
# Add argument processing - getopts
# Argument - string to be processed
# Argument - Delimiter

import sys, os

class Parentheses:

   parens = "abc(def()"
   lpc = 0
   rpc = 0
   for i in parens:
      print i
      if i == '(':
         print "Found Parens"
         lpc += 1
      elif i == ')':
         print "Found Parens"
         rpc += 1
   print "lpc = ", lpc   
   print "rpc = ", rpc   
   if ((lpc == rpc) and (lpc != 0 or rpc != 0)):
      print "String: " + parens + " is balanced."
   else:
      print "String: " + parens + " is not balanced."

if __name__ == "__main__":
   Parentheses()
