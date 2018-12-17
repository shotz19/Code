#!/anaconda3/bin/python

from PIL import Image, ImageColor
from colorsys import rgb_to_hls, hls_to_rgb
import colorsys
import random
import sys
#.3871 .3892 .5784 .5812

# image function draws mandelbrot set with parameters
# MinX, MaxX, MinY, MaxY - min and max of X,Y to plot
# Iwide, Ihigh - pixel width and height of plot area
# julia - complex number for Julia set, or 0 to plot Mandelbrot
# colortype - to try different color systems
# c0a,c0b,c0c - parameters for color of fractal points
# c1a,c1b,c1c - starting color for non-set points 1 iteration discovery
# c2a,c2b,c2c - target color with more iterations to find
# savefile - name of output file
def image(MinX,MaxX,MinY,MaxY,Iwide,Ihigh,MaxIter,julia,colortype,c0a,c0b,c0c,c1a,c1b,c1c,c2a,c2b,c2c,savefile):
    image = Image.new(colortype, (Iwide, Ihigh))
    for y in range(Ihigh):
        zy=y*(MaxY-MinY)/(Ihigh)+MinY
        for x in range(Iwide):
            zx=x*(MaxX-MinX)/(Iwide)+MinX
            z=zx+zy*1j
            if julia == 0:
                c = z
            else:
                c = julia
            for i in range(MaxIter):
                if abs(z)>2.0:
                    break
                z=z*z+c
            ca = c0a
            cb = c0b
            cc = c0c
            if (i < MaxIter-1):
                ca = int(c1a + (c2a-c1a) * i/MaxIter)
                cb = int(c1b + (c2b-c1b) * i/MaxIter)
                cc = int(c1c + (c2c-c1c) * i/MaxIter)

            image.putpixel((x, y), (ca,cb,cc))
    image.save(savefile, "PNG")
    print("Saved "+savefile)

## basic mandelbrot
image(-2,1,-1.5,1.5,1000,1000,60,0,"RGB",0,0,0,255,255,255,255,0,0,"image01.png")

## change plot area
image(-2,0,0,1.5,1000,1000,60,0,"RGB",0,0,0,255,0,255,255,255,0,"image02.png")

## change plot area
image(-2,0,0,1,1000,1000,60,0,"RGB",0,0,0,255,0,255,255,255,0,"image03.png")

## create a julia
image(-2,1,-1.5,1.5,1000,1000,60,0.1+0.9j,"RGB",0,0,0,255,0,0,0,255,0,"image04.png")

## create another julia
image(-2,1,-1.5,1.5,1000,1000,60,0.1+0.7j,"RGB",0,0,0,0,100,0,255,0,0,"image05.png")

## create another julia
image(-2,1,-1.5,1.5,1000,1000,60,0.1+0.65j,"RGB",0,0,0,0,100,0,255,0,0,"image06.png")

## create another julia
image(-2,1,-1.5,1.5,1000,1000,60,0.1+0.63j,"RGB",0,0,0,0,100,0,255,0,0,"image07.png")

## create another julia
image(-2,1,-1.5,1.5,1000,1000,60,0.1+0.615j,"RGB",0,0,0,0,100,0,255,0,0,"image08.png")

## create another julia
image(-2,1,-1.5,1.5,1000,1000,60,0.1+0.6j,"RGB",0,0,0,0,100,0,255,0,0,"image09.png")

## create completely different julia
image(-2,1,-1.5,1.5,1000,1000,60,0.3+0.45j,"RGB",0,0,60,0,50,50,255,0,0,"image10.png")
