# Advent of code Year 2018 Day 2 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input_as_lines = input.splitlines()

double_count = 0
triple_count = 0

for line in input_as_lines:
    char_done = []
    has_double = False
    has_triple = False
    for char in line:
        if not has_double and line.count(char) == 2:
            double_count += 1
            has_double = True
        if not has_triple and line.count(char) == 3:
            triple_count += 1
            has_triple = True

print("Part One : "+str(double_count*triple_count))

def match(box1,box2):
    differ = 0
    ans = ""
    for i in range(len(box1)):
        if(box1[i] != box2[i]):
            differ += 1
            if(differ > 1):
                return False
        else:
            ans += box1[i]
    if differ == 1:
        return ans
    else:
        return False

def find_match(boxes): 
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            ans = match(boxes[i], boxes[j])
            if ans != False:
                return ans
print("Part Two : "+find_match(input_as_lines))