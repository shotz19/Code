import sys
number=int(sys.argv[1])
def moves(n,  left):
	if n ==0:
		return
	moves(n-1,not  left)
	if  left:    
		print(str(n)+'  left')
	else:    
		print(str(n)+'  right')
	moves(n-1,not  left)
moves(number,True)
