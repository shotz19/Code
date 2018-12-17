#https://docs.python-guide.org/scenarios/imaging/
import sys
def filterpic(pic):
	from PIL import Image, ImageFilter
	originalimage = Image.open(pic)
	imgx, imgy  = originalimage.size
	#originalimage.show()
	image=Image.new("RGB",(imgx, imgy))
	count = 0
	for x in range (imgx):
		for y in range (imgy):
			RGB = originalimage.getpixel((x,y))
			r,g,b = RGB 
			count = 0
			if 10<x<imgx-10 and 10<y<imgy-10:
				r = int(r + 1.5*x)
				g = int(g + 1.5*abs(imgx/2-x))
				b = int(b + 1.5*abs(imgx-x))
			else:
				r = 0
				g = 0
				b = 0
			image.putpixel((x,y),(r,g,b))
	image.show()
filterpic(sys.argv[1])
filterpic(sys.argv[2])
filterpic(sys.argv[3])
filterpic(sys.argv[4])
filterpic(sys.argv[5])