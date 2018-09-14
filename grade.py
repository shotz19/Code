#Stephanie Hotz 9.14.18
import sys
grade=float(sys.argv[1])
keepgoing= True
while keepgoing== True:
	if 4.85<=grade<5:
		letter="A+"
		print(letter)
		keepgoing=False
	elif 4.7<=grade<4.85:
		letter="A"
		print(letter)
		keepgoing=False
	elif 4.5<=grade<4.7:
		letter="A-"
		print(letter)
		keepgoing=False
	elif 4.2<=grade<4.5:
		letter="B+"
		print(letter)
		keepgoing=False
	elif 3.85<=grade<4.2:
		letter="B"
		print(letter)
		keepgoing=False
	elif 3.5<=grade<3.85:
		letter="B-"
		print(letter)
		keepgoing=False
	elif 3.2<=grade<3.5:
		letter="C+"
		print(letter)
		keepgoing=False
	elif 2.85<=grade<3.2:
		letter="C"
		print(letter)
		keepgoing=False
	elif 2.5<=grade<2.85:
		letter="C-"
		print(letter)
		keepgoing=False
	elif 2<=grade<2.5:
		letter="D+"
		print(letter)
		keepgoing=False
	elif 1.5<=grade<2:
		letter="D"
		print(letter)
		keepgoing=False
	elif 0<=grade<1.5:
		letter="oof"
		print(letter)
		keepgoing=False
	else:
		grade=float(input("That is not a valid grade for this course. Please enter a number between 0 and 5"))
		


