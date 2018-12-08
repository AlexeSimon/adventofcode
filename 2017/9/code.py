# Advent of code Year 2017 Day 9 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

depth = 0
score = 0
index = 0
count = 0
garbage = False

while index < len(input):

    if input[index] == "!":
        index += 1
    elif garbage:
        if input[index] == ">":
            garbage = False
        else:
            count += 1
    else:
        if input[index] == "<":
            garbage = True
        elif input[index] == "}" and depth > 0:
            depth -= 1
        elif input[index] == "{":
            depth += 1
            score += depth
    index += 1

print("Part One : "+ str(score))
print("Part Two : "+ str(count))