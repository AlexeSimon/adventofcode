# Advent of code Year 2018 Day 5 solution
# Author = Alexe Simon
# Date = December 2018

import string

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = list(input_file.read())

def resolve(polymer):
    i = 0
    while i < len(polymer)-1:
        if polymer[i] != polymer[i+1] and polymer[i].upper() == polymer[i+1].upper():
            del polymer[i+1]
            del polymer[i]
            i = -1
        i += 1
    return polymer

def remove_all(polymer, character):
    i = 0
    while i < len(polymer):
        if polymer[i] == character or polymer[i] == character.upper():
            del polymer[i]
            i -= 1
        i += 1
    return polymer
    
base = resolve(input)

print("Part One : "+ str(len(base)))

best = None
best_score = len(base)
for i in list(string.ascii_lowercase):
    score = len(resolve(remove_all(base.copy(), i)))
    if score < best_score:
        best = i
        best_score = score
        
print("Part Two : "+ str(best_score))