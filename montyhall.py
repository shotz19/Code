#Stephanie Hotz 1.9.19
#It is better to switch because if you choose one with the pennies (2/3 of the time) you win if you switch while if you choose the one with the car (1/3) of the time you win if you do not switch. So, 2/3 of the time you win if you switch and 1/3 of the time you win if you don't; therefore, you should switch>
import random
import sys
#I am using 2 as the box with the car
def nochange():
	wins = 0
	for i in range (1000):
		box = random.randint(1,3)
		if box == 2:
			wins = wins + 1
	print(wins)
def change():
	wins = 0
	for i in range (1000):
		box = random.randint(1,3)
		if box == 1 or box == 3:
			wins = wins +1
	print(wins)
if sys.argv[1] == "change":
	change()
elif sys.argv[1] == "nochange":
	nochange()
# The program did what I expected change won 651-675 of the times and nochane won 322-350 of the times. This is because you win if you don't change and pick 2 or if you do change and pick 1 or 3.