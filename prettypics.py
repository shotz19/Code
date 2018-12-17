#On my honor, I have neither given nor received unauthorized aid.
#http://hslpicker.com/#9500ff
#https://docs.python.org/2/library/colorsys.html
#http://www.karlsims.com/julia.html
#Stephanie Hotz: Madelbrot sets. The first two are mandelbrot sets. One, is more simple using rgn colormode and mods. The other uses hls and uses logs to smooth out the color.
#The last is a julia set. Here, I used an if statement to color different parts if the set.
from PIL import Image, ImageColor
from colorsys import rgb_to_hls, hls_to_rgb
import colorsys
import sys
import math
#Mandelbrot
def image1():
	#setting up the part of the set
	x1 = .38555
	x2 = .40555
	y1 = .12055
	y2 = .13565
	#set the max
	stop = 300
	#set the size of the image
	imgx = 1000
	imgy = 1000
	image = Image.new("RGB", (imgx, imgy))
	for y in range(imgy):
		for x in range(imgx):
			#equations from the set
			zx=x*(x2-x1)/(imgx)+x1
			zy=y*(y2-y1)/(imgy)+y1
			z=zx+zy*1j
			c=z
			for i in range(stop):
				if abs(z)>2.0:
					break
				z=z*z+c
			#the middle is a blue made with rgb
			r=0
			g=70
			b=255
			#the log smooths out the set
			H=100*math.log(i*5,4)/stop
			L= 255
			S= -1
			#the color is given in HLS, but colorsys is used to translate it to rgb.
			rgb=colorsys.hls_to_rgb(H, L, S)
			if (i < stop-1):
				r=rgb[0]
				g=rgb[1]
				b=rgb[2]
			image.putpixel((x, y),(int(abs(r)),int(abs(g)),int(abs(b))))

	image.save("prettypic11.png", "PNG")
#Mandelbrot
def image2():
	#setting up the part of the set
	x1 = .3871
	x2 = .3892
	y1 = .5784
	y2 = .5812
	#set the max
	stop = 255
	#set the size of the image
	imgx = 1000
	imgy = 1000
	image = Image.new("RGB", (imgx, imgy))
	for y in range(imgy):
		for x in range(imgx):
			#equations from the set
			zx=x*(x2-x1)/(imgx)+x1
			zy=y*(y2-y1)/(imgy)+y1
			z=zx+zy*1j
			c=z
			for i in range(stop):
				if abs(z)>2.0:
					break
				z=z*z+c
			#modding to make the colors more interesting
			r=i
			g=i
			b=(i*280)%130
			image.putpixel((x, y), (r,g,b))

	image.save("prettypic2.png", "PNG")
#Juliaset
def image3():
	#setting up the part of the set
	x1=-1
	x2=1
	y1=-1
	y2=1
	#set the size of the image
	imgx=1000
	imgy=1000
	#set the max
	stop=60
	#sets up the julia set
	julia=0.1+0.615j
	image = Image.new("RGB", (imgx, imgy))
	for y in range(imgy):
		#similar to the mandelbrot equations
		zy=y*(y2-y1)/(imgy)+y1
		for x in range(imgx):
			zx=x*(x2-x1)/(imgx)+x1
			z=zx+zy*1j
			if julia == 0:
				c = z
			else:
				c = julia
			for i in range(stop):
				if abs(z)>2.0:
					break
				z=z*z+c
			#colors the inside
			r = 0
			g = 30*int(math.log(i*3,(10)))
			b = i*2
			#colors outside
			if (i < stop-1):
				r = int(0 + (255-0) * i/stop)
				g = int(0 + (100-0) * i/stop)
			image.putpixel((x, y), (r,g,b))
	image.save("prettypic3.png", "PNG")
image1()
image2()
image3()






