# Advent of code Year 2017 Day 10 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

#part1
commands = [int(num) for num in input.split(",")]
hash = [i for i in range(0,256)]
skip = 0
index = 0

for command in commands:
    if index + command < 256:
        sublist = hash[index:index+command]
        sublist = sublist[::-1]
        hash[index:index+command] = sublist
    else:
        sublist = hash[index:] + hash[:(index+command)%256]
        sublist = sublist[::-1]
        hash[index:] = sublist[0:256-index]
        hash[:(index+command)%256] = sublist[256-index:]
    
    index = (index + skip + command) %256
    skip += 1

print("Part One : "+ str(hash[0]*hash[1]))    

#part 2
commands = [ord(character) for character in input]
commands += [17, 31, 73, 47, 23]
hash = [i for i in range(0,256)]
skip = 0
index = 0
for j in range(64):
    for command in commands:
        if index + command < 256:
            sublist = hash[index:index+command]
            sublist = sublist[::-1]
            hash[index:index+command] = sublist
        else:
            sublist = hash[index:] + hash[:(index+command)%256]
            sublist = sublist[::-1]
            hash[index:] = sublist[0:256-index]
            hash[:(index+command)%256] = sublist[256-index:]
        
        index = (index + skip + command) %256
        skip += 1
        
densehash = [0 for i in range(16)]
for i in range(16):
    xor = hash[i*16]
    for j in range(1,16):
        xor = xor ^ hash[i*16+j]
    densehash[i] = xor

string = ''
for block in densehash:
    if block == 0:
        string += "00"
    elif block < 16:
        string += '0'
    string += str(hex(block)).lstrip("0x")

print("Part Two : "+ string)