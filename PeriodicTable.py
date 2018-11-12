#On my honor, I have neither given nor received unauthorized aid.

#This is the Periodic Table Class file (one of three for this project). This creates the Periodic Table to be used in the main part of the program.

#By Stephanie and Kaki

#PERIODIC TABLE

#SOURCES
#https://docs.python.org/3/howto/regex.html
#https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python

#IMPORTS

#This is the regular expressions module. It is used to find patterns in strings. This program uses it to take apart the compound that is given.
import re
#This imports the Element class from the file Element.py
from element import Element

#CLASS
#This is the class for the periodic table that holds funtions that relate multiple elements.
class PeriodicTable:

#FUNCTIONS

# Here, the file is opened and each line is split into different parts which are added to a dictionary.
	def __init__ (self, pfile):
		self.allelements = {}
		file = open('elements.csv')
		for line in file:
			part = line.split(',')

			#This eliminates the first first line of the file which is just text
			if part[0] == "Element":
				continue

			# In this, the object from Class Element is intialized and set into a dictionary with the chemical symbol as the key for each element.	
			oneelement = Element(part[0], part[1], part[2], part[3])
			self.allelements[part[2]] = oneelement	


# This funtion gives the atomic weight of a compund
	def calcWeight(self, compound) :

		# This checker will be used later to check if the compound calculated is the same as the one entered.
		checker = ''

		'''This matcher funtion goes through the coumpound entered and matches a capital [A-Z] and any following 
		letters [a-z] (the star says to find as many lowercase letters as possible) with the number [0-9](this star has the same function as the first for the numbers).'''
		matcher = re.compile('([A-Z][a-z]*)([0-9]*)')

		#This uses the matcher that was just set up to go through the compound given
		parts = re.findall(matcher, compound)
		totalWeight = 0

		# This uses a for loop to go through each part that was identified in the matcher
		for part in parts:

			#If part[1] (the number after the symbol) exists then that becomes the multiplier for the weight of the element. If not, the multiplier is 1
			if part[1]:	
				multiplier = float(part[1])
			else:
				multiplier = 1

			# This retrieves the element from the dictionary using the chemical symbol key that was given in the compound and labeled as part[1].
			element = self.allelements.get(part[0])

			# This is some error checking to account for things that look like element (Egg, Pn, etc.)
			if not element:
				return (part[0]+" is not a valid element in your compound. Please try again.")

			#The weight is set to the weight that was retrieved from the dictionary by using the getWeight() function from the Element Class.
			weightofElement = element.getWeight()

			#This is where the weight is multiplied by the number given and then added to the total
			totalWeight = float(totalWeight) + float(weightofElement) * float(multiplier)

			#The checker is built by adding the parts together
			checker += part[0] + part [1]

		#This checks if the compound that was calculated is the one entered
		if checker == compound:
			return totalWeight
		else:
			return("You entered an invalid compund. Please try again.")


	#This Function finds the element with the nearest weight to the one entered
	def nearestWeight(self, weight):

		#Initializing lowest as an impossibly high number, so the new number will definetly be lesser.
		lowest = float(1000)

		#Initializing the element
		lowestElement = ''

		#This goes through the dictionary of elements and labels them as symbol, element.
		for symbol, element in self.allelements.items():
			print(symbol,element)

			#The difference is taken between the number entered and the atomic weight of the element being tested and is compared to the current least difference.
			#If the difference is greater, it will move on to the next element, if it is lesser, the lesser number will become the new lowest.
			if abs(float(element.getWeight())-weight) < lowest:
				lowest = abs(float(element.getWeight())-weight)
				lowestElement = element

		#This returns the element that had the closest atomic weight to the one entered
		return lowestElement


	#This function displays information about an element given one of its attributes.
	def display (self,given) :

		#This goes through the dictionary of elements and labels them as symbol, element.
		for symbol, element in self.allelements.items():
			#This checks to see if the given is equal to any of the element's attributes.
			#If it is, it will return the element.
			if given in (element.getWeight(),element.getSymbol(),element.getNumber(),element.getElement()):
				return (element)
			elif symbol == 'Lr' and given not in (element.getWeight(),element.getSymbol(),element.getNumber(),element.getElement()):
				return (given+" is not a valid element attribute. Please try again.")


	#This Calculates the moles that are in a number of grams of a compund.
	def calcMoles(self, compound, grams) :	

		#The grams of the element are given by the user and divided by atomic weight found by the calcWeight function. 
		return float(grams)/self.calcWeight(compound)
  
	#This defines the string of all of the elements
	def __str__ (self) :
		info = ""
		for e in self.allelements :
			info = str (e)
		return info
  
	__repr__ = __str__


