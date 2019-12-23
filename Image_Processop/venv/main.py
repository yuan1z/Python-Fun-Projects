from PIL import Image, ImageFilter
image = Image.open('./pikachu.jpg')
print(image.format)
print(image.size)
print(image.mode)
print(dir(image))
filtered_image = image.filter(ImageFilter.SMOOTH)
filtered_image = image.convert('L') #convert to grey scale
box = (100,100,400,400)
region = filtered_image.crop(box) #crop the image by the tuple
crooked = filtered_image.rotate(90) #rotate image by 90 degree
resize = filtered_image.resize((300,300))# resize the number of pixel of image
filtered_image.save("blur.png","png") #save image
region.save("crop.png",'png')
region.show() # show image


