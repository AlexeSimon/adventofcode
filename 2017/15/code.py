# Advent of code Year 2017 Day 15 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

GEN_LIMIT = 2147483647

GEN_A_START = int(input[input.find("with")+len("with "):input.find("\n")])
GEN_A_FACTOR = 16807
GEN_A_CRITERION = 4

GEN_B_START = int(input[input.rfind("with")+len("with "):])
GEN_B_FACTOR = 48271
GEN_B_CRITERION = 8

JUDGE_RANGE = 40000000
JUDGE_RANGE_CRITERION = 5000000

class Generator:
    def __init__(self, start, factor, criterion):
        self.start = start
        self.factor = factor
        self.criterion = criterion
        self.output = (start * factor) % GEN_LIMIT
    
    def next(self):
        self.output = (self.output * self.factor) % GEN_LIMIT
    
    def next_criterion(self):
        self.output = (self.output * self.factor) % GEN_LIMIT
        while (self.output % self.criterion) != 0 :
            self.output = (self.output * self.factor) % GEN_LIMIT
    
    def init_criterion(self):
        while (self.output % self.criterion) != 0 :
            self.output = (self.output * self.factor) % GEN_LIMIT

class Judge:
    def __init__(self, gen_A, gen_B):
        self.val = 0
        self.gen_A = gen_A
        self.gen_B = gen_B
        self.print_header = True
    
    def print_val(self):
        print("Judge counter = " + str(self.val))
        self.print_header = True
    
    def print_gens(self):
        if (self.print_header):
            self.print_header = False
            print("--Gen. A--  --Gen. B--")
        print("{:10d}".format(self.gen_A.output) + "  " + "{:10d}".format(self.gen_B.output))    
    
    def step(self):
        self.gen_A.next()
        self.gen_B.next()
    
    def step_criterion(self):
        self.gen_A.next_criterion()
        self.gen_B.next_criterion()
    
    def init_criterion(self):
        self.gen_A.init_criterion()
        self.gen_B.init_criterion()
    
    def compare(self):
        if "{:0>32b}".format(gen_A.output)[16:32] == "{:0>32b}".format(gen_B.output)[16:32]:
            self.val += 1
    
gen_A = Generator(GEN_A_START, GEN_A_FACTOR, GEN_A_CRITERION)
gen_B = Generator(GEN_B_START, GEN_B_FACTOR, GEN_B_CRITERION)
judge = Judge(gen_A, gen_B)

for i in range(JUDGE_RANGE):
    #judge.print_gens()
    judge.compare()
    judge.step()
print("Part One : "+ str(judge.val))

gen_A = Generator(GEN_A_START, GEN_A_FACTOR, GEN_A_CRITERION)
gen_B = Generator(GEN_B_START, GEN_B_FACTOR, GEN_B_CRITERION)
judge = Judge(gen_A, gen_B)
judge.init_criterion()

for i in range(JUDGE_RANGE_CRITERION):
    #judge.print_gens()
    judge.compare()
    judge.step_criterion()
print("Part Two : "+ str(judge.val))