#https://stackoverflow.com/questions/18412179/reading-a-file-and-storing-values-into-variables-in-python
file = open('elements.csv')
from element.py import Element
allelements=[]
for line in file:
	part = line.split(',')
	elements=[part[0],part[1],part[2],part[3]]
	allelements.append(elements)
print(allelements[1])
class elements:
	def __init__ (self,Element1,number1,Element2,number2,Elemnt3,number3,Element4,number4):
		self.Element1 = Element
	def __add__(self):
		total_weight = (self.Element1.weight*self.number1) + (self.Element2*self.number2) + (self.Element3*self.number3) + (self.Element4*self.number4)
		return total_weight
	def givemoles:
choice = input("Would you like molecule weight, moles, or display?")
if choice == "molecule weight":
	enteredmolecule = input("Please enter the molecule")
	molecule = enteredmolecule.split(" ")
elementdictionary = dict([
	(H)])



