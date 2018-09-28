#https://www.programiz.com/python-programming/methods/list/sort
#Create  a  list  of  15  random  numbers  from  0-100.  Ask  the  user  for  one  input  from  0-100.  Append  this  input  to  the  list.  Sort  the  list  into  descending  order. 
import random
g=[]
for x in range(15):
	g.append(random.randint(1,100))
new=int(input("Give me a number between 1 and 100 to add to the list"))
g.append(x)
g.sort(reverse=True)
print(g)