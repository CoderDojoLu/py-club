#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## This Fractal converges towards the Koch snowflake
from turtle import *

speed(12)

def f(length, depth):
  print("Called with length: {} and depth {}".format(str(length), str(depth)))
  if depth == 0:
    print("Going forward: {}".format(str(length)))
    forward(length)
  else:
    f(length/3, depth-1)
    print("Going right π/3")
    right(60)
    f(length/3, depth-1)
    print("Going right π/1.5")
    left(120)
    f(length/3, depth-1)
    print("Going right π/3")
    right(60)
    f(length/3, depth-1)

f(250, 4)

# Exit more gracefully: turtle.Terminator (raised)
