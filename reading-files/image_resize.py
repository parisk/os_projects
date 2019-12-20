from PIL import Image
import os, shutil
from sku_patterns import pure_sku, pure_order, pure_extension
from resizeimage import resizeimage
import re

image_list =[]

os.chdir('images')

image_list = [item.name for item in os.scandir('.') if item.is_file()]

print (image_list)

for image in image_list:
    img = Image.open(image)
    width, height = img.size
    sku = pure_sku(image)
    order = int(pure_order(image)) +1
    extension = pure_extension(image)
    new_name = sku + "_" + str(order) + extension
    if width >500 or height>500:
        try:
            print ("Now resizing file: " + image +"...")
            cover = resizeimage.resize_contain(img, [300,300])
            cover.save(new_name, img.format)
        except OSError as e:
            print ("Error occuren at image :" + image , e)
        finally:
            