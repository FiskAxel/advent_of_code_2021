input = []
with open('input24.txt', 'r') as puzzleInput:
	p = puzzleInput.readlines()
	for i in range(14):
		if p[i * 18 + 4] == "div z 26\n":
			input.append(int(p[i * 18 + 5][6:].strip()))
		else:
			input.append(int(p[i * 18 + 15][6:].strip()))	

def getValidNum(mNum, downOrUp):
	while True:	
		z = 0
		for i in range(14):
			if input[i] > 0:
				z *= 26
				z += input[i] + mNum[i]
			elif z % 26 + input[i] != mNum[i]:
				downOrUp(mNum, i)
				break
			else:
				z = int(z / 26)
		if i == 13:
			if z != 0:
				downOrUp(mNum, i)
			else:
				break
	return ''.join([str(i) for i in mNum])
def down(mNum, i):
	mNum[i] -= 1
	if mNum[i] == 0:
		mNum[i] = 9
		down(mNum, i - 1)	
def up(mNum, i):
	mNum[i] += 1
	if mNum[i] == 10:
		mNum[i] = 1
		up(mNum, i - 1)

print(f"Part 1: {getValidNum([9 for _ in range(14)], down)}") # runs in about 15 seconds
print(f"Part 2: {getValidNum([1 for _ in range(14)], up)}")