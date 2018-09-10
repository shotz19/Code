#Name: Stephanie Hotz, Date: September 10, 2018, Description:Conversation program that asks and answers questions.
print("Hello, my name is conversation bot 3000")
name=input("What is your name? ")
print("It is nice to meet you, "+name+"!")
favcolor=input(" "+name+", What is your favorite color? ")
if favcolor == "yellow":
	print("that is mine too!")
elif favcolor == "orange":
	print("I hate that color.")
elif favcolor == "black":
	print("That's not a color!")
else :
	print("That's cool, mine is blue.")
favfood=input("what is your favorite food? ")
print(""+favfood+" is cool, but I just run on batteries!")
print("ask me a question")
print("(A) How are you")
print("(B) Do you like being a computer?")
print("(C) What's your favorite animal?")
print("(D) How do you stop an elephant from chraging?")
answer = 1
while answer == 1:
	question=input("Choose: A, B, C, or D")
	if question == "A":
		print("I am tired, but pretty good!")
		answer = 0
	elif question == "B":
		print("Yes! But my life gets boring... It's all 0s 1s!)")
		answer = 0
	elif question == "C":
		print("Sloths")
		answer = 0
	elif question == "D":
		print("You take away its credit card!")
		answer = 0
	else:
		print("I don't understand. Please answer again.")
print("It has been nice talking to you!")
print("Goodbye!")



