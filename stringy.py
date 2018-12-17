from PIL import Image
import random
imgx=int(512)
imgy=int(512)
image=Image.new("RGB",(imgx, imgy))
for count in range(100):
	x=random.randint(10,509)
	R=random.randint(0,254)
	G=random.randint(0,254)
	B=random.randint(0,254)
	for y in range (3,509):
		if 3<x<509:
			x=x+random.randint(-2,2)
		elif x<=3:
			x=x+5
		elif x>=509:
			x=x-5
		image.putpixel((x,y),(R,G,B))
	image.save("strings","PNG")