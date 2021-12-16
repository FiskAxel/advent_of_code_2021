def main():
	with open('input15.txt', 'r') as puzzleInput:
		grid = [[int(j) for j in i.strip()] for i in puzzleInput.readlines()]
	print(f"Part 1: {aStar(grid)}") # Runs in about 10 seconds
	expand(grid)
	print(f"Part 2: {aStar(grid)}") # Runs in about 15 minutes :'(

tx, ty = 0, 0
def aStar(grid):
	global tx, ty
	tx, ty = len(grid[0]) - 1, len(grid) - 1
	que = [[0, 0, 0, h(0, 0)]]
	bestVisits = {}
	while True:
		q = que[0]
		x, y, cost = q[0], q[1], q[2]
		if x == tx and y == ty:
			return cost
		k = str(x) + ',' + str(y)
		if k in bestVisits and bestVisits[k] <= cost:
			que.remove(q)
			continue
		bestVisits[k] = cost
		for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
			nx, ny = x + dx, y + dy
			if 0 <= nx <= tx and 0 <= ny <= ty:
				que.append([nx, ny, cost + grid[nx][ny], h(nx, ny)])
		que.remove(q)
		que.sort(key=lambda i: i[2] + i[3])
def h(x, y):
	return abs(tx - x) + abs(ty - y)

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