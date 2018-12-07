# Advent of code Year 2017 Day 1 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

sum1 = 0
sum2 = 0
n = int(len(input)/2)
for i in range(len(input)):
    if(int(input[i]) == int(input[(i+1)%len(input)])):
        sum1+=int(input[i])
    if(int(input[i]) == int(input[(i+n)%len(input)])):
        sum2+=int(input[i])

print("Part One : "+ str(sum1))
print("Part Two : "+ str(sum2))