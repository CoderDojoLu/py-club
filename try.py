#!/usr/bin/env python3

myInput = input("Enter stuff: ")

try:
    int(myInput[0])
except ValueError:
    print("Value error")

try:
    int(myInput[1])
except ValueError:
    print("Value error")

