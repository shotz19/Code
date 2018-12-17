from PIL import Image
imgx=512
imgy=512
image=Image.new("RGB",(imgx, imgy))
for x in range imgx
	for x in range imgy
image.putpixel((0,0),(0,110,130))
image.save("demo_image.png","PNG")