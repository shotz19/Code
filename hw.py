import sys
number=int(sys.argv[1])
ex=int(sys.argv[2])
l=[]
exp=ex
for x in range(ex):
	l.append(number**exp)
	exp=exp-1
l.reverse()
print(l)