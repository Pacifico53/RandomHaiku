#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from pathlib import Path


path1 = Path(__file__).parent / "haikus.txt"
file1 = open(path1, 'r')
Lines = file1.readlines()

path2 = Path(__file__).parent / "translated.txt"
file2 = open(path2, 'r')
Lines2 = file2.readlines()

i = 0
strs = ["" for x in range(3)]
haikujp = []
haikueng = []

for line in Lines:
    strs[i] = line.strip()
    if i == 2:
        haikujp += strs
    i = (i + 1) % 3

for line in Lines2:
    strs[i] = line.strip()
    if i == 2:
        haikueng += strs
    i = (i + 1) % 3

r = random.randrange(1, 76, 3)

print(haikujp[r])
print(haikujp[r+1])
print(haikujp[r+2])

print(haikueng[r])
print(haikueng[r+1])
print(haikueng[r+2])
