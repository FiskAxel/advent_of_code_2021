def main():
	with open('input15.txt', 'r') as puzzleInput:
		grid = [[int(j) for j in i.strip()] for i in puzzleInput.readlines()]
	print(f"Part 1: {aStar(grid)}") # Runs in about 10 seconds
	expand(grid)
	print(f"Part 2: {aStar(grid)}") # Runs in about 15 minutes :'(

tx, ty = 0, 0
class queItem:
	def __init__(self, x, y, cost, path):
		self.x = x
		self.y = y
		self.cost = cost # From entrance
		self.hCost = h(x, y) # Lowest estimated cost from here to target (result of heuristic function)
		self.path = path
def aStar(grid):
	global tx, ty
	tx, ty = len(grid[0]) - 1, len(grid) - 1
	que = [queItem(0, 0, 0, [])]
	bestVisits = {}
	while True:
		q = que[0]
		x, y, cost, path = q.x, q.y, q.cost, q.path
		if x == tx and y == ty:
			return cost
		k = key(x, y)
		if k in bestVisits and bestVisits[k] <= cost:
			que.remove(q)
			continue
		bestVisits[k] = cost
		for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
			nx, ny = x + dx, y + dy
			if 0 <= nx <= tx and 0 <= ny <= ty:
				nPath = path.copy()
				nPath.append(key(nx, ny))
				que.append(queItem(nx, ny, cost + grid[nx][ny], nPath))
		que.remove(q)
		que.sort(key=lambda i: i.cost + i.hCost)
def h(x, y):
	return abs(tx - x) + abs(ty - y)
def key(x, y):
	return str(x) + ',' + str(y)

def expand(grid):
	L = len(grid)
	gridVariants = []
	gridVariants.append(grid)
	for _ in range(8):
		newGrid = createNewGrid(gridVariants[-1])
		gridVariants.append(newGrid)
	# 1st column
	for i in range(1, 5):
		for row in gridVariants[i]:
			grid.append(row)
	# Compleating each row
	for i in range(0, 5):
		for j in range(1, 5):
			for k, row in enumerate(gridVariants[i + j]):
				grid[L * i + k] += row
def createNewGrid(grid):
	newGrid = []
	for y in grid:
		row = []
		for x in y:
			v = (x + 1) % 10
			if v == 0: v = 1
			row.append(v)
		newGrid.append(row)
	return newGrid

main()