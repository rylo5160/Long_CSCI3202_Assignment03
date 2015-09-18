import sys

tile_open = 0
tile_mountain = 1
tile_wall = 2

cost_adjacent = 10
cost_mountain = 10
cost_diagonal = 14

class node:
	def _init_(self, parent, location):
		self.parent = parent
		self.location = location
		self.f = none
		self.g = none
		self.h = none
	
def manhattan(startRow, startCol, endRow, endCol):
	return ((abs(endRow - startRow), abs(endCol - startCol)) * 10)
	
def customHeuristic(startRow, startCol, endRow, endCol):
	x = (endRow - startRow)
	y = (endCol - startCol)
	if x < y:
		return abs((x * 14) + ((y - x) * 10))
	if y > x:
		return abs((x * 10) + ((x - y) * 10))

def adjacent(row, col, maxRow, maxCol):
	neighbor = []
	if col >= 0:
		if (col - 1) >= 0:
			neighbor.append(row, (col - 1))
		if (col + 1) < maxCol:
			neighbor.append(row, (col + 1))
	if row >= 0:
		if (row - 1) >= 0:
			neighbor.append((row - 1), col)
		if (row + 1) < maxRow:
			neighbor.append((row + 1), col)
	return neighbor
			
	
def diagonal(row, col, maxRow, maxCol):
	neighbor = []
	if (col - 1) >= 0:
		if (row - 1) >= 0:
			neighbor.append((row - 1), (col - 1))
		if (row + 1) < maxRow:
			neighbor.append((row + 1), (col - 1))
	if (col + 1) < maxCol:
		if (row - 1) >= 0:
			neighbor.append((row - 1), (col + 1))
		if (row + 1) < maxRow:
			neighbor.append((row + 1), (col + 1))
	return neighbor

def aStarSearch(start, end, world):
	listClosed = []
	listOpen = []
	
	rootNode.h = heuristic.chosen(start, goal)
	rootNode.g = 0
	rootNode.f = rootNode.h
	listOpen.append(start)
	while len(listOpen) != 0:
		currentNode = minCost(listOpen)
		if currentNode == end:
			return currentNode
			listClosed.append(currentNode)
			for nextLocation in world[currentNode.location]:
				nextNode = node(currentNode, nextLocation)
				nextNode.g = currentNode.g + cost
				nextNode.h = Heuristic.chosen(nextNode.location, goal)
				nextNode.f = nextNode.g + nextNode.h
				if nextNode.location == goal:
					listClosed.append(nextNode)
					return (nextNode, len(listClosed))
	return None
		
def main(argv):
	world = open(filename)
	return None
