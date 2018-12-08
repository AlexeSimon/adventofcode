# Advent of code Year 2017 Day 19 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()


class MazeRunner:
    def __init__(self, source):
        self.source = source
        self.maze = [line.rstrip('\n') for line in source.split("\n")]
        self.hist = []
        self.posx = 0
        self.posy = 0
        self.vel = "stuck" # "down", "right", "left", "up", "stuck"
        self.steps = 0
        self.findEntry()
    
    def step(self):
        if self.vel == "down":
            self.posy += 1
        elif self.vel == "up":
            self.posy -= 1
        elif self.vel == "right":
            self.posx += 1
        elif self.vel == "left":
            self.posx -= 1
        self.steps += 1
    
    def findEntry(self):
        while self.maze[self.posy][self.posx] != '|':
            self.posx += 1
        self.vel = "down"
    
    def changeVel(self):
        searching = True
        if searching and self.posx+1 < len(self.maze[self.posy]):
            if self.maze[self.posy][self.posx+1] == '-' and self.vel != "left":
                self.vel = "right"
                searching = False
                
        if searching and self.posx-1 > 0:    
            if self.maze[self.posy][self.posx-1] == '-' and self.vel != "right":
                self.vel = "left"
                searching = False
                
        if searching and self.posy+1 < len(self.maze):
            if self.maze[self.posy+1][self.posx] == '|' and self.vel != "up":
                self.vel = "down"
                searching = False
                
        if searching and self.posy-1 > 0:
            if self.maze[self.posy-1][self.posx] == '|' and self.vel != "down":
                self.vel = "up"
                searching = False
                
        if searching:
            self.vel = "stuck"
    
    def walkThrough(self):
        while self.vel != "stuck":
            while self.maze[self.posy][self.posx] in ['|','-']:
                self.step()
            if self.maze[self.posy][self.posx] == '+':
                self.changeVel()
                self.step()
            elif self.maze[self.posy][self.posx] == ' ':
                return 1
            else:
                self.hist.append(self.maze[self.posy][self.posx])
                self.step()
        return 0
            
    
maze = MazeRunner(input)
maze.walkThrough()

print("Part One : "+ ''.join(maze.hist))
print("Part Two : "+ str(maze.steps))