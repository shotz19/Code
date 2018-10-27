class Account:
	def __init__(self,name,balance,pin,amount):
		self.name=name
		self.balance=balance
		self.pin=pin
		self.amount=amount
	def withdraw(self):
		if self.amount<self.balance:
			self.balance=self.balance-amount
			status="You now have"+str(self.balance)
		else:
			status="You can not do that!"	
		return status
	def deposit(self):
		self.balance=self.balance+amount
		status="You now have"+str(self.balance)
	def stats(self):
		info="Name: "+self.name
		info+="\nBalance "+str(self.balance)
		return info
account1=Account("Steph",300, 9999,0)
while True:
	print(account1.stats())
	choice = input("What would you like to do?\n")
	if choice== "withdraw":
		pinnum=int(input("\nWhat is you pin number?\n"))
		if pinnum== int(account1.pin):
			amount=int(input("\nHow much?"))
			account1.amount=amount
			print("\n"+account1.withdraw())
		else:
			print("\nThat is not your pin number. You may not make a transaction.")
	elif choice=="deposit":
		pinnum=int(input("\nWhat is you pin number?\n"))
		if pinnum== int(account1.pin):
			amount=int(input("How much?"))
			account1.amount=amount
			print("\n"+account1.deposit())
		else:
			print("\nThat is not your pin number. You may not make a transaction.")
	elif choice=="end":
		exit()
	else:
		print("You can't do that.")