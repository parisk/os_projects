import shutil
import os
from sku_patterns import pure_extension, pure_sku, pure_order

path = 'images'

image_lst = [item.name for item in os.scandir(path) if item.is_file()]

stored_images_path = 'images/images_stored'

stored_images = [item.name  for item in os.scandir(stored_images_path) if item.is_file()]
print (stored_images)

for image in image_lst:
    sku = pure_sku(image)
    try:
        corresponding_images = [x for x in stored_images if sku in x] #create list of filenames that have image sku in them
        print ("images with same sku that are already stored in server for file: " + image + " are the following: " , corresponding_images)
    except TypeError as t:
        print ("Image file " + image + " does not follow specific pattern fiven. No corresponding stored images returned.")

print (image_lst)