#!/usr/bin/env python3

import random
import manHangASCII

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

	if guessedChar[len(guessedChar)-1].isalpha() & len(guessedChar[len(guessedChar)-1]) == 1:
		print("Great, we have ONE char that is NOT numerical")
		print("The char: \"{}\" is {} times in the word".format(guessedChar[len(guessedChar)-1], word.count(guessedChar[len(guessedChar)-1])))
		break
	else:
		print("You need to enter a Character, you know: aBc…")
		continue


print("\nThe length of the word: \"{}\" is {}".format(wordList[0].rstrip(), len(wordList[0])))
