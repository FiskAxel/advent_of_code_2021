def main():
	with open('input06.txt', 'r') as puzzleInput:
		input = puzzleInput.readline().split(',')
		fishies = list(map(input.count, "012345678"))
		print(f"Part 1: {countFishies(fishies, 80)}")
		print(f"Part 2: {countFishies(fishies, 256 - 80)}")

def countFishies(fishies, days):
	for _ in range(days):
		s = fishies.pop(0) # Give birth
		fishies[6] += s # Baby-fishies
		fishies.append(s) # Baby-fish-mother-fishies
	return sum(fishies)

main()