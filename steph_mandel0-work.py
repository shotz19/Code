#!/anaconda3/bin/python

from PIL import Image, ImageColor
from colorsys import rgb_to_hls, hls_to_rgb
import colorsys
import random
import sys
#.3871 .3892 .5784 .5812

def image1():
    x1 = -2
    x2 = 1
    y1 = -1.5
    y2 = 1.5
    stop = 100
    imgx = 1000
    imgy = 1000
    image = Image.new("RGB", (imgx, imgy))

    for y in range(imgy):
        zy=y*(y2-y1)/(imgy)+y1
        for x in range(imgx):
            zx=x*(x2-x1)/(imgx)+x1

            z=zx+zy*1j
            c=z
            for i in range(stop):
                if abs(z)>2.0:
                    break
                z=z*z+c

            ## default color in set is black
            r=0
            g=0
            b=120

            H=i/stop
            L= 50
            S= 0-0.5
            rgb=colorsys.hls_to_rgb(H, L, S)

            if (i < stop-1):
                r=rgb[0]
                g=rgb[1]
                b=rgb[2]

            image.putpixel((x, y),(int(r),int(g),int(b)))

    image.save("prettypic1.png", "PNG")

image1()

