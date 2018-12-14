from PIL import Image, ImageColor
from colorsys import rgb_to_hls, hls_to_rgb
import colorsys
for i in range(360):
	H=(i*20)%20
	S=i%50
	L=i%100
	rgb=colorsys.hls_to_rgb(H, L, S)
	r=rgb[0]
	g=rgb[1]
	b=rgb[2]
	print(r,g,b)