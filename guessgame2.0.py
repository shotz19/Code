import random
def limited():
	number= random.randint(1,100)
	guesses= int(input("How many guesses would you like?"))
	while guesses>0:
		guess=input("Guess my number")
		guess=float(guess)
		if guess==number:
			print("You guessed my number!")
			exit()
		elif guess<number:
			print("too low")
			print("you have "+str(guesses-1)+" guesses left")
			guesses=guesses-1
		elif guess>number:
			print("too high")
			print("you have "+str(guesses-1)+" guesses left")
			guesses=guesses-1
	print("you lose!")
	print("The number was", number)
def unlimited():
	guesses=True
	number= random.randint(1,100)
	while guesses==True:
		guess=input("Guess my number")
		guess=float(guess)
		if guess==number:
			print("You guessed my number!")
			exit()
		elif guess<number:
			print("too low")
		elif guess>number:
			print("too high")
def start():
	print("Welcome to the number guessing game!")
	whatgame=input("Would you like to play with limited or unlimited guesses")
	if whatgame=="limited":
		limited()
	elif whatgame=="unlimited":
		unlimited()
	else:
		start()
start()