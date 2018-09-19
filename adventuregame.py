import random
def impass():
	print("You continue walking up the mountain and you come upon a steep impass.\nYou must climb this impass to contiue.\nTo go through, you must play a game and win.")
	print("When I show you a letter, match it on your keyboard to climb the mounatin")
	letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t,','u','v','w','x','y','z']
	playing=0
	while playing<5:
		r=random.randint(0,25)
		given=input(letters[r])
		if given==str(letters[r]):
			playing=playing+1
		else:
			print("You missed ther letter! You failed to grab the next handhold and you fall to your death :(")
			exit()
	print("Yay! You climbed the impass")
def killthedragon():
	print("You have chosen to kill the dragon")
	print("You walk up to a giant, looming mountain")
	print("You are told that this is where the dragon lives.")
	sphinx=input("Along the way you encounter a sphinx would you like to\n\n1) talk to it\n\n2)continue on")
	if sphinx=="1":
		sphinx()
	elif sphinx=="2":
		print("You have chosen to ignore the sphinx and continue on your path")
		impass()
	else:
		print("I don't know what "+sphinx+"means. Please type 1 or 2")
		killthedragon()
	impass()
def start():
	print("\nYou are here to kill a dragon!\n\nThe dragon has been terrorizing this city for years.")
	one=input("\nYou find yourself at a fork in the road. \n\nWould you like to \n\n1) continue on \n\n2) go to a town where you can hang out")
	if one=="1": 
		killthedragon()
	elif one=="2":
		town()
	else:
		print("I don't know what "+one+"means. Please type 1 or 2")
		start()
start()
def town():
	print("You go into a town...")
def sphinx():
	print("The sphinx is sitting on a rock and says to you\nI have a riddle for you.")
	riddle=input("Voiceless it cries\nWingless flutters\nToothless bites\nMouthless mutters.")
	if riddle == "wind" or riddle == "Wind" or riddle=="the wind":
		print("You have solved the sphinx's riddle!\nIt tells you a shortcut through the mountain, sp you don't have to climb a treacherous pass.")
	elif riddle == "bug":
		print("The sphinx hates your answer, so it kills you.")
		exit()
	else:
		print("The sphinx does not like your answer!\nYou must continue on your original path. \nYou are lucky you survived an encounter with this dangerous creature! ")

