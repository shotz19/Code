#https://www.geeksforgeeks.org/abs-in-python/
#https://stackoverflow.com/questions/24812444/why-are-complex-numbers-in-python-denoted-with-j-instead-of-i
from PIL import Image
x1 = -2.0
x2 = 2.0
y1 = -2.0
y2 = 2.0
stop = 255
imgx = 512
imgy = 512
image = Image.new("RGB", (imgx, imgy))
for y in range(imgy):
    zy = y * (y2 - y1) / (imgy)  + y1
    for x in range(imgx):
        zx = x * (x2 - x1) / (imgx)  + x1
        z = zx + zy * 1j
        c = z
        for i in range(stop):
            if abs(z) > 2.0: break 
            z = z * z + c
        image.putpixel((x, y), (int(i/2), 0, i))

image.save("mandel.png", "PNG")
