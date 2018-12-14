
class card():
	def __init__(self,suit,rank):
		self.suit=suit
		self.rank=rank
	def __str__(self):
		if self.rank == 11:
			self.rank = "Jack"
		elif self.rank == 12:
			self.rank = "Queen"	
		elif self.rank == 13:
			self.rank = "King"	
		elif self.rank == 1:
			self.rank = "Ace"	
		elif self.rank == 14:
			self.rank = "A"	
		if self.suit == 2:
			self.suit = "Hearts"
		if self.suit == 4:
			self.suit = "Diamonds"
		if self.suit == 3:
			self.suit = "Clubs"
		if self.suit == 1:
			self.suit = "Spades"
		return(str(self.rank)+" of "+str(self.suit))