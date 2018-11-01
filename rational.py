class RationalNumber:
	def __init__(self, n, d):
		self.n = n
		self.d = d

	def __add__(self, other):
		n = self.n*other.d + self.d*other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def __sub__(self, other):
		n = self.n*other.d-self.d*other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def __mul__(self, other):
		n = self.n*other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def __truediv__(self, other):
		n = self.n*other.d
		d = self.d*other.n
		return RationalNumber(n, d)

	# complete this first!
	def __str__(self):
		return str(self.n)+"/"+str(self.d)

	__repr__ = __str__ # what does this do?

def main():
	a = RationalNumber(1, 2)
	b = RationalNumber(1, 3)
	print(str(a)) # 1/2
	print(str(b)) # 1/3
	print(a+b) # 5/6
	print(a-b) # 1/6
	print(a*b) # 1/6
	print(a/b) # 3/2
main()