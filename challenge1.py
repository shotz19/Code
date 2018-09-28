#https://www.programiz.com/python-programming/methods/list/sort
import random
g=[]
for x in range(15):
	g.append(random.randint(1,100))
new=int(input("Give me a number between 1 and 100 to add to the list"))
g.append(x)
g.sort(reverse=True)
print(g)