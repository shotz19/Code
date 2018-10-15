from PIL import Image
imgx=512
imgy=512
image=Image.new("RGB",(imgx, imgy))
for x in range (imgx):
	red=255
	green=0
	blue=0
	count=0
	for y in range (imgy):
		image.putpixel((x,y),(red,green,blue))
		if count<127:
			green=green+2
		elif 127<count<190:
			red=red-2
		elif 190<count<317:
			blue=blue+2
		elif 317<count<444:
			green=green-2
		elif count>444:
			red=red+2
		count=count+1
image.save("colored_image.png","PNG")