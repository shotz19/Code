import math
import sys
t= float(sys.argv[1])
p= float(sys.argv[2])
r= float(sys.argv[3])
print("I am calculating $"+str(p)+" compounded continuosly for "+str(t)+" years at a "+str(r)+" percent interest.")
money=p*math.e**(.01*r*t)
print("You would have $", money)
