#Generate  a  list  of  10  random  numbers  between  0  and  100.  Get  them  inorder  from  largest  to  smallest,  removing  numbers  divisible  by  3. 
import random
g=[]
for x in range(10):
	a=random.randint(1,100)
	e=True
	while e==True:
		if a%3==0:
			a=random.randint(1,100)
		else:
			e=False	
	g.append(a)
print(g)