#!/usr/bin/env python3
import time, random

version = "0.1"
penalty = 1
words = ['one','password','taxi', 'pizza', 'polo']

print("""Welcome to the fastestTyper v{}

Your mission is to type as fast as you can the words displayed followed by the enter key.

If a word is wrong, you will get a -{} seconds penalty.
""".format(version, penalty))

input("Press the enter key to start the game, type the word as fast as you can…")

startTime = int(time.time())

randomWord = words[random.randint(0,len(words)-1)]

while answer != answer:
	answer = input()
	if answer == randomWord:
		print("Well done, it took you: {} second and {} try(ies)".format(deltaTime, tries))