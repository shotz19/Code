import math
#https://docs.python.org/3/library/math.html
theta=input("give me an angle (in radians) and I will prove a pythagorean identity")
sine=math.sin(float(theta))
cosine=math.cos(float(theta))
print("Sine=",sine)
print("Cosine=",cosine)
sinesq=sine**2
cosinesq=cosine**2
print("Sine squared=",sinesq)
print("Cosine squared=",cosinesq)
print("=",int(sinesq+cosinesq))

