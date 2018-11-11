#PERIODIC TABLE
import re
from element import Element

class PeriodicTable:

	def __init__ (self, pfile):
		self.allelements = {}
		file = open('elements.csv')
		for line in file:
			part = line.split(',')
			oneelement = Element(part[0], part[1], part[2], part[3])
			self.allelements[part[2]] = oneelement	


	def calcWeight(self, compound):
		matcher = re.compile('([A-Z][a-z]*)([0-9]*)')
		parts = re.findall(matcher, compound)
		totalWeight = 0

		for part in parts: 

			if part[1]:	
				multiplier = float(part[1])

			else:
				multiplier = 1

			element = self.allelements.get(part[0])
			#adderrorcheckinghere
			weightofElement = element.getWeight()
			totalWeight = float(totalWeight) + float(weightofElement) * float(multiplier)
		return totalWeight
	def display (self,given) :

	def calcMoles(self, compound, grams) :
		
		return float(grams)/self.calcWeight(compound)
  
	def __str__ (self) :
		info = ""
		for e in self.allelements :
			info = str (e)
		return info
  
	__repr__ = __str__

