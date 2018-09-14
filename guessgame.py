import random
number= random.randint(1,100)
guesses=5
while guesses>0:
	guess=input("Guess my number")
	guess=float(guess)
	if guess==number:
		guessed=True
		print("You guessed my number!")
		exit()
	elif guess<number:
		print("too low")
		print("you have "+str(guesses)+" guesses left")
		guesses=guesses-1
	elif guess>number:
		print("too high")
		print("you have "+str(guesses)+" guesses left")
		guesses=guesses-1
print("you lose!")
