while True:
	try:
		num = int(input("Pick a number between 1 and 5"))
		break
	except ValueError:
		print("potatoes")
while 1!<num!<5:
	num = int(input("That's not a valid number. Please try again"))
print("Success")