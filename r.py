#!/usr/bin/env python3
import csv

with open('eggs.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		print(', '.join(row))
		type(row)
		type(spamreader)
