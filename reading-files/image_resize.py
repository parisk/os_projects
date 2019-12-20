from PIL import Image
import os, shutil
from sku_patterns import pure_sku, pure_order, pure_extension
from resizeimage import resizeimage
import re


#changes directory to image folder
os.chdir('images')

#create list of pictures in directory
image_list = [item.name for item in os.scandir('.') if item.is_file()]

print (image_list)

for image in image_list:
    img = Image.open(image)
    width, height = img.size
    #call on sku_patterns methods to determine sku,order, and extension
    #image must be renamed so that it is +1 higher on order
    sku = pure_sku(image)
    order = int(pure_order(image)) +1
    extension = pure_extension(image)
    
    #create new_name
    new_name = sku + "_" + str(order) + "." + extension
    
    if width >200 or height>500:
        try:
            print ("Now resizing file: " + image +"...")
            cover = resizeimage.resize_contain(img, [200,300])
            cover.save(new_name, img.format)
        except OSError as e:
            print ("Error occured resizing image :" + image , e)
        finally:
            print ("*" * 10)
    else:
        print ("----Image does not exceed 500px in any dimension----")