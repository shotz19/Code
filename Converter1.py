print("A. Dollars to Yen")
print("B. Dollars to Euros")
print("C. Dollars to Colóns")
userinput=1
while userinput==1:
	answer= input("Choose A,B, or C")
	if answer== ("A"):
		print("Dollars to Yen calculator")
		dollars= input("Dollars:")
		yen= float(dollars)*111.47
		print("Yen:",yen)
		userinput= 0
	elif answer== ("B"):
		print("Dollars to Euros calculator")
		dollars= input("Dollars:")
		Euro= float(dollars)*.86
		print("Euro:",Euro)
		userinput= 0
	elif answer== ("C"):
		print("Dollars to Colóns calculator")
		dollars= input("Dollars:")
		Colóns= float(dollars)*580.69
		print("Colóns:",Colóns)
		userinput= 0
	else:
		print("I do not understand")
