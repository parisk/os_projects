import os;
import xlrd;

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
os.getcwd()
loc = ('new_directory/.xlsx')

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 

#create an empty list to store skus
mymarket_sku_lst=[]
for i in range(sheet.nrows): 
    if is_number(sheet.cell_value(i,0)):
        print(int(sheet.cell_value(i,0)))
        mymarket_sku_lst.append(int(sheet.cell_value(i,0)))

print("*" * 7)
for i in range(0, len(mymarket_sku_lst)):
    print (mymarket_sku_lst[i])