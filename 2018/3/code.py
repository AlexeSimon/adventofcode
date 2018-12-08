# Advent of code Year 2018 Day 3 solution
# Author = Alexe Simon
# Date = December 2018

import re

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

class Claim:
    def __init__(self, description):
        match = re.match("#(?P<id>.+) @ (?P<dist_to_left>.+),(?P<dist_to_top>.+): (?P<width>.+)x(?P<height>.+)", description)
        self.id = int(match.group("id"))
        self.x1 = int(match.group("dist_to_left"))
        self.x2 = int(match.group("width"))+self.x1
        self.y1 = int(match.group("dist_to_top"))
        self.y2 = int(match.group("height"))+self.y1
        self.alone = True

        
fabric = [[0 for i in range(1000)] for i in range(1000)]
claims = [Claim(line) for line in input.split("\n")]
alone = list(range(1, len(claims)+1))

for claim in claims:
    for i in range(claim.x1, claim.x2):
        for j in range(claim.y1, claim.y2):
            if fabric[i][j] == 0:
                fabric[i][j] = claim.id
            else:
                if claim.alone:
                    claim.alone = False
                    alone.remove(claim.id)
                if fabric[i][j] > 0 :
                    if claims[fabric[i][j]-1].alone:
                        claims[fabric[i][j]-1].alone = False
                        alone.remove(claims[fabric[i][j]-1].id)
                    fabric[i][j] = -1
                else:
                    fabric[i][j] -= 1

over_claimed = 0
for i in range(1000):
    for j in range(1000):
        if fabric[i][j] < 0:
            over_claimed += 1

# If you want to see the fabric :
# with open((__file__.rstrip("code.py")+"output.txt"), 'w+') as output_file:
    # for line in fabric:
        # output_file.write(str(line)+"\n")

print("Part One : "+ str(over_claimed))
print("Part Two : "+ str(alone[0]))