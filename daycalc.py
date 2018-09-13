import sys
m=float(sys.argv[1])
d=float(sys.argv[2])
y=float(sys.argv[3])
y= y-int((14-m)/12)
print(y)
x= int(y+y/4-y/100+y/400)
print(x)
m=m+12*(int((14-m)/12))-2
print(m)
d=(d+x+(31*m)/12)%7
print(d)
if int(d) == 0:
	print("Sunday") 
elif int(d) == 1:
	print("Monday")     
elif int(d) == 2:
	print("Tuesday")
elif int(d) == 3:
	print("Wednesday")
elif int(d) == 4:
	print("Thursday")
elif int(d) == 5:
	print("Friday")
elif int(d) == 6:
	print("Saturday")
else:
	print("I don't understand")