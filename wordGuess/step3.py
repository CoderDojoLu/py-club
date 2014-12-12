#!/usr/bin/env python3

import random

fh = open('words.txt', 'r')

wordList = []

for word in fh:
	wordList.append(word)

random.shuffle(wordList)

print(wordList[0], end="")
print(type(wordList[0]))
