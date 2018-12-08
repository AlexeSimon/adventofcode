# Advent of code Year 2017 Day 6 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

banks = [int(number) for number in input.split('\t')]
dic = {}
dic[str(banks)] = 0
n = 0

while True:
    n+=1
    temp = max(banks)
    index = banks.index(temp)
    banks[index] = 0
    while temp > 0:
        index = (index + 1) % len(banks)
        banks[index] += 1
        temp -= 1
    if str(banks) in dic:
        break
    else:
        dic[str(banks)] = n

print("Part One : "+ str(n))
print("Part Two : "+ str(n-dic[str(banks)]))