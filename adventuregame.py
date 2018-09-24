#stephanie Hotz adventure text based game 9-24-18
# This is a text based adventure game where the user is asked to make decisions and play mini games.
import random
#each def is a different part of the game
#Here, the user goes to a town then continues on the journey.
def town():
	print("You go into a town and see an inn where you can stay the night.\nYou hang out there for the night and decide to continue your adventure in the morning.\n\n")
	killthedragon()
#The sphinx is a mini riddle game.
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
def dragon():
	print("You have found the dragon!\n\n To defeat it you must slay it with your sword")
	sword=input("Pick up the sword by typing: sword")
	if sword == "sword":
		print("Now you must slay the dragon.")
		slay=input("Type slay to slay the dragon")
		if slay == "slay":
			print("Yay! You slayed the dragon!")
			exit()
		else:
			print("You failed to slay the dragon, so you die a horrible death and leave the dragon to kill the townspeople")
			exit()
	else:
		print("Your sword skills are clearly struggling. \nYou accidently slice yourslef in half with your sword.")
		exit()
def game():
	riddle=input("The goblin looks up at you and gives you a piece of paper that says:\n\nThis thing all things devours\nBirds, beasts, trees, flowers;\nGnaws iron, bites steel\nGrinds hard stones to meal\nSlays king, ruins town\nAnd beats high mountain down.")
	if riddle == "time":
		print("The goblin shows you a secret passageway through the cave that leads you to the dragon's layer.")
		dragon()
	else:
		print("The goblin is angry with yiur stupid answer, so he chases you out of his cave.\nYou walk for several more miles until you come upon what seems to be the dragon's layer.")
		dragon()
def cave():
	cavei=input("You come upon a giant cave. Do you\n\n1)Go in\n\n2)Ignore it and contniue walking.\n\nChoose 1 or 2")
	if cavei=="1":
		print("You have chosen to go into the cave!\nYou walk into the cave and see a small goblin creature that asks you to play a game with it.\n It brings you deeper into the cave and gives you cards.")
		game()
	elif cavei =="2":
		("You continue on your path and will never get to learn what lies within the cave.")
	else:
		print("I do not understand. Please enter 1 or 2")
		cave()
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
	cave()
#This is the start of the journey
def killthedragon():
	print("You walk up to a giant, looming mountain")
	print("You are told that this is where the dragon lives.")
	sphinxi=input("Along the way you encounter a sphinx would you like to\n\n1) talk to it\n\n2)continue on")
	if sphinxi=="1":
		sphinx()
	elif sphinxi=="2":
		print("You have chosen to ignore the sphinx and continue on your path")
		impass()
	else:
		print("I don't know what "+sphinxi+"means. Please type 1 or 2")
		killthedragon()
	impass()
#this is the beginning of the game where the user can choose to go or hang out in a town
def start():
	print("\nYou are here to kill a dragon!\n\nThe dragon has been terrorizing this city for years.")
	one=input("\nYou find yourself at a fork in the road. \n\nWould you like to \n\n1) continue on \n\n2) go to a town where you can hang out")
	if one=="1": 
		print("You have chosen to kill the dragon")
		killthedragon()
	elif one=="2":
		town()
	else:
		print("I don't know what "+one+"means. Please type 1 or 2")
		start()
def sphinx():
	print("The sphinx is sitting on a rock and says to you\nI have a riddle for you.")
	riddle=input("Voiceless it cries\nWingless flutters\nToothless bites\nMouthless mutters.")
	if riddle == "wind" or riddle == "Wind" or riddle=="the wind":
		print("You have solved the sphinx's riddle!\nIt tells you a shortcut through the mountain, sp you don't have to climb a treacherous pass.")
		cave()
	elif riddle == "bug":
		print("The sphinx hates your answer, so it kills you.")
		exit()
	else:
		print("The sphinx does not like your answer!\nYou must continue on your original path. \nYou are lucky you survived an encounter with this dangerous creature! ")
		impass()
start()
