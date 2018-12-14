from PIL import Image
imgx=int(512)
imgy=int(512)
image=Image.new("RGB",(imgx, imgy))
number=0
for count in range (8):
	for x in range (64*count,64*(count+1)):
		if count%2==1:
			for number in range(8):
				for y in range (64*number,64*(number+1)):
					if number%2==1:
						image.putpixel((x,y),(0,0,255))
					else:
						image.putpixel((x,y),(255,0,0))
		else:
			for number in range(8):
				for y in range (64*number,64*(number+1)):
					if number%2==1:
						image.putpixel((x,y),(255,0,0))
					else:
						image.putpixel((x,y),(0,0,255))
				
image.save("checker","PNG")