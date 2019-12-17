import re

SkuNumRegex = re.compile(r'(.*)_([0-9]{1,3}).(jpg|jpeg|JPG|png|tif|psd)') #means SKU comes in form of 6 to 9 decimals, followed by a _ followed by 1 to 3 decimals - showing order - followed by image file extension

result = SkuNumRegex.search("345678-APRIL-BUND_12.jpeg")
print ("Match is: " + result.group())
print ("SKU that corresponds to filename is: " + result.group(1))
print ("SKU that corresponds to carousel order is: " + result.group(2))
print ("SKU that corresponds to image type is: " + result.group(3))