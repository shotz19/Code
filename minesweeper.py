#Stephanie Hotz Minesweeper 10.1.18
import sys
import random
#WHB
#Initializing board size
W=int(sys.argv[1])
H=int(sys.argv[2])
B=int(sys.argv[3])
score=0
#function to print board
def printboard():
	#deleting extra columns
	for x in range(H):
		del board[x][W]
		del board[x][W]
	for x in range(H):
		del board1[x][W]
		del board1[x][W]
	for x in range(len(board1)-2):
		print(*board1[x])
	#replacing extra columns
	for x in range (H):
		board[x].append(0)
		board[x].append(0)
	for x in range (H):
		board1[x].append(0)
		board1[x].append(0)
#function for radiatin which prints around a space
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
#some error catching if the user gives more bombs than space on the board
if B>W*H:
	print("NO!")
	exit()
#Initializing the board with answers
board=[[0]*(W+2) for i in range(H+2)]
#Initializing the playing board
board1=[["o"]*(W+2) for i in range(H+2)]
#placing the bombs
bombs=0
while bombs<B:
	#choosing random places for bombs
	bomby=random.randint(0,H-1)
	bombx=random.randint(0,W-1)
	if board[bomby][bombx]!="*":
		board[bomby][bombx]="*"
		bombs=bombs+1
#making sure the bombs do not overlap
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
#gameplay
while True:
	#choosing between placing flag and guessing spots
	flag=input("Would you like to\n\n1) Guess a space\n\nor\n\n2)Place a flag")
	if flag=="1":
		#choosing the space
		row=int(input("What space would you like to open?\nPlease enter the row"))-1
		column=int(input("Now, enter the comlumn"))-1
		#this makes the chosen spot show
		board1[row][column]=board[row][column]
		#ends the game if the user chose a bomb
		if board[row][column]=='*':
			printboard()
			print("You lose")
			exit()
		#radiates(opens surrounding spaces)
		elif board[row][column]==0:
			score=score+1
			printaround(row,column,score)
			#This checks each space to see if it is open and zero
			for x in range(H):
				for y in range(W):
					if board[x][y]==0 and board1[x][y]==board[x][y]:
						printaround(x,y,score)
			printboard()	
		else:
			#this is what happens normally
			score=score+1
			printboard()
		#you win sequence
		if score==(W*H)-B:
			print("You win!")
			exit()
	#if the user chooses to place a flag
	elif flag=="2":
		row=int(input("Where would you like to place a flag?\nPlease enter the row"))-1
		column=int(input("Now, enter the comlumn"))-1
		board1[row][column]="*"
		for x in range(len(board1)-2):
			print(*board1[x])
	#more error checking
	else:
		print("I do not understand.")


	

   