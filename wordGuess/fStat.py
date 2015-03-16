#!/usr/bin/env python3

# Source: cat /usr/share/dict/words > words.txt

fh = open('words.txt')

for index, word in enumerate(fh.readlines()):
    print(index, len(word))

