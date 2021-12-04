def main():
	with open('input04.txt', 'r') as puzzleInput:
		nums = puzzleInput.readline().strip().split(',')
		input = puzzleInput.readlines()
		boards = []
		for i in range(0, len(input), 6):
			board = []
			for j in range(1, 6):
				board.append(input[i + j].split())
			boards.append(board)
		for i in range(5, len(nums)):
			n = nums[:i + 1]
			for b in boards:
				win = winner(b, n)
				if win:
					break
			if win:
				result = int(nums[i]) * sumOfUnmarked(win, n)
				break
		print(f"Part 1: {result}")

		for i in range(5, len(nums)):
			n = nums[:i + 1]
			remove = []
			for b in boards:
				win = winner(b, n)
				if win:
					remove.append(win)
			for b in remove:
				if len(boards) == 1:
					result = int(nums[i]) * sumOfUnmarked(win, n)
					print(f"Part 2: {result}")
					exit(0)
				boards.remove(b)

def winner(board, n):
	# Check rows
	for row in range(5):
		win = True
		for col in range(5):
			if board[row][col] not in n:
				win = False
				break
		if win:
			return board
		
	# Check colls
	for col in range(5):
		win = True
		for row in range(5):
			if board[row][col] not in n:
				win = False
				break
		if win:
			return board
def sumOfUnmarked(board, n):
	sum = 0
	for row in board:
		for col in row:
			if col not in n:
				sum += int(col)
	return sum

main()