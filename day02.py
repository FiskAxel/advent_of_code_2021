with open('input02.txt', 'r') as puzzleInput:
	input = puzzleInput.readlines()
	depth = 0
	horizontal = 0
	for i in input:
		p = i.split()
		if p[0] == 'forward':
			horizontal += int(p[1])
		elif p[0] == 'down':
			depth += int(p[1])
		elif p[0] == 'up':
			depth -= int(p[1])
	result = horizontal * depth
	print(f"Part 1: {result}")

	aim = 0
	depth = 0
	horizontal = 0
	for i in input:
		p = i.split()
		if p[0] == 'forward':
			horizontal += int(p[1])
			depth += int(p[1]) * aim
		elif p[0] == 'down':
			aim += int(p[1])
		elif p[0] == 'up':
			aim -= int(p[1])
	result = horizontal * depth
	print(f"Part 2: {result}")