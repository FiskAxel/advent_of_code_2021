def main():
	with open('input16.txt', 'r') as puzzleInput:
		b = "".join(["{0:04b}".format(int(i, 16)) for i in puzzleInput.readline()])
	bigPack = unpack(b, [0])
	print(f"Part 1: {countVersionSum([bigPack])}")
	print(f"Part 2: {value(bigPack)}")

class package:
	def __init__(self, v, t):
		self.v = v
		self.t = t
		self.value = None
		self.subPackages = []
def unpack(b, index):
	i = index[0]
	v = int(b[i:i+3], 2)
	i += 3
	t = int(b[i:i+3], 2)
	i += 3
	packy = package(v, t)
	if t == 4:
		p = ''
		while True:
			p += b[i+1:i+5]
			if b[i] == '0':
				i += 5
				break
			i += 5
		index[0] = i
		packy.value = int(p, 2)
		return packy
	else:
		id = b[i]
		i += 1
		if id == '0':
			l = int(b[i:i+15], 2)
			i += 15
			index[0] = i
			while index[0] < i + l:
				packy.subPackages.append(unpack(b, index))
		else:
			l = int(b[i:i+11], 2)
			i += 11
			index[0] = i
			for _ in range(l):
				packy.subPackages.append(unpack(b, index))
	return packy
def countVersionSum(packages):
	sum = 0
	for p in packages:
		sum += p.v
		sum += countVersionSum(p.subPackages)
	return sum

def value(p):
	s = p.subPackages
	if p.t == 0: return sum(s)
	if p.t == 1: return product(s)
	if p.t == 2: return minimum(s)
	if p.t == 3: return maximum(s)
	if p.t == 4: return p.value
	if p.t == 5: return greaterThan(s)
	if p.t == 6: return lessThan(s)
	if p.t == 7: return equalTo(s)
def sum(p):
	sum = 0
	for i in p:
		sum += value(i)
	return sum
def product(p):
	sum = 1
	for i in p:
		sum *= value(i)
	return sum
def minimum(p):
	m = float("inf")
	for i in p:
		if value(i) < m:
			m = value(i)
	return m
def maximum(p):
	m = float("-inf")
	for i in p:
		if value(i) > m:
			m = value(i)
	return m
def greaterThan(p):
	if value(p[0]) > value(p[1]):
		return 1
	return 0
def lessThan(p):
	if value(p[0]) < value(p[1]):
		return 1
	return 0
def equalTo(p):
	if value(p[0]) == value(p[1]):
		return 1
	return 0

main()