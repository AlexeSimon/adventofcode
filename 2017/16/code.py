# Advent of code Year 2017 Day 16 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

SHOW_PROGRESS = False

import re

class ProtocolReader:
    def __init__(self, source):
        self.jobs = source.split(",")
        self.progs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
        self.level = 0
        self.loop = None
    
    def reset_level(self):
        self.progs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
        self.level = 0
    
    def basic_compute(self):
        for job in self.jobs:
            if job[0] == "s": #sN
                for i in range(int(job[1:])):
                    self.progs.insert(0,self.progs.pop())
                
            if job[0] == "x": #xN/M
                nums = re.findall("[\d]+", job)
                self.progs[int(nums[0])], self.progs[int(nums[1])] = self.progs[int(nums[1])], self.progs[int(nums[0])]
                
            if job[0] == "p": #pA/B
                index1 = self.progs.index(job[1])
                index2 = self.progs.index(job[3])
                self.progs[index1], self.progs[index2] = self.progs[index2], self.progs[index1]
                
        self.level += 1
    
    def find_loop(self):
        current_level = self.level
        current_progs = self.progs.copy()
        
        self.loop = 0
        hist = []
        
        while(''.join(self.progs) not in hist):
            hist.append(''.join(self.progs))
            self.basic_compute()
            self.loop += 1
        
        self.progs = current_progs
        self.level = current_level
            
    def loop_compute(self, steps):
        if self.loop == None:
            self.find_loop()
        steps = steps % self.loop
        for i in range(steps):
            self.basic_compute()
    
    def __str__(self):
        return ''.join(self.progs)
        
reader = ProtocolReader(input)
reader.basic_compute()
print("Part One : "+ str(reader))
reader.loop_compute(1000000000-1)
print("Part Two : "+ str(reader))