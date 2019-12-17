import re
import os

SkuNumRegex = re.compile(r'(.*)_([0-9]{1,3}|[a-z]*).(jpg|jpeg|JPG|png|tif|psd)') #means SKU comes in form of 6 to 9 decimals, followed by a _ followed by 1 to 3 decimals - showing order - followed by image file extension
for (root,directories,files) in os.walk('.'):
    if "images" in root:
        for f in files:
            print ("-"*10 + "\n" + "File is: " + f)
            try:
                result = SkuNumRegex.search(f)
                print ("*" * 10)
                print ("Match is: " + result.group())
                print ("*" * 10)
                print ("SKU that corresponds to filename is: " + result.group(1) )
                print ("SKU that corresponds to carousel order is: " + result.group(2))
                print ("SKU that corresponds to image type is: " + result.group(3))
            except AttributeError:
                print (f + ": this one didn't match")
        
result = SkuNumRegex.search("345678-APRIL-BUND_12.jpeg")

def pure_sku (filename):
    try:
        result = SkuNumRegex.search(filename)
        pass
    except AttributeError:
        pass
    