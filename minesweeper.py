#Stephanie Hotz Minesweeper 10.1.18
import sys
import random
#WHB
W=int(sys.argv[1])
H=int(sys.argv[2])
B=int(sys.argv[3])
score=0
if B>W*H:
	print("NO!")
	exit()
board=[[0]*(W+2) for i in range(H+2)]
board1=[["o"]*(W+2) for i in range(H+2)]
bombs=0
while bombs<B:
	bomby=random.randint(0,H-1)
	bombx=random.randint(0,W-1)
	if board[bomby][bombx]!="*":
		board[bomby][bombx]="*"
		bombs=bombs+1
for x in range(H):
	count=0
	for y in range(W):
		if board[x][y]!="*":
			count=0
			if board[x+1][y]=="*":
				count= count+1 
			if board[x-1][y]=="*":
				count= count+1
			if board[x][y-1]=="*":
				count=count+1
			if board[x][y+1]=="*":
				count=count+1
			if board[x+1][y+1]=="*":
				count=count+1
			if board[x+1][y-1]=="*":
				count=count+1
			if board[x-1][y+1]=="*":
				count=count+1
			if board[x-1][y-1]=="*":
				count=count+1
			board[x][y]=count
for x in range(H):
	del board[x][W]
	del board[x][W]
for x in range(H):
	del board1[x][W]
	del board1[x][W]
'''for x in range(len(board)-2):
	print(*board[x])'''
for x in range(len(board1)-2):
	print(*board1[x])
while True:
	row=int(input("What space would you like to open?\nPlease enter the row"))-1
	column=int(input("Now, enter the comlumn"))-1
	board1[row][column]=board[row][column]
	for x in range(len(board1)-2):
		print(*board1[x])
	if board[row][column]=='*':
		print("You lose")
		exit()
	else:
		score=score+1
	if score==(W*H)-B:
		print("You win!")
		exit()


	

   