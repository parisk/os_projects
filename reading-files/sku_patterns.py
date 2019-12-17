import re
import os

SkuNumRegex = re.compile(r'(.*)_([0-9]{1,3}|[a-z]*).(jpg|jpeg|JPG|png|tif|psd)') #means SKU comes in form of 6 to 9 decimals, followed by a _ followed by 1 to 3 decimals - showing order - followed by image file extension


def pure_sku(filename):
    """prints the sku that corresponds to the image file, so everything before _"""
    try:
        result = SkuNumRegex.search(filename)
        print ("SKU that corresponds to filename is: " + result.group(1) )
    except AttributeError as e:
        print (e, filename)

def pure_order(filename, ret = False):
    """prints the number that corresponds to the order the image has in the carousel in-site, so everything between _ and ."""
    try:
        result = SkuNumRegex.search(filename)
        print ("Number that corresponds to carousel order is: " + result.group(2))
    except AttributeError as e:
        print (e, filename)
    if ret:
            return (result.group(2))
def pure_extension(filename):
    try:
        result = SkuNumRegex.search(filename)
        print ("Extension that corresponds to image type is: " + result.group(3))
    except AttributeError as e:
        print (e, filename)

for (root,directories,files) in os.walk('.'):
    if "images" in root:
        for f in files:
            print ("-"*10 + "\n" + "File is: " + f)
            try:
                pure_sku(f)
                pure_order(f)
                pure_extension(f)
            except AttributeError:
                print (f + ": this one didn't match")
print ("---Walking through directory over---")



