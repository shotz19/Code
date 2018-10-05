#Stephanie Hotz Minesweeper 10.1.18
import sys
import random
#WHB
W=int(sys.argv[1])
H=int(sys.argv[2])
B=int(sys.argv[3])
score=0
def printboard():
	for x in range(H):
		del board[x][W]
		del board[x][W]
	for x in range(H):
		del board1[x][W]
		del board1[x][W]
	for x in range(len(board1)-2):
		print(*board1[x])
	for x in range (H):
		board[x].append(0)
		board[x].append(0)
	for x in range (H):
		board1[x].append(0)
		board1[x].append(0)
def printaround(therow,thecolumn,score):
	score=score
	board1[therow+1][thecolumn]= board[therow+1][thecolumn]
	score=score+1
	board1[therow-1][thecolumn]= board[therow-1][thecolumn]
	score=score+1
	board1[therow][thecolumn+1]= board[therow][thecolumn+1]
	score=score+1
	board1[therow][thecolumn-1]= board[therow][thecolumn-1]
	score=score+1
	board1[therow+1][thecolumn+1]= board[therow+1][thecolumn+1]
	score=score+1
	board1[therow+1][thecolumn-1]= board[therow+1][thecolumn-1]
	score=score+1
	board1[therow-1][thecolumn+1]= board[therow-1][thecolumn+1]
	score=score+1
	board1[therow-1][thecolumn-1]= board[therow-1][thecolumn-1]
	score=score+1
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
printboard()
score=0
while True:
	flag=input("Would you like to\n\n1) Guess a space\n\nor\n\n2)Place a flag")
	if flag=="1":
		row=int(input("What space would you like to open?\nPlease enter the row"))-1
		column=int(input("Now, enter the comlumn"))-1
		board1[row][column]=board[row][column]
		if board[row][column]=='*':
			printboard()
			print("You lose")
			exit()
		elif board[row][column]==0:
			score=score+1
			printaround(row,column,score)
			for x in range(H):
				for y in range(W):
					if board[x][y]==0 and board1[x][y]==board[x][y]:
						printaround(x,y,score)
			printboard()	
		else:
			score=score+1
			printboard()
		if score==(W*H)-B:
			print("You win!")
			exit()
	elif flag=="2":
		row=int(input("Where would you like to place a flag?\nPlease enter the row"))-1
		column=int(input("Now, enter the comlumn"))-1
		board1[row][column]="*"
		for x in range(len(board1)-2):
			print(*board1[x])
	else:
		print("I do not understand.")


	

   