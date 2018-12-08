# Advent of code Year 2017 Day 7 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

progs = {} #list of programs
called = [] #list of children

#represents a program with its name, weight, parent and children as list
class prog(list):
    def __init__(self, name, weight):
        super(prog, self).__init__(self)        #The prog as a list
        self.name = name        #The prog name
        self.weight = weight    #The prog weight
        self.load = 0            #The prog load = sum of the weights above it
        self.parent = None        #The prog parent prog
        self.children = self    #Pointer to self, the list
        
    def total(self):
        return self.weight + self.load
    def __hash__(self):
        return (self.name+str(self.children)).__hash__()
        
#parses and puts every prog in progs list with its children list
for line in input.split("\n"):
    words = line.split()
    temp = prog(words[0], int((words[1].lstrip('(')).rstrip(')')))
    progs[temp.name] = temp
    if len(words) > 2:
        for sub in words[3:]:
            sub = sub.rstrip(',')
            temp.append(sub)
            called.append(sub)
            
#creates tree
for key,value in progs.items():
    for index, sub in enumerate(value):
        value[index] = progs[sub]
        progs[sub].parent = value

#cleans tree by deleting all children
for key in called:
    del progs[key]
rootname, root = progs.popitem()
#rootname = name of root, not needed
#root = root of the tree as a prog object

#each disk weight becomes the sum of itself plus all its children
def recursiveLoadCompute(disk):
    if len(disk) == 0:
        return disk.weight
    else:
        disk.load = sum([recursiveLoadCompute(child) for child in disk])
        return disk.weight + disk.load

#now we just need to check if every disk at the same level has the same weight
def findDifferent(list):
    if len(list) == 0:
        return None
    elif len(list) < 3: #1, 2 not implemented: if len = 1, can't be different from itself; if len = 2, both are different from each other and the problem can't be solved.
        return list
    else:
        A = list[0]
        B = list[1]
        for i in range(2,len(list)):
            check = list[i]
            #Case 1 : A is diff
            if check.total() != A.total() and check.total() == B.total():
                return A
            #Case 2 : B is diff
            elif check.total() == A.total() and check.total() != B.total():
                return B
            #case 3 : check is diff
            elif check.total() != A.total() and check.total() != B.total():
                return check
            #case 4 : all 3 equal, skip
        #case 5: all equals, return None
        return None
    
def loopLoadCheck(list):
    prev = list
    diff = findDifferent(list)
    while diff is not None:
        prev = diff
        diff = findDifferent(diff)
    parent = prev.parent
    for elem in parent:
        if elem.total() != prev.total():
            return prev.weight + (elem.total()-prev.total())
    

recursiveLoadCompute(root)

print("Part One : "+ root.name)
print("Part Two : "+ str(loopLoadCheck(root)))