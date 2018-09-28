import sys
while True:
	try:
		g=[]
		for x in range(1,11):
			g.append(int(sys.argv[x]))
		break
	except ValueError:
		print("Your entry was not valid. Please try again.")
		exit()
print(sorted(g))
g.sort(reverse=True)
print(g)
total=sum(g)
print(total)
