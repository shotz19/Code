'''import sys
number=int(sys.argv[1])
def factorial(n):
	if n==0:
		return 1
	return n*factorial(n-1)
#answer=factorial(number)

letters="dhuascilx"
def count(x):
	answer=0
	if x[len(x)-1]=="x":
		del x[len(x)-1]
		return count(x-1)
answer=count(letters)
print(letters)

numbers=9037568
def count(x):
	if x[x]
	return count(x+1)
answer=count(numbers)
print(answer)'''
	
def ce(n):
	if n is 0:
		return 0
	if n%10 ==8:
		if n%100==88:
			return 2+ce(n//10)
		else: 
			return 1+ce(n//10)
	return ce(n //10)




