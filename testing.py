import random
Sudoku = False
while Sudoku == False:
	board=[[random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9),  random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9)] for i in range(9)]
	correct = 0
	for i in range (9):
		if board[i][0] + board[i][2] + board[i][3] + board[i][4] + board[i][5] + board[i][6] + board[i][7] + board[i][8] == 45:
			correct = correct+1
	for i in range (9):
		if board[0][i] + board[2][i] + board[3][i] + board[4][i] + board[5][i] + board[6][i] + board[7][i] + board[8][i] == 45:
			correct = correct+1
	if correct == 18:
		Sudoku = True
		print(*board)