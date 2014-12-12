#!/usr/bin/env python3

import random

fh = open('words.txt', 'r')

wordList = []
guessWord = []
guessedChar = []

for word in fh:
	wordList.append(word)

random.shuffle(wordList)

word = wordList[0]
wordLength = len(word)

for _ in word:
	guessWord.append("_")

while True:
	print(guessWord)
	guessedChar.append(str(input("Please guess a letter: ")))
	print(guessedChar[0].isalpha())
	if guessedChar[len(guessedChar)-1].isalpha():
		break
	else:
		print("You need to enter a Character, you know: aBc…")
		continue

print("\nThe length of the word: \"{}\" is {}".format(wordList[0].rstrip(), len(wordList[0])))
