# Advent of code Year 2018 Day 1 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

frequency = 0
input_as_int = [int(line) for line in input.splitlines()]
size = len(input_as_int)
reached = {}
found = False

for val in input_as_int:
    frequency += val
    if not found and frequency in reached:
        reached_twice = frequency
        found = True
    reached[frequency] = True
print("Part One :" + str(frequency))

i = 0
while not found:
    frequency += input_as_int[i]
    if not found and frequency in reached:
        reached_twice = frequency
        found = True
    reached[frequency] = True
    i = (i+1) % size

print("Part Two : " + str(reached_twice))