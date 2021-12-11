lowpoints = []
def main():
	with open('input09.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		field = []
		for y in input:
			field.append([int(i) for i in y.strip()])
		lowPointRiskLevelSum = 0
		for y, r in enumerate(field):
			for x, v in enumerate(r):
				if y == 0 or v < field[y - 1][x]:
					if x == 0 or v < field[y][x - 1]:
						if y == len(field) - 1 or v < field[y + 1][x]:
							if x == len(r) - 1 or v < field[y][x + 1]:
								lowPointRiskLevelSum += 1 + v
								lowpoints.append([y, x])
		print(f"Part 1: {lowPointRiskLevelSum}")

		b = []
		for p in lowpoints:
			b.append(basinSize(field, p[0], p[1]))
		b.sort()
		print(f"Part 2: {b.pop() * b.pop() * b.pop()}")

visited = []
def basinSize(f, y, x):
	v = f[y][x]
	if v == 9 or [y, x] in visited:
		return 0
	visited.append([y, x])
	count = 1
	if y != 0 and v < f[y - 1][x]:
		count += basinSize(f, y - 1, x)
	if y != len(f) - 1 and v < f[y + 1][x]:
		count += basinSize(f, y + 1, x)
	if x != len(f[y]) - 1 and v < f[y][x + 1]:
		count += basinSize(f, y, x + 1)
	if x != 0 and v < f[y][x - 1]:
		count += basinSize(f, y, x - 1)
	return count

main()