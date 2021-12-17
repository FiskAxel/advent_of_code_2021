x1, x2, y1, y2 = 195, 238, -93, -67
def main():
	result, result2 = 0, 0
	for x in range(x2 + 1):
		for y in range(y1, 100):
			topHeight = shoot(x, y)
			if result < topHeight:
				result = topHeight
			if topHeight >= 0:
				result2 += 1
	print(f"Part 1: {result}")
	print(f"Part 2: {result2}")

def shoot(a, b):
	top = 0
	x, y, vx, vy = a, b, a, b
	while x <= x2 and y >= y1:
		if top < y:
			top = y
		if inTarget(x, y):
			return top
		vx = toZero(vx)
		vy -= 1
		x += vx
		y += vy
	return -1
def inTarget(x, y):
	if x1 <= x <= x2 and y1 <= y <= y2:
		return True
	return False
def toZero(a):
	if a < 0:
		return a + 1
	if a > 0:
		return a - 1
	return 0

main()