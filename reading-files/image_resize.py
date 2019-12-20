from PIL import Image
import os, shutil
import sku_patterns
from resizeimage import resizeimage

image_list =[]

os.chdir('images')

image_list = [item.name for item in os.scandir('.') if item.is_file()]

print (image_list)

for image in image_list:
    img = Image.open(image)
    width, height = img.size
    if width >500 or height>500:
        print ("Now resizing file: " + image +"...")
        cover = resizeimage.resize_contain(img, [300,300])
        cover.save(pure_sku(image) + (pure_order(image) +1), image.format)