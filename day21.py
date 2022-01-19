ONE = 3
TWO = 5
class player:
	def __init__(self, pos, score):
		self.pos = pos - 1 # 0-index
		self.score = score
def part1():
	p1, p2 = player(ONE, 0), player(TWO, 0)
	dice = 0
	rolls = 0
	while p1.score < 1000 and p2.score < 1000:
		if rolls % 2 == 0:
			roll(p1, dice)
		else: 
			roll(p2, dice)
		dice = (dice + 3) % 100
		rolls += 3
	if p1.score > p2.score:	result = rolls * p2.score
	else: result = rolls * p1.score
	print(f"Part 1: {result}")
def roll(p, dice):
	move = dice + (dice + 1) % 100 + (dice + 2) % 100 + 3
	p.pos = (p.pos + move) % 10
	p.score += p.pos + 1

def part2():
	rolls = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}
	wins = [0, 0]
	tree(rolls, 0, ONE - 1, 0, TWO - 1, True, 1, wins)
	print("Part 2: ", end='')
	if wins[0] > wins[1]: print(wins[0])
	else: print(wins[1])
def tree(r, p1, pos1, p2, pos2, p1turn, count, wins):
	if p1 >= 21:
		wins[0] += count
		return
	if p2 >= 21:
		wins[1] += count
		return

	if p1turn:
		for i in r:
			nP = (pos1 + i) % 10
			tree(r, p1 + nP + 1, nP, p2, pos2, False, count * r[i], wins)
	else:
		for i in r:
			nP = (pos2 + i) % 10
			tree(r, p1, pos1, p2 + nP + 1, nP, True, count * r[i], wins)

part1()
part2() # Runs in about 3 minutes :/