from PIL import Image
import os, shutil
from sku_patterns import *
from resizeimage import resizeimage
import re
from more_file_manip import dicti
#changes directory to image folder
os.chdir('images')

#create list of pictures in directory
image_list = [item.name for item in os.scandir('.') if item.is_file()]

print (image_list)

def determine_order(order):
    #if order is letter, return the number 1, else does nothing 
    if order in dicti.keys():
        return 0
    else:
        return order

for image in image_list:
    sku = pure_sku(image) #call on sku_patterns methods to determine sku,order, and extension
    determined_order = determine_order(pure_order(image))
    order = int(determined_order) + 1 #image must be renamed so that it is +1 higher on order
    extension = pure_extension(image)
    
    new_name = sku + "_" + str(order) + "." + extension #create new_name
    with open (image, 'rb') as i:
        with Image.open(i) as img:
            #determine image size
            width, height = img.size
            print ("Image " + image + " has dimensions ", img.size)
            if width >1000 or height>1000: #image will be resized if it exceeds 1000 in either dimension
                try:
                    print ("Now resizing file: " + image +"...")
                    cover = resizeimage.resize_cover(img, [1000,1000])
                    cover.save(new_name)
                except OSError as e:
                    print ("Error occured resizing image :" + image , e)
                finally:
                    print ("*" * 10)
            else:
                print ("----Image does not exceed 1000px in any dimension----")