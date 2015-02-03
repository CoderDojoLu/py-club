#!/usr/bin/env python
#
# Initially based on sudoku-password card
#
# This software is in the public domain
#
# python password-card.py  -c 100 -p 13 -n 10
#
# Alexandre Dulaunoy (a<AT>foo.be)

from optparse import OptionParser
import sys
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from random import choice, shuffle

def strong_password(size=10):
  nbig = size/5
  nsmall = size/3
  v = ([choice(ascii_uppercase) for x in xrange(  nbig)] +
        [choice(ascii_lowercase) for x in xrange(nsmall)] +
        [choice(digits)          for x in xrange(size/2)] +
        [choice(punctuation.replace('|','-'))     for x in xrange(size/5)] )
  shuffle(v)
  return v[:size]

usage = "usage: %prog [options]"
parser = OptionParser(usage)
parser.add_option("-c","--card", dest="card", type=int, default=1, help="set the number of password card to generate (default is 1)")
parser.add_option("-n","--number", dest="number", type=int, default=9, help="set the number of password lines (default is 9)")
parser.add_option("-p","--pnumber", dest="pnumber", type=int, default=9, help="set the number of vertical lines (default is 9)")
parser.add_option("-t","--topheader", dest="topheader", default=True, action='store_false', help="disable top header")
parser.add_option("-l","--leftheader", dest="leftheader", default=True, action='store_false', help="disable left header")
(options, args) = parser.parse_args()

for n in xrange(options.card):
  if options.leftheader:
      sys.stdout.write("  ")
  if options.topheader:
      sys.stdout.write("  ")
      for l in xrange(options.pnumber+1):
        sys.stdout.write(ascii_uppercase[l]+"  ")
      sys.stdout.write("\n")

  for i in xrange(options.number):
    if options.leftheader:
        sys.stdout.write(str(i)+ "   ")
    for c in strong_password(size=options.pnumber+1):
        sys.stdout.write(c+"  ")
    sys.stdout.write("\n")

  sys.stdout.write("\n")
