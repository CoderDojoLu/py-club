#!/usr/bin/env python3

import time

x = "bla"

startTime = int(time.time())

while True:
	if x == 'blah':
		print('exiting loop')
		break

	print(time.time())
	time.sleep(1)
	x = input("type a word :) ")

endTime = int(time.time())

print("""

yo dawg, 

you started at:

{} seconds

and ended at:

{} seconds


elapsed since 00:00:00 Coordinated Universal Time (UTC), Thursday, 1 January 1970


Delta: {}""".format(startTime,endTime, endTime-startTime))