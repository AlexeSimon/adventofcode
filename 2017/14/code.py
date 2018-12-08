# Advent of code Year 2017 Day 14 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def knot_hash(input):
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
            
    dense_hash = [0 for i in range(16)]
    for i in range(16):
        xor = hash[i*16]
        for j in range(1,16):
            xor = xor ^ hash[i*16+j]
        dense_hash[i] = xor

    string = ''
    for block in dense_hash:
        if block == 0:
            string += "00"
        elif block < 16:
            string += '0'
        string += str(hex(block)).lstrip("0x")

    return string
    
spec = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=128, type='b')
memory = [[0 for i in range(128)] for j in range(128)]
count = 0
for i in range(128):
    temp = knot_hash(input+"-"+str(i))
    result = format(int(temp,16), spec)
    for j in range(128):
        memory[i][j] = int(result[j])
    count += result.count('1')
print("Part One : "+ str(count))

def recursive_region_rename(x, y, ID): #explores right and down and renames 
    if memory[x][y] == 1:
        memory[x][y] = ID
        if x-1 >= 0:
            recursive_region_rename(x-1, y, ID)
        if y-1 >= 0:
            recursive_region_rename(x, y-1, ID)
        if x+1 < len(memory):
            recursive_region_rename(x+1, y, ID)
        if y+1 < len(memory[0]):
            recursive_region_rename(x, y+1, ID)
        
region_id = 2
for i in range(128):
    for j in range(128):
        if memory[i][j] == 1:
            recursive_region_rename(i, j, region_id)
            region_id += 1
print("Part Two : "+ str(region_id-2))

#if you want to see the visual representation of the 128x128 grid, it prints in output.txt
out = open((__file__.rstrip("code.py")+"output.txt"), "w")
for line in memory:
    for block in line:
        out.write(str(block).zfill(4)+" ")
    out.write("\n")
out.close


