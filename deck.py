'''import cards
Deck
(colors)
list of cards/empty list
draw a card/dealing
shuffle
play a card'''
from card import card
class deck:
	def __init__(self,cards,color):
		self.cards = cards
		self.color = color
	def create(self):
		for i in range (1,5):
			for j in range(1,15):
				self.cards.append[card(i,j)]
	def print(self):
		print(self.cards)
deck = deck(0,0)
deck.create()
deck.print()



