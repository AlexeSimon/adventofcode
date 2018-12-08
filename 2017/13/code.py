# Advent of code Year 2017 Day 13 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

layers = [0 for i in range(100)]
max = 0
for line in input.split("\n"):
    words = line.split()
    max = int(words[0].rstrip(':'))
    layers[max] = int(words[1])

i = 0
severity = 0
while i <= max:
    if layers[i] != 0:
        if i % ((layers[i]-1)*2) == 0:
            severity += layers[i]*i
    i += 1
print("Part One : "+ str(severity))

delay = 0
i = 0
while i <= max:
    if layers[i] != 0:
        if (i+delay) % ((layers[i]-1)*2) == 0:
            i = -1
            delay += 1
    i += 1
print("Part Two : "+ str(delay))