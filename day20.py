from math import sqrt
def main():
	with open('input20.txt', 'r') as puzzleInput:
		IEA = puzzleInput.readline()
		puzzleInput.readline()
		img = {}
		for y, i in enumerate(puzzleInput.readlines()):
			for x, j in enumerate(i.strip()):
				img[x, y] = j
		img = enhance(img, IEA, False)
		img = enhance(img, IEA, True)
		print(f"Part 1: {onCount(img)}")
		
		for _ in range(24):
			img = enhance(img, IEA, False)
			img = enhance(img, IEA, True)
		print(f"Part 2: {onCount(img)}") # Runs in about 10 seconds

def enhance(img, iea, infLit):
	l = int(sqrt(len(img))) + 1
	newImg = {}
	for y in range(-1, l):
		for x in range(-1, l):
			binStr = ''
			for i in range(-1, 2):
				for j in range(-1, 2):
					if (x + j, y + i) not in img:
						if iea[0] == '.' or not infLit:
							binStr += '0'
						else: binStr += '1'
					elif img[x + j, y + i] == '#':
						binStr += '1'
					else: binStr += '0'
			b = int(binStr, 2)
			newImg[x + 1, y + 1] = iea[b] # +1 to make the top left corner 0,0
	return newImg
def onCount(img):
	count = 0
	for p in img:
		if img[p] == '#':
			count += 1
	return count

def printImg(img):
	print()
	l = int(sqrt(len(img)))
	for y in range(l):
		for x in range(l):
			print(img[x, y], end="")
		print()

main()