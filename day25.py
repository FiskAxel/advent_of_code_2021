def main():
	with open('input25.txt', 'r') as puzzleInput:
		map = [[j for j in i.strip()] for i in puzzleInput]
		result = 0
		while True:
			result += 1
			if step(map) == "none":
				break
		print(f"Part 1: {result}") # Runs in under 10 seconds.

def step(map):
	east = []
	for y, row in enumerate(map):
		for x, j in enumerate(row):
			if j == '>' and map[y][(x + 1) % len(map[0])] == '.':
				east.append([x, y])
	for i in east:
		map[i[1]][i[0]] = '.'
		map[i[1]][(i[0] + 1) % len(map[0])] = '>'
	
	south = []
	for y, row in enumerate(map):
		for x, j in enumerate(row):
			if j == 'v' and map[(y + 1) % len(map)][x] == '.':
				south.append([x, y])
	for i in south:
		map[i[1]][i[0]] = '.'
		map[(i[1] + 1) % len(map)][i[0]] = 'v'

	if len(east) == 0 and len(south) == 0:
		return "none"

main()