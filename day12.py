caves = {}
def main():
	with open('input12.txt', 'r') as puzzleInput:
		for i in puzzleInput.readlines():
			a, b = i.strip().split('-')
			if a not in caves: caves[a] = []
			if b not in caves: caves[b] = []
			caves[a].append(b)
			caves[b].append(a)
	print(f"Part 1: {findPaths(False)}")
	print(f"Part 2: {findPaths(True)}") # Runs in about 5 seconds.

def findPaths(part2):
	paths = []
	que = [['start']]
	for path in que:
		location = path[len(path) - 1]
		if location == 'end':
			paths.append(path)
			continue
		for cave in caves[location]:
			if cave == 'start': continue
			if ord(cave[0]) < 90 or cave not in path or (part2 and not lowerCaseTwice(path)):
				c = path.copy()
				c.append(cave)
				que.append(c)

	return len(paths)
def lowerCaseTwice(path):
	visited = []
	for i in path:
		if i == 'start': continue
		if ord(i[0]) >= 97:
			if i in visited:
				return True
			visited.append(i)
	return False

main()