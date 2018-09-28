'''#empty list
a=[]
#adds to the end
a.append(4)
a.append(5)
a.append(3)
#adds the the beginning
a=[1]+a
#removes the number
a.remove(3)
#(position,argument)
a.insert(2,6)
#removes the position
del a[0]
print(a)
#prints then removes the last in the list
print(a.pop())
print(a)
#returns last thing in list
print(a[len(a)-1])
print(a[-1])
print(a)
#does it remove all 3s?
b=[1,2,3,6,3]
b.remove(3)
print("B=",b)
#c=5,d=7
c,d=5,7
#or
temp=c
c=d
d=temp
#more swaps
e=[1,2,3,7,5,6,4]
e[3],e[6]=e[6],e[3]
print(e)
#creating lists
f=[]
for x in range(7,707,7):
	f.append(x)
print(f)
print(len(f))
#list of 10 random numbers'''
import random
g=[]
for x in range(10):
	g.append(random.randint(1,100))#r.randrange(100) works too
print(g)
#sort the list
g.sort()#print(sorted(g)) to just print the sorted version
print(g)







