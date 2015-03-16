#!/usr/bin/env python3
#first.py
from scratra import *

@start
def whenstart(scratch):
  print('Hello, World!')

@broadcast('hi, scratra!')
def hi(scratch):
  print('Hi, Scratch!')

run()
