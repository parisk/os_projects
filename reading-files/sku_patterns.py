import re
import os


def pure_sku(filename):
    """prints the sku that corresponds to the image file, so everything before _"""
    
    SkuNumRegex = re.compile(r'(.*)_([0-9]{1,3}|[a-z]*).(jpg|jpeg|JPG|png|tif|psd)') #means SKU comes in form of 6 to 9 decimals, followed by a _ followed by 1 to 3 decimals - showing order - followed by image file extension
    try:
        result = SkuNumRegex.search(filename)
        sku = result.group(3)
        print ("SKU that corresponds to filename is: " + result.group(1))
        return sku
    except AttributeError as e:
        print (e, filename)

def pure_order(filename, ret = False):
    """prints the number that corresponds to the order the image has in the carousel in-site, so everything between _ and ."""
    SkuNumRegex = re.compile(r'(.*)_([0-9]{1,3}|[a-z]*).(jpg|jpeg|JPG|png|tif|psd)') #means SKU comes in form of 6 to 9 decimals, followed by a _ followed by 1 to 3 decimals - showing order - followed by image file extension
    try:
        result = SkuNumRegex.search(filename)
        order = result.group(3)
        print ("Number that corresponds to carousel order is: " + result.group(2))
        return order
    except AttributeError as e:
        print (e, filename)
    
def pure_extension(filename):
    SkuNumRegex = re.compile(r'(.*)_([0-9]{1,3}|[a-z]*).(jpg|jpeg|JPG|png|tif|psd)') #means SKU comes in form of 6 to 9 decimals, followed by a _ followed by 1 to 3 decimals - showing order - followed by image file extension
    try:
        result = SkuNumRegex.search(filename)
        extension = result.group(3)
        print ("Extension that corresponds to image type is: " + result.group(3))
        return extension
    except AttributeError as e:
        print (e, filename)
        
#main execution
if __name__ = "__main__":
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

    def rename_order(filename):
        pass
    print ("---Walking through directory over---")



