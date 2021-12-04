with open('input01.txt', 'r') as puzzleInput:
	input = [int(i) for i in puzzleInput.readlines()]
	result = 0
	prev = input[0]
	for i in input:
		if i > prev:
			result += 1
		prev = i
	print(f"Part 1: {result}")
	
	tM = [0, 0]
	for i in input:
		for j in range(len(tM) - 2, len(tM)):
			tM[j] += i
		tM.append(i)
	result = 0
	prev = tM[2]
	for i in range(3, len(tM) - 2):
		if tM[i] > prev:
			result += 1
		prev = tM[i]
	print(f"Part 2: {result}")
	
	d = input
	print(len([i for i in range(1, len(d)) if d[i] > d[i - 1]]))
	print(len([i for i in range(2, len(d)) if d[i - 2] + d[i - 1] + d[i] > d[i - 3] + d[i - 2] + d[i - 1]]))