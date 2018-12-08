# Advent of code Year 2017 Day 12 solution
# Author = Alexe Simon
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()


class Node:
	nodeList = {}
	
	def __init__(self, id, connection):
		if id in Node.nodeList:
			#update only
			self = Node.nodeList[id]
		else:
			#makenew
			self.id = id
			self.direct = [self] #self is directly reachable by logic
			self.family = id
			Node.nodeList[id] = self
			
		for subnode in connection:
			if subnode not in Node.nodeList:
				Node.nodeList[subnode] = Node(subnode, [id])
				self.direct.append(Node.nodeList[subnode])
			else:
				if Node.nodeList[subnode] not in self.direct:
					self.direct.append(Node.nodeList[subnode])
		
		self.family = min([sub.family for sub in self.direct])
		
	def __repr__(self):
		return str(self.id)
	
	def updateFamilies():
		queue = [value for key, value in Node.nodeList.items()]
		while len(queue) > 0:
			temp = queue.pop()
			prev = temp.family
			temp.family = min([sub.family for sub in temp.direct])
			if prev != temp.family:
				for sub in temp.direct:
					queue.insert(0,sub)
		
	def getFamilySize(familyId):
		count = 0
		for key, value in Node.nodeList.items():
			if value.family == familyId:
				count += 1
		return count
	
	def countFamilies():
		families = []
		for key, value in Node.nodeList.items():
			if value.family not in families:
				families.append(value.family)
		return len(families)
	
	def getFamilyNames():
		families = []
		for key, value in Node.nodeList.items():
			if value.family not in families:
				families.append(value.family)
		return families
	
	def getFamily(familyName):
		family = []
		for key, value in Node.nodeList.items():
			if value.family == familyName:
				family.append(value)
		return family
		
for line in input.split("\n"):
	words = line.split()
	Node(int(words[0]), [int(word.rstrip(",")) for word in words[2:]])

Node.updateFamilies()

# Uncomment this if you want to print all families
# for name in Node.getFamilyNames():
	# family = Node.getFamily(name)
	# print("Family "+str(name)+" ("+str(len(family))+"): " + str(family))
	
print("Part One : "+ str(Node.getFamilySize(0)))
print("Part Two : "+ str(Node.countFamilies()))