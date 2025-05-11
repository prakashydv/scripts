from PIL import Image
img = Image.open("League of Legends Screenshot 2019.02.25 - 14.58.48.39.png")
area = (207,41, 231, 54)
cropped_img = img.crop(area)
cropped_img.show()
cropped_img.save("output.jpg")