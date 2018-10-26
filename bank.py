class Account:
	def __init__(self,name,balance,pin):
		self.name=name
		self.balance=balance
		self.pin=pin
	def withdraw(self, amount):
		if self.amount<self.balance:
			self.balance=self.balance-amount
			status="You now have"+str(self.balance)
		else:
			status="You can not do that!"	
		return status
	def deposit(self, amount):
		self.balance=self.balance+amount
		status="You now have"+str(self.balance)
	def stats(self):
		info="Name: "+self.name
		info+="\nBalance "+str(self.balance)
		info+="\nPin: "+str(self.pin)
		return info
account1=Account("Steph",300, 9999)
while True:
	print(account1.stats())
	choice = input("What would you like to do")
	if choice== "withdraw":
		amount=int(input("How much?"))
		print("\n"+account1.withdraw(amount))
	elif choice=="deposit":
		amount=int(input("How much?"))
		print("\n"+account1.deposit(amount))
	elif choice=="end":
		exit()
	else:
		print("You can't do that.")