# Advent of code Year 2018 Day 8 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [int(elem) for elem in input_file.read().split(" ")]

type = [0 for i in range(len(input))]
# 0 means not computed
# 1 means info node -> always followed by 2 and thus skipped in recursive calls
# 2 means info meta -> can be followed by 1 or 3
# 3 means data -> can be followed by 1 or 3

class Node:
    def __init__(self, idx, info_node, info_data):
        self.idx = idx
        self.info_node = info_node
        self.info_data = info_data
        self.children_nodes = []
        self.metadata = []
    

def recursive_identify(idx, nodes_left, data_left, node):
    if nodes_left > 0: # idx is a children node
        while nodes_left > 0:
            type[idx] = 1
            type[idx+1] = 2
            next_node = Node(idx, input[idx], input[idx+1])
            node.children_nodes.append(next_node)
            idx = recursive_identify(idx+2, input[idx], input[idx+1], next_node)
            nodes_left -= 1
        
    if data_left > 0: # idx is metadata
        while data_left > 0:
            type[idx] = 3
            node.metadata.append(input[idx])
            idx += 1
            data_left -= 1
    
    return idx
        


type[0] = 1
type[1] = 2
root = Node(0, input[0], input[1])
recursive_identify(2, input[0], input[1], root)

sum1 = 0
for i in range(len(input)):
    if type[i] == 3:
        sum1 += input[i]

# Use a dictionary of weights already computed to avoid unnecessary work
weight = {}
def recursive_sum(node):
    if node.idx in weight: # already computed
        return weight[node.idx]
        
    if node.info_node == 0: # no children, weight is sum of metadata
        weight[node.idx] = sum(node.metadata)
        return weight[node.idx]
        
    rec_sum = 0
    for i in node.metadata: # for each meta data call
        if i > 0 and i <= node.info_node: # if it is valid (we ignore 0)
            rec_sum += recursive_sum(node.children_nodes[i-1]) # add its weight to self weight
    weight[node.idx] = rec_sum
    return rec_sum
 
print("Part One : "+ str(sum1))
print("Part Two : "+ str(recursive_sum(root)))

# If you want to print to file the data and its type
# with open((__file__.rstrip("code.py")+"output.txt"), 'w+') as output_file:
    # output_file.write(''.join(['{:2d} '.format(t) for t in input]))
    # output_file.write("\n")
    # output_file.write(''.join(['{:2d} '.format(t) for t in type]))
    
    