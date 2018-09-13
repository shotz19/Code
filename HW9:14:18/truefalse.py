# Stephanie Hotz 9.13.18
import sys
x=sys.argv[1]
y=sys.argv[2]
z=sys.argv[3]
if x<y<z:
	print("True")
elif x>y>z:
	print("True")
else:
	print("False")