# Advent of code Year 2017 Day 3 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = int(input_file.read())

import math

ring = math.ceil((math.sqrt(input) - 1) / 2)

pin = (((ring - 1) * 2 + 1) ** 2) + 1
x = ring
y = -ring + 1

for i in range(0, 2 * ring - 1):
    if pin == input:
        break
    y += 1
    pin += 1

for i in range(0, 2 * ring):
    if pin == input:
        break
    x -= 1
    pin += 1

for i in range(0, 2 * ring):
    if pin == input:
        break
    y -= 1
    pin += 1

for i in range(0, 2 * ring):
    if pin == input:
        break;
    x += 1
    pin += 1

print("Part One : "+ str(abs(x) + abs(y)))


class Spiral(dict):
    def add(self, x, y):
        if (x, y) in self:
            return self[(x, y)]
        else:
            self[(x, y)] = self.get(x - 1, y) + self.get(x + 1, y) + self.get(x, y - 1) + self.get(x, y + 1) + self.get(
                x + 1, y + 1) + self.get(x - 1, y + 1) + self.get(x - 1, y - 1) + self.get(x + 1, y - 1)
            return self[(x, y)]

    def get(self, x, y):
        if (x, y) in self:
            return self[(x, y)]
        else:
            return 0


mySpiral = Spiral()

ring = 1
x = 0
y = 0
mySpiral[(0, 0)] = 1

while True:
    x += 1
    for i in range(0, 2 * ring - 1):
        if mySpiral.add(x, y) > input:
            break
        y += 1

    for i in range(0, 2 * ring):
        if mySpiral.add(x, y) > input:
            break
        x -= 1

    for i in range(0, 2 * ring):
        if mySpiral.add(x, y) > input:
            break
        y -= 1

    for i in range(0, 2 * ring):
        if mySpiral.add(x, y) > input:
            break
        x += 1

    if mySpiral.add(x, y) > input:
        break
    ring += 1

print("Part Two : "+ str(mySpiral.get(x, y)))