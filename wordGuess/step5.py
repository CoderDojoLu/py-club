#!/usr/bin/env python3

import random

fh = open('words.txt', 'r')

wordList = []

for word in fh:
	wordList.append(word)

random.shuffle(wordList)

word = wordList[0]
wordLength = len(word)

while True:
	for a in word:
		print("_ ", end="")
	break

print("\nThe length of the word: \"{}\" is {}".format(wordList[0].rstrip(), len(wordList[0])))
