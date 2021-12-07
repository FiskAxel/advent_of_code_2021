def main():
	with open('input03.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		values = [i.strip() for i in input]
		gammaRate = ''
		for i in range(len(values[0])):
			gammaRate += commonDigit('most', values, i)
		epsilonRate = ''.join(['1' if i == '0' else '0' for i in gammaRate])
		powerConsumption = int(gammaRate, 2) * int(epsilonRate, 2)
		print(f"Part 1: {powerConsumption}")

		oxygenGeneratorRating = magicRatingCalculator('most', input)
		co2ScrubberRating = magicRatingCalculator('least', input)
		lifeSupportRating = oxygenGeneratorRating * co2ScrubberRating
		print(f"Part 2: {lifeSupportRating}") # too high 2886138

def commonDigit(mL, list, index):
	count = 0
	for i in list:
		if i[index] == '1':
			count += 1
	if count >= len(list) / 2:
		if mL == 'most': 
			return '1'
		else: 
			return '0'
	elif mL == 'most': 
			return '0' 
	return '1'
def magicRatingCalculator(mL, input):
	ratings = [i.strip() for i in input]
	rat     = [i.strip() for i in input]
	for i in range(len(ratings[0])):
		cD = commonDigit(mL, rat, i)
		for b in ratings:
			if b[i] != cD:
				rat.remove(b)
			if len(rat) == 1:
				break
		ratings = [i for i in rat]
		if len(ratings) == 1:
			break
	return int(ratings[0], 2)

main()