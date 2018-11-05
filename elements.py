#https://stackoverflow.com/questions/18412179/reading-a-file-and-storing-values-into-variables-in-python
file = open('elements.csv')
'''for line in file:
	element= file.readline()
	part = line.split(',')
	print (part[0],part[1])'''
board=[]
for i in range (0,103):
	for line in file:
		element = file.readline()
		part = line.split(',')
		elements=[part[0],part[1],part[2],part[3],part[4]]
		board.append(elements)
print(board[0][0])
class elements:
	def __init__ (self,Element,Number,Symbol,Weight,Boil):
		self.Element = Element
		self.Number = Number
		self.Symbol = Symbol
		self.Weight = Weight
		self.Boil = Boil
	def add(self):
		addition= self.Weight + self.weight

