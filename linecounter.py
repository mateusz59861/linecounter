#!/usr/bin/python

import sys

filename = sys.argv[1]

Lines = 0
Words = 0
Chars = 0

with open(filename, "r") as file:
    for line in file:
        list_of_words = line.split()
        Lines = Lines + 1
        Words = Words + len(list_of_words)
        Chars = Chars + len(line)

print("Lines: " + str(Lines))
print("Words: " + str(Words))
print("Chars: " + str(Chars))