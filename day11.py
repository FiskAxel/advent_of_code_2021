def main():
	with open('input11.txt', 'r') as puzzleInput:
		grid = [[int(c) for c in i] for i in [r.strip() for r in puzzleInput.readlines()]]
		part1, steps = 0, 0
		flashes = []
		while len(flashes) != 100:
			flashes, check = [], []
			for y in range(10):
				for x in range(10):
					part1 += update(grid, y, x, check, flashes)
			for i in check:
				y, x = i[0], i[1]
				if y < 0 or 10 <= y or x < 0 or 10 <= x or [y, x] in flashes:
					continue
				part1 += update(grid, y, x, check, flashes)
			steps += 1
			if steps == 100:
				print(f"Part 1: {part1}")	
		print(f"Part 2: {steps}")

def update(grid, y, x, check, flash):
	grid[y][x] += 1
	if grid[y][x] > 9:
		grid[y][x] = 0
		flash.append([y, x])
		addNeighboursToCheck(check, y, x)
		return 1
	return 0
def addNeighboursToCheck(check, y, x):
	check.append([y - 1, x - 1])
	check.append([y - 1, x])
	check.append([y - 1 , x + 1])
	check.append([y, x - 1])
	check.append([y, x + 1])
	check.append([y + 1, x - 1])
	check.append([y + 1, x])
	check.append([y + 1, x + 1])

main()