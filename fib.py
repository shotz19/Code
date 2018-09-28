import sys
number=int(sys.argv[1])
answer=0
answer1=1
i=0
while i<number:
	print(answer1)
	newanswer=answer1+answer
	i=i+1
	answer=answer1
	answer1=newanswer

