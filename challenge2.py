#Allow  10  random  integers  to  be  entered  as  arguments.  Catch  any  potential  errors.  Print  them  sorted  from  small  to  large,  then  large  to  small,  and  then  print  the  sum
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
