# Advent of code Year 2018 Day 7 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# input = """Step C must be finished before step A can begin.
# Step C must be finished before step F can begin.
# Step A must be finished before step B can begin.
# Step A must be finished before step D can begin.
# Step B must be finished before step E can begin.
# Step D must be finished before step E can begin.
# Step F must be finished before step E can begin."""

class Step:
    def __init__(self, name):
        self.parent = []
        self.children = []
        self.name = name
        self.time = 60 + 1 + ord(self.name) - ord('A')
    
    def is_ready(self):
        return len(self.parent) == 0
    
    def __lt__(self, other):
        return self.name < other.name
        
def link(parent_step, child_step):
        parent_step.children.append(child_step)
        child_step.parent.append(parent_step)

def init(input):
    steps = {}
    for line in input.split("\n"):
        words = line.split()
        parent = words[1]
        child = words[7]
        if parent not in steps:
            steps[parent] = Step(parent)
        if child not in steps:
            steps[child] = Step(child)
        link(steps[parent], steps[child])
    return steps


def insert_sorted_letter(steps_list, step):
    i = 0
    while(i < len(steps_list) and steps_list[i] < step):
        i += 1
    steps_list.insert(i, step)
    
steps = init(input)
available = []
done = []
    
for step in list(steps.values()):
    if step.is_ready():
        insert_sorted_letter(available, step)

while len(available) > 0:
    next = available.pop(0)
    done.append(next.name)
    for child in next.children:
        child.parent.remove(next)
        if child.is_ready():
            insert_sorted_letter(available, child)

print("Part One : "+ ''.join(done))

### Part Two : reset data

steps = init(input)
available = []
done = []
t = 0
workers = []

# Fill available 
for step in list(steps.values()):
    if step.is_ready():
        insert_sorted_letter(available, step)

# Give job to workers
while available and len(workers) < 5:
        workers.append(available.pop(0))   
        
while available or workers:
    i = 0
    while i < len(workers):
        work = workers[i]
        work.time -= 1
        if work.time == 0:
            workers.remove(work)
            for child in work.children:
                child.parent.remove(work)
                if child.is_ready():
                    insert_sorted_letter(available, child)
        else:
            i += 1
        
    while available and len(workers) < 5:
        workers.append(available.pop(0))   
    t += 1

print("Part Two : "+ str(t))