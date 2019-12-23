import sys
import os
from PIL import Image,ImageFilter

old_folder =sys.argv[1]
new_folder = sys.argv[2]

if not os.path.isdir(new_folder): #check whether output folde exists
    os.mkdir(new_folder) #if not, create the folder
for file in os.listdir(old_folder): #loop though the jpg image in the input folder
    new_file = file.split('.') #seperate the file name and format
    new_file = new_file[0]+'.'+'png'
    img = Image.open(old_folder+file)
    img.save(new_folder+"/"+new_file, "png")  # save image
