#!/usr/bin/env python3

fh = open('words.txt', 'r')

wordList = []

for word in fh:
	wordList.append(word)

print(len(wordList))
