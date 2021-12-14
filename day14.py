rules = {}
def main():
	with open('input14.txt', 'r') as puzzleInput:
		t = puzzleInput.readline().strip()
		puzzleInput.readline()
		for i in puzzleInput.readlines():
			key, c = i.split(' -> ')
			rules[key] = c.strip()
	pairs = {}
	for i in rules: pairs[i] = 0
	for i in range(len(t) - 1): pairs[t[i] + t[i + 1]] += 1
	for _ in range(10): pairs = step(pairs)
	print(f"Part 1: {result(pairs, t)}")
	for _ in range(30): pairs = step(pairs)
	print(f"Part 2: {result(pairs, t)}")

def step(pairs):
	newPairs = {}
	for p in pairs: newPairs[p] = 0
	for p in pairs:
		newPairs[p[0] + rules[p]] += pairs[p]
		newPairs[rules[p] + p[1]] += pairs[p]	
	return newPairs
def result(pairs, t):
	sums = {}
	for p in pairs: sums[p[0]] = 0
	for p in pairs:
		sums[p[0]] += pairs[p]
		sums[p[1]] += pairs[p]
	# In the loop every character is counted twice except the first and the last.
	sums[t[0]] += 1 # First
	sums[t[len(t) - 1]] += 1 # Last
	c = [sums[i] for i in sums]
	return int((max(c) - min(c)) / 2)

main()