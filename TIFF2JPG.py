# Source : User MatthieuW @ http://stackoverflow.com/questions/21340740/split-tif-file-using-pil
from PIL import Image

img = Image.open('multipage.tif')

for i in range(4):
    try:
        img.seek(i)
        img.save('page_%s.tif'%(i,))
    except EOFError:
        break
