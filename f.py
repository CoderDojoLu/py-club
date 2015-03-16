#!/usr/bin/env python3
while True:
    myInput = input("Gimme some data between 0 and 42: ")
    try:
       myInput = int(myInput)
    except ValueError:
       print('Valid number, please')
       continue
    if 0 <= myInput <= 42:
       break
    else:
       print('Valid range, please: 0-42')
