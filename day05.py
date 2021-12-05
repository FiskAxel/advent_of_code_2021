import re
with open('input05.txt', 'r') as puzzleInput:
	input = puzzleInput.readlines()
	p = re.compile("(\d+),(\d+) -> (\d+),(\d+)")
	map = {}
	
	for i in input:
		a = [int(n) for n in p.findall(i)[0]]
		x1, y1, x2, y2 = a[0], a[1], a[2], a[3]
		if x1 > x2:
			x1, x2 = a[2], a[0]
		if y1 > y2:
			y1, y2 = a[3], a[1]
		if x1 == x2 or y1 == y2: # Horizontal & Vertical
			for y in range(y1, y2 + 1):
				for x in range(x1, x2 + 1):
					key = f"{x},{y}"
					if key in map:
						map[key] += 1
					else:
						map[key] = 1
	result = 0					
	for i in map:
		if map[i] > 1:
			result += 1
	print(f"Part 1: {result}")
	
	for i in input:
		a = [int(n) for n in p.findall(i)[0]]
		x1, y1, x2, y2 = a[0], a[1], a[2], a[3]
		dx, dy = 1, 1
		if x1 > x2:
			dx = -1
		if y1 > y2:
			dy = -1
		if x1 != x2 and y1 != y2: # Diagonal
			while True:
				key = f"{x1},{y1}"
				if key in map:
					map[key] += 1
				else:
					map[key] = 1
				if x1 == x2:
					break
				x1 += dx
				y1 += dy
	result = 0					
	for i in map:
		if map[i] > 1:
			result += 1
	print(f"Part 2: {result}")