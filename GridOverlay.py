from PIL import Image, ImageDraw
im = Image.open("0003_inversion.jpg")

draw = ImageDraw.Draw(im)
gridSize = 40 # input("GridSize? :")
[Coffset,Roffset] = [0,0] #[int(i)%gridSize for i in raw_input("(C,R) +/- offset? : ").split()]
saveoutput = True

[C,R] = im.size
i,j=Coffset,Roffset
while i<C or j<R:
	if i>0 and i<C:
		draw.line((i,0) + (i,R), fill=255)
	if j>0 and j<R:
		draw.line((0,j) + (C,j), fill=255)
	i += gridSize
	j += gridSize		
del draw
im.show()
# write to stdout
if saveoutput :
	im.save("0003_inversion.bmp", "BMP")





	
