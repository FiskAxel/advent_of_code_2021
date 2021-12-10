def main():
	with open('input08.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		#print(f"Part 1: {sum([sum([1 if len(i) <= 4 or len(i) == 7 else 0 for i in o.split()]) for o in [i.split(' | ')[1].strip() for i in input]])}")
		signals = [i.split(' | ')[0] for i in input]
		outputs = [i.split(' | ')[1].strip() for i in input]
		result = 0
		for o in outputs:
			o = o.split()
			for j in o:
				if len(j) <= 4 or len(j) == 7:
					result += 1
		print(f"Part 1: {result}")

		result = 0
		for s, o in zip(signals, outputs):
			s = [''.join(sorted(i)) for i in s.split()]
			o = [''.join(sorted(i)) for i in o.split()]
			number = {} # Storing int:string, for 0-9 
			one478(s, number)
			nine(s, number)
			zeroSix(s, number)
			five(s, number)
			twoThree(s, number)
			number = {b : a for a, b in number.items()} # string:int
			result += int(''.join([str(number[i]) for i in o]))
		print(f"Part 2: {result}")

def one478(signal, n):
	for i in signal:
		if len(i) == 2:
			n[1] = i
		elif len(i) == 4:
			n[4] = i
		elif len(i) == 3:
			n[7] = i
		elif len(i) == 7:
			n[8] = i
def nine(signal, n):
	for i in signal:
		if len(i) == 6 and dif(n[4], i) == 0 and dif(n[7], i) == 0:
			n[9] = i
def zeroSix(signal, n):
	for i in signal:
		if len(i) == 6 and n[9] != i:
			if dif(n[1], i) == 0:
				n[0] = i
			else:
				n[6] = i
def five(signal, n):
	for i in signal:
		if len(i) == 5 and dif(n[6], i) == 1:
			n[5] = i
def twoThree(signal, n):
	for i in signal:
		if len(i) == 5:
			if dif(n[5], i) == 2:
				n[2] = i
			elif dif(n[5], i) == 1: 
				n[3] = i
def dif(n1 , n2):
	"Returns how many parts of n1 is not in n2"
	dif = 0
	for c in n1:
		if c not in n2:
			dif += 1
	return dif

main()