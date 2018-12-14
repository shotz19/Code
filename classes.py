class Hamster:
	# constructor
	#scales are out of 10
	def __init__(self, name,hunger,energy,happiness):
		self.hunger=hunger
		self.energy=energy
		self.happiness=happiness
		self.name=name
	def play(self):
		if self.hunger>0 and self.energy>0:
			self.happiness+=1
			#dog is hungry is hungry if hunger is at 0
			self.hunger-=1
			self.energy-=1
			status=self.name+" ran on the wheel."
			return status
		else:
			status="Your hamster can not play right now. You should give it food of let it sleep."
	def eat(self):
		if self.hunger<10 and self.energy>0:
			self.hunger+=1
			self.energy-=1
			self.happiness+=1
			status=self.name+" ate some strawberries. It is much happier now."
			return status
		else:
			status=self.name+" can not eat right now."
			return status
	def sleep(self):
		if self.hunger>0 and self.energy<10:
			self.hunger-=1
			self.energy+=1
			self.happiness-=1
			status=self.name+" ate some strawberries. It is much happier now."
			return status
		else:
			status=self.name+" is too hungry to sleep."
			return status
	def stats(self):
		info="Name: "+self.name
		info+="\nEnergy: "+str(self.energy)
		info+="\nHapiness: "+str(self.happiness)
		info+="\nHunger: "+str(self.hunger)
		return info

hamster1=Hamster("Buddy",5,5,5)

while True:
	print(hamster1.stats())
	choice = input("What would you like to do with your hamster?")
	if choice== "play":
		print("\n"+hamster1.play())
	elif choice=="sleep":
		print("\n"+hamster1.sleep())
	elif choice=="eat":
		print("\n"+hamster1.eat())
	elif choice=="end":
		exit()
	else:
		print("You can't do that.")

