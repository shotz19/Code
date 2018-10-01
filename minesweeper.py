#Stephanie Hotz Minesweeper 10.1.18
import sys
import random
#WHB
W=int(sys.argv[1])
H=int(sys.argv[2])
B=int(sys.argv[3])
board=[[0]*(W+2) for i in range(H+2)]
bombs=0
while bombs<B:
	bomby=random.randint(0,H-1)
	bombx=random.randint(0,W-1)
	board[bomby][bombx]="*"
	bombs=bombs+1
for x in range(W):
	count=0
	for y in range(H):
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
for x in range(len(board)-2):
	print(*board[x])

	

   