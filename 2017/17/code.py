# Advent of code Year 2017 Day 17 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

STEPS = int(input)
TOTAL = 2017
BIGTOTAL = 50000000

import math

class Tornado:
    def __init__(self, steps):
        self.pos = 1
        self.num = 1
        self.state = [0, 1]
        self.steps = steps
        
    def next_state(self):
        self.pos = (self.pos + self.steps) % len(self.state) + 1
        self.num += 1
        self.state.insert(self.pos, self.num)
        
    def to_state(self, n):
        while self.num < n:
            self.next_state()
    
    def __str__(self):
        return "State "+str(self.num) + ", pos = " + str(self.pos) + " : " + str(self.state)
        
    def find_next(self):
        return self.state[(self.pos+1)%len(self.state)]
        
    def find_second(self):
        return self.state[1]
    
    def next_imaginary_state(self):
        jump = ((self.num+1-self.pos) // self.steps)
        if (self.num+1-self.pos) % self.steps > 0:
            jump += 1
            
        self.pos = (self.pos + self.steps*jump) % (self.num+1) + 1
        self.num += jump
        if self.pos == 1:
            self.state[1] = self.num
            
    def to_imaginary_state(self, n):
        while self.num < n:
            self.next_imaginary_state()
    
        
my_tornado = Tornado(STEPS)
my_tornado.to_state(TOTAL)
my_imaginary_tornado = Tornado(STEPS)
my_imaginary_tornado.to_imaginary_state(BIGTOTAL)

print("Part One : "+ str(my_tornado.find_next()))
print("Part Two : "+ str(my_imaginary_tornado.find_second()))