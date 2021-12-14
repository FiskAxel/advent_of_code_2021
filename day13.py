dots = []
def main():
	with open('test.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		for i, c in enumerate(input):
			if c == '\n':
				folds = input[i + 1:]
				folds = [j.split()[2].split('=') for j in folds]
				break
			dots.append([int(xy) for xy in c.strip().split(',')])	
		fold(folds)
		print(f"Part 1: {len(dots)}")
		for _ in range(len(folds)): fold(folds)
		print(f"Part 2:")
		printDots()

def fold(folds):
	xy, n = folds.pop(0)
	n = int(n)
	remove = []
	for i in dots:
		x, y = i
		if xy == 'x':
			if x < n: 
				continue
			remove.append(i)
			x = n - (x - n)
			new = [x, y]
			if new not in dots:
				dots.append(new)
		if xy == 'y':
			if y < n: 
				continue
			remove.append(i)
			y = n - (y - n)
			new = [x, y]
			if new not in dots:
				dots.append(new)
	for i in remove:
		dots.remove(i)
def printDots():
	dots.sort()
	xMin, xMax = dots[0][0], dots[len(dots) - 1][0]
	dots.sort(key=lambda i : i[1])
	yMin, yMax = dots[0][1], dots[len(dots) - 1][1]
	for y in range(yMin, yMax + 1):
		row = ""
		for x in range(xMin, xMax + 1):
			if [x, y] in dots:
				row += '#'
			else:
				row += '.'
		print(row)
		
main()