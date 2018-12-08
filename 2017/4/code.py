# Advent of code Year 2017 Day 4 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

ok1 = 0
ok2 = 0
for line in input.split("\n"):
	dic1 = {}
	dic2 = {}
	flag1 = True
	flag2 = True
	for word in line.split():
		temp2 = ''.join(sorted(word))
		if temp2 in dic2:
			flag2 = False
		else:
			dic2[temp2] = 1
		if word in dic1:
			flag1 = False
		else:
			dic1[word] = 1
		if not flag1 and not flag2:
			break
	if flag1:
		ok1 += 1
	if flag2:
		ok2 += 1		

print("Part One : "+ str(ok1))
print("Part Two : "+ str(ok2))