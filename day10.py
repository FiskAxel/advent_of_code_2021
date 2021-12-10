def main():
	with open('input10.txt', 'r') as puzzleInput:
		result = 0
		result2 = []
		for i in puzzleInput.readlines():
			stack = []
			for j, c in enumerate(i):
				if c in "([{<":
					stack.append(c)
				elif c in ")]}>":
					dif = ord(c) - ord(stack.pop()) # ( and ) are 1 away in unicode. The rest of the pairs are 2 away.
					if dif != 1 and dif != 2: 
						result += score(c)
						break
				if j == len(i) - 1 and len(stack) > 0:
					s = 0
					while(len(stack) > 0):
						s = score2(s, stack.pop())
					result2.append(s)
		print(f"Part 1: {result}")
		result2.sort()
		print(f"Part 2: {result2[int(len(result2) / 2)]}")

def score(c):
	if c == ')': return 3
	if c == ']': return 57
	if c == '}': return 1197
	if c == '>': return 25137
def score2(s, c):
	s *= 5
	if c == '(': return s + 1
	if c == '[': return s + 2
	if c == '{': return s + 3
	if c == '<': return s + 4

main()