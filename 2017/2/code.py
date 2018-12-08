# Advent of code Year 2017 Day 2 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [[int(i) for i in line.split('\t')] for line in input_file]


print("Part One : "+ str(sum([max(row)-min(row) for row in input])))
print("Part Two : "+ str(int(sum([sum([sum([(i/j if i > j and i%j is 0 else 0) for i in row]) for j in row]) for row in input]))))