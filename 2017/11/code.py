# Advent of code Year 2017 Day 11 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

commands = input.split(",")
diagNE = 0
diagNW = 0
maxdist = 0
for command in commands:
    if command == "s":
        diagNE -= 1
        diagNW -= 1
    elif command == "n":
        diagNE += 1
        diagNW += 1
    elif command == "nw":
        diagNW += 1
    elif command == "se":
        diagNW -= 1
    elif command == "ne":
        diagNE += 1
    elif command == "sw":
        diagNE -= 1
    
    if diagNE*diagNW > 0:
        tempdist = max(abs(diagNE), abs(diagNW))
    else: 
        tempdist = abs(diagNE) + abs(diagNW)
        
    if maxdist < tempdist:
        maxdist = tempdist

print("Part One : "+ str(tempdist))
print("Part Two : "+ str(maxdist))