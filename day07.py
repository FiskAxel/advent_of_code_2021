with open('input07.txt', 'r') as puzzleInput:
	input = [*map(int, puzzleInput.read().split(','))]
	maxi, mini = max(input), min(input)
	numRange = [i for i in range(maxi + 1)]
	result, result2 = float("inf"), float("inf")
	for i in range(mini, maxi):
		sum1, sum2 = 0, 0
		for j in input:
			sum1 += abs(j - i)
			sum2 += sum(numRange[:abs(j - i) + 1])
		if sum1 < result:
			result = sum1
		if sum2 < result2:
			result2 = sum2
	print(f"Part 1: {result}")
	print(f"Part 2: {result2}") # Runs in about 20 seconds.