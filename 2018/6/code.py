# Advent of code Year 2018 Day 6 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().split("\n")

# By turning the problem around (starting from the coordinates and expanding through the territory) it was actually a lot more complicated to code but the end result is a lot more optimized and interesting.

class Coordinate:
    def __init__ (self, x, y, id, territory):
        self.x = x
        self.y = y
        self.id = id
        self.infinite = False
        self.size = 0
        self.territory = territory
        
    def recursive_expend(self, x, y, dist, going_up, going_right, state, dist_left):
        if state and dist_left > 0:
                if going_up :
                    self.recursive_expend(x, y+1, dist+1, going_up, going_right, self.territory.claim(x, y+1, self, dist+1), dist_left-1)
                if not going_up :
                    self.recursive_expend(x, y-1, dist+1, going_up, going_right, self.territory.claim(x, y-1, self, dist+1), dist_left-1)
                if going_right:
                    self.recursive_expend(x+1, y, dist+1, going_up, going_right, self.territory.claim(x+1, y, self, dist+1), dist_left-1)
                if not going_right:
                    self.recursive_expend(x-1, y, dist+1, going_up, going_right, self.territory.claim(x-1, y, self, dist+1), dist_left-1)
                
        
    def expend(self, max_dist = float('inf')):
        self.recursive_expend(self.x+1, self.y, 1, False, True, self.territory.claim(self.x+1, self.y, self, 1), max_dist-1)
        self.recursive_expend(self.x, self.y+1, 1, True, True, self.territory.claim(self.x, self.y+1, self, 1), max_dist-1)
        self.recursive_expend(self.x-1, self.y, 1, True, False, self.territory.claim(self.x-1, self.y, self, 1), max_dist-1)
        self.recursive_expend(self.x, self.y-1, 1, False, False, self.territory.claim(self.x, self.y-1, self, 1), max_dist-1)
        
class Territory:
    def __init__(self, min_x, max_x, min_y, max_y):
        self.distance = [[-1 for y in range(max_y-min_y+1)] for x in range(max_x-min_x+1)]
        self.ownership = [[None for y in range(max_y-min_y+1)] for x in range(max_x-min_x+1)]
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
    
    def claim(self, x, y, owner, dist):
        if x <= self.max_x and x >= self.min_x and y >= self.min_y and y <= self.max_y:
            if self.distance[x-self.min_x][y-self.min_y] == -1:
                self.distance[x-self.min_x][y-self.min_y] = dist
                self.ownership[x-self.min_x][y-self.min_y] = owner
                owner.size += 1
                return True 
            elif self.ownership[x-self.min_x][y-self.min_y] == owner:
                if dist < self.distance[x-self.min_x][y-self.min_y]:
                    self.distance[x-self.min_x][y-self.min_y] = dist
                    return True
                else:
                    return False
            
            elif dist < self.distance[x-self.min_x][y-self.min_y]:
                self.distance[x-self.min_x][y-self.min_y] = dist
                if self.ownership[x-self.min_x][y-self.min_y] != None:
                    self.ownership[x-self.min_x][y-self.min_y].size -= 1
                self.ownership[x-self.min_x][y-self.min_y] = owner
                owner.size += 1
                return True
            elif dist == self.distance[x-self.min_x][y-self.min_y]:
                if self.ownership[x-self.min_x][y-self.min_y] != None:
                    self.ownership[x-self.min_x][y-self.min_y].size -= 1
                    self.ownership[x-self.min_x][y-self.min_y] = None
                return False
            else:
                return False
            
        else: 
            return False
            
                    
                
coordinates = [Coordinate(int(line[:line.find(',')]), int(line[line.find(',')+2:]), idx, None) for idx, line in enumerate(input)]
    
max_x = max(coordinates, key = lambda coord : coord.x).x
min_x = min(coordinates, key = lambda coord : coord.x).x
min_y = min(coordinates, key = lambda coord : coord.y).y
max_y = max(coordinates, key = lambda coord : coord.y).y

territory = Territory(min_x, max_x, min_y, max_y)

for coord in coordinates:
    coord.territory = territory
    coord.territory.claim(coord.x, coord.y, coord, 0)

for coord in coordinates:
    coord.expend()

# set all 4 borders to infinity :
for i in range(max_x-min_x+1):
    if territory.ownership[i][0] != None:
        territory.ownership[i][0].infinite = True
    if territory.ownership[i][max_y-min_y] != None:
        territory.ownership[i][max_y-min_y].infinite = True
for i in range(max_y-min_y+1):
    if territory.ownership[0][i] != None:
        territory.ownership[0][i].infinite = True
    if territory.ownership[max_x-min_x][i] != None:
        territory.ownership[max_x-min_x][i].infinite = True

# Find biggest, not infinite
best_size = 0
for coord in coordinates:
    if not coord.infinite:
        if coord.size > best_size:
            best_size = coord.size

print("Part One : "+ str(best_size))

# Quick sum of all manhattan distances abusing masks and lists instead of loops
def quick_man(x, y, x_sorted, y_sorted):
    x_mask = [1 if x > i else -1 for i in x_sorted]
    y_mask = [1 if y > i else -1 for i in y_sorted]
    return sum(x_mask)*x + sum(y_mask)*y - sum([i*j for i,j in zip(x_sorted,x_mask)]) - sum([i*j for i,j in zip(y_sorted,y_mask)])
    
x_sorted = sorted([coord.x for coord in coordinates])
y_sorted = sorted([coord.y for coord in coordinates])

total_good = 0
for i in range(min_x, max_x):
    for j in range(min_y, max_y):
        if quick_man(i, j, x_sorted, y_sorted) < 10000:
            total_good += 1

print("Part Two : "+ str(total_good))

# if you want to print the areas distances, it's pretty beautiful
with open((__file__.rstrip("code.py")+"output.txt"), 'w+') as output_file:
    for i in range(max_x-min_x+1):
        for j in range(max_y-min_y+1):
            output_file.write('{0:3d} '.format(territory.distance[i][j]))
        output_file.write("\n")