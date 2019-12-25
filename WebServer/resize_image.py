from PIL import Image, ImageFilter
image = Image.open('./static/Zihao.png')
new_image = image.resize((1200, 1200))
#new_image = new_image.convert('L')
new_image = new_image.filter(ImageFilter.SMOOTH())
new_image.show()
new_image.save('Zihao_large.png',quality=100)