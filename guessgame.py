import random
guessTaken=0
number=random.randint(1,10)
print("Guess a number between 1-10")
while guessTaken<5:
	print(guess)
	guess = input()
	guessesTaken = guessesTaken + 1
	if guess < number:
		print('Your guess is too low.') # There are eight spaces in front of print.
	elif guess > number:
		print('Your guess is too high.')
	elif guess == number:
		print("You guessed my number")
	elif guessTaken=5:
		print ("my number was"+number)
