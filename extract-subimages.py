from PIL import Image
import os
area = (1666,6,1746,23)
index = 0

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filepath = os.path.join(subdir, file)
        if file.find("bmp")>=0:
            img = Image.open(filepath)
            cropped_img = img.crop(area)
            # cropped_img.show()
            cropped_img.save("subimage_%05d.bmp"%(index))
            img.close()
            print(filepath)
            index += 1
            # break
            






