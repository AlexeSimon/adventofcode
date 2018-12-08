# Advent of code Year 2017 Day 8 solution
# Author = Alexe Simon
# Date = December 2018

input_file = open((__file__.rstrip("code.py")+"input.txt"), 'r')

data = {}
maxest = 0
for line in input_file:
    words = line.split()
    reg = words[0]
    job = words[1]
    valjob = int(words[2])
    #skip "if" at words[3]
    ref = words[4]
    tes = words[5]
    valtes = int(words[6])
    do = False
    if reg not in data:
        data[reg] = 0
    if ref not in data:
        data[ref] = 0
    
    if tes == "<":
        if(data[ref] < valtes):
            do = True
    elif tes == "<=":
        if(data[ref] <= valtes):
            do = True
    elif tes == ">":
        if(data[ref] > valtes):
            do = True
    elif tes == ">=":
        if(data[ref] >= valtes):
            do = True
    elif tes == "!=":
        if(data[ref] != valtes):
            do = True
    elif tes == "==":
        if(data[ref] == valtes):
            do = True
    else:
        print("ERROR")
    
    if do:
        if job == "inc":
            data[reg] += valjob
        else:
            data[reg] -= valjob
    
    if maxest < data[reg]:
        maxest = data[reg]
max = 0
for key, value in data.items():
    if max < value:
        max = value

input_file.close()

print("Part One : "+ str(max))
print("Part Two : "+ str(maxest))