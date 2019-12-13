Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os, shutil, fnmatch
>>> os.getcwd()
'C:\\Users\\mpitsalidis\\AppData\\Local\\Programs\\Python\\Python38'
>>> os.chdir('C:\\Users\\mpitsalidis\\Desktop')
>>> os.getcwd()
'C:\\Users\\mpitsalidis\\Desktop'
>>> os. listdir('.')
['12152054_t.jpg', '3E', '401094_d.jpg', '7th Generation', 'Airwick', 'Amita - Juices', 'ariel 27-11-2017', 'Atom.lnk', 'BARCODES', 'BIC ΣΧΟΛΙΚΑ', 'Canderel', 'Coca-Cola', 'desktop.ini', 'Dettol_SKUs_Hazard_Sign.JPG', 'elbisco', 'elvive', 'Energizer', 'ESHOP', 'Excel με κωδικούς Εταιριών', 'export-rich-content 27-11-2019_files', 'FANTA', 'Fitness Bio', 'Fotos Delice&Lion&Friskies', 'gda_template.xlsx', 'gilette_new_skus_aug_19', 'hellmans', 'henkel', 'herbal essences', 'HIPP', 'j&j', 'jacobs', 'jde', 'JDE September 2019', 'Johnson & Johnson', 'Landing Pages - RIch Content Pages (Atom Projects)', 'landing_page_code.txt', 'maybelline', 'megales_perigrafes_49.xlsx', 'MILESTONE SM21', 'MITSUKO', 'mns_password_papaki.txt', 'MY', 'My Φυλλαδίου 15-5', 'Nestle', 'Nestle December 19', 'Nestle November 2019', 'Nestle October 2019', 'Nestle September 2019', 'nestle παγωτα', 'Nivea Hazards', 'NOYNOY Classic', 'Oral-B Rich Content', 'p&g', 'p&g rich content', 'Pampers new Packshots', 'Pampers Visuals', 'Perrier', 'PL Φωτο χωρίς Κωδικό', 'primo gusto', 'primo gusto gda', 'Purina Dentalife 25-11-2019', 'Python', 'Reckitt', 'rich_content_reports', 'Santigy', 'SC Johnson', 'shell_removing_files.py', 'Skip September 2019', 'sm24', 'Spotify.lnk', 'Sprite', 'test.JPG', 'test2.JPG', 'TUBORG', 'Unilever 18-10-2019', 'Unilever 23-10-2019', 'Unilever Oral & Deos Αλλαγές November 2019', 'VILEDA', 'WET HANKIES NEW- BC CALMING_18.09.19', '~$megales_perigrafes_22.xlsx', 'ΑΘΗΝΑΙΚΗ ΖΥΘΟΠΟΙΙΑ', 'Αλλαγές eshop 20-11-2019', 'Αλλαγές σε φωτό site από Πρίντεζη, 18-11-2019', 'ατλαντα', 'βιολαντα', 'Διατροφικά-Κίνδυνοι 6-11-2019', 'ΔΙΑΤΡΟΦΙΚΑ', 'Είδη_sm24.xlsx', 'ΚΡΗΤΩΝ ΑΡΤΟΣ', 'ΜΕΓΑ', 'ΜΕΓΑΛΕΣ  ΠΕΡΙΓΡΑΦΕΣ', 'ΝΕΣΤΛΕ 13-8', 'ΟΛΥΜΠΟΣ 29-5', 'Πρόσθετα Εικαστικά MY', 'ΠΡΙΝΤΕΖΗΣ ΔΙΑΤΡΟΦΙΚΑ 15-11', 'ΠΡΟΦΥΛΑΞΕΙΣ', 'ΣΧΟΛΙΚΑ 2019', 'ΦΩΤΟΓΡΑΦΙΣΗ ΠΡΙΝΤΕΖΗ 2-11-2019', 'ΦΩΤΟΓΡΑΦΙΣΗ ΠΡΙΝΤΕΖΗ 2-12-2019']
>>> os.chdir('Unilever Oral & Deos Αλλαγές November 2019')
>>> os.listdir('.')
['Aim', 'Axe', 'Dove', 'Rexona -done']
>>> os.chdir('Axe')
>>> axe_local = [item.name for item in os.scandir('.')]
>>> print (axe_local)
['Axe Deo Roll On Africa 50ml 50097265.jpg', 'Axe Deo Roll On Black 50ml 96100561.tif', 'Axe Deo Roll On Dark Temptation 50ml 50098026.TIF', 'Axe Deo Roll On Ice Chill 50ml 59079378.tif', 'Axe Deo Roll-On Gold 50ml 87342802.tif', 'Axe Deo Spray Africa 150ml 8710447497272.tif', 'Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tif', 'Axe Deo Spray Apollo 150ml 8710447484258.tif', 'Axe Deo Spray Black 150ml 8710447484289.tif', 'Axe Deo Spray Black Night 150ml 8710908052040.tif', 'Axe Deo Spray Dark Temptation 150ml 8717163640821.tif', 'Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tif', 'Axe Deo Spray Dry Gold 150ml 8710447248973.tif', 'Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tif', 'Axe Deo Spray Gold 150ml 8710447249017.tif', 'Axe Deo Spray Gold Temptation 150ml 8710447484418.tif', 'Axe Deo Spray Ice Chill 150ml 8710447497340.tif', 'Axe Deo Spray Marine 150ml 8710447484500.tif', 'Axe Deo Spray You 150ml 8710447484555.tif', 'Axe Roll On Dry Gold 50ml 87342802 (hero).png', 'Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpg', 'Black.tif']
>>> Import re
SyntaxError: invalid syntax
>>> import re
>>> code = 678854_1.jpeg
SyntaxError: invalid syntax
>>> code ='678854_1.jpeg'
>>> x = re.search([0-9]{6,7}, code)
SyntaxError: invalid syntax
>>> x = re.search(^[0-9]{6,7}$, code)
SyntaxError: invalid syntax
>>> x = re.search("^[0-9]{6,7}$", code)
>>> print (x)
None
>>> x = re.search("[0-9]{6,7}", code)
>>> print (x)
<re.Match object; span=(0, 6), match='678854'>
>>> x = re.search("[0-9]{6}", code)
>>> if x is not None:
	print ('matches')

	
matches
>>> x = re.search("[0-9]{6}_", code)
\
>>> print (x)
<re.Match object; span=(0, 7), match='678854_'>
>>> x = re.search("[0-9]{6}_[0-9]{1,2}.[a-z]{3,4}", code)
>>> print (x)
<re.Match object; span=(0, 13), match='678854_1.jpeg'>
>>> print (x.group(2))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print (x.group(2))
IndexError: no such group
>>> print x.group(1)
SyntaxError: invalid syntax
>>> print (x.group(1))
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print (x.group(1))
IndexError: no such group
>>> print (x.group(0))
678854_1.jpeg
>>> x = re.search("[0-9]{6}","_[0-9]{1,2}.[a-z]{3,4}", code)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x = re.search("[0-9]{6}","_[0-9]{1,2}.[a-z]{3,4}", code)
  File "C:\Users\mpitsalidis\AppData\Local\Programs\Python\Python38\lib\re.py", line 199, in search
    return _compile(pattern, flags).search(string)
  File "C:\Users\mpitsalidis\AppData\Local\Programs\Python\Python38\lib\re.py", line 302, in _compile
    p = sre_compile.compile(pattern, flags)
  File "C:\Users\mpitsalidis\AppData\Local\Programs\Python\Python38\lib\sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "C:\Users\mpitsalidis\AppData\Local\Programs\Python\Python38\lib\sre_parse.py", line 948, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
TypeError: unsupported operand type(s) for &: 'str' and 'int'
>>> if (x):
	print ("ii")

	
ii
>>> x = x = re.search("[0-9]{6}_[0-9]{1,2}.[a-z]{3,4}", "099921_6.png")
>>> if (x):
	print("ues')
	      
SyntaxError: EOL while scanning string literal
>>> 
>>> if (x):
	print ("ues")

	
ues
>>> os.getcwd()
'C:\\Users\\mpitsalidis\\Desktop\\Unilever Oral & Deos Αλλαγές November 2019\\Axe'
>>> os.listdir('.')
['Axe Deo Roll On Africa 50ml 50097265.jpg', 'Axe Deo Roll On Black 50ml 96100561.tif', 'Axe Deo Roll On Dark Temptation 50ml 50098026.TIF', 'Axe Deo Roll On Ice Chill 50ml 59079378.tif', 'Axe Deo Roll-On Gold 50ml 87342802.tif', 'Axe Deo Spray Africa 150ml 8710447497272.tif', 'Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tif', 'Axe Deo Spray Apollo 150ml 8710447484258.tif', 'Axe Deo Spray Black 150ml 8710447484289.tif', 'Axe Deo Spray Black Night 150ml 8710908052040.tif', 'Axe Deo Spray Dark Temptation 150ml 8717163640821.tif', 'Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tif', 'Axe Deo Spray Dry Gold 150ml 8710447248973.tif', 'Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tif', 'Axe Deo Spray Gold 150ml 8710447249017.tif', 'Axe Deo Spray Gold Temptation 150ml 8710447484418.tif', 'Axe Deo Spray Ice Chill 150ml 8710447497340.tif', 'Axe Deo Spray Marine 150ml 8710447484500.tif', 'Axe Deo Spray You 150ml 8710447484555.tif', 'Axe Roll On Dry Gold 50ml 87342802 (hero).png', 'Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpg', 'Black.tif']
>>> Os.listdir('.')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    Os.listdir('.')
NameError: name 'Os' is not defined
>>> os.listdir('.')
['Axe Deo Roll On Africa 50ml 50097265.jpg', 'Axe Deo Roll On Black 50ml 96100561.tif', 'Axe Deo Roll On Dark Temptation 50ml 50098026.TIF', 'Axe Deo Roll On Ice Chill 50ml 59079378.tif', 'Axe Deo Roll-On Gold 50ml 87342802.tif', 'Axe Deo Spray Africa 150ml 8710447497272.tif', 'Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tif', 'Axe Deo Spray Apollo 150ml 8710447484258.tif', 'Axe Deo Spray Black 150ml 8710447484289.tif', 'Axe Deo Spray Black Night 150ml 8710908052040.tif', 'Axe Deo Spray Dark Temptation 150ml 8717163640821.tif', 'Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tif', 'Axe Deo Spray Dry Gold 150ml 8710447248973.tif', 'Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tif', 'Axe Deo Spray Gold 150ml 8710447249017.tif', 'Axe Deo Spray Gold Temptation 150ml 8710447484418.tif', 'Axe Deo Spray Ice Chill 150ml 8710447497340.tif', 'Axe Deo Spray Marine 150ml 8710447484500.tif', 'Axe Deo Spray You 150ml 8710447484555.tif', 'Axe Roll On Dry Gold 50ml 87342802 (hero).png', 'Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpg', 'Black.tif']
>>> for item in os.listdir('.'):
	x = re.match("[0-9]{8,14}.",item)
	if x:
		print ("Item " + item + "matches pattern")

		
>>> for item in os.listdir('.'):
	x = re.match("[0-9]{8,14}.",item)
	if x:
		print ("Item " + item + "matches pattern")

		
>>> for item in os.listdir('.'):
	x = re.match("[0-9]{8,14}.",item)
	if x:
	    print ("Item " + item + "matches pattern")

	    
>>> for item in os.listdir('.'):
	print (item)
	x = re.match("[0-9]{8,14}.",item)
	if x:
	    print ("Item " + item + "matches pattern")

	    
Axe Deo Roll On Africa 50ml 50097265.jpg
Axe Deo Roll On Black 50ml 96100561.tif
Axe Deo Roll On Dark Temptation 50ml 50098026.TIF
Axe Deo Roll On Ice Chill 50ml 59079378.tif
Axe Deo Roll-On Gold 50ml 87342802.tif
Axe Deo Spray Africa 150ml 8710447497272.tif
Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tif
Axe Deo Spray Apollo 150ml 8710447484258.tif
Axe Deo Spray Black 150ml 8710447484289.tif
Axe Deo Spray Black Night 150ml 8710908052040.tif
Axe Deo Spray Dark Temptation 150ml 8717163640821.tif
Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tif
Axe Deo Spray Dry Gold 150ml 8710447248973.tif
Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tif
Axe Deo Spray Gold 150ml 8710447249017.tif
Axe Deo Spray Gold Temptation 150ml 8710447484418.tif
Axe Deo Spray Ice Chill 150ml 8710447497340.tif
Axe Deo Spray Marine 150ml 8710447484500.tif
Axe Deo Spray You 150ml 8710447484555.tif
Axe Roll On Dry Gold 50ml 87342802 (hero).png
Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpg
Black.tif
>>> for item in os.listdir('.'):
	print (item)
	x = re.match(" [0-9]{8,14}.",item)
	if x:
	    print ("Item " + item + "matches pattern")

	    
Axe Deo Roll On Africa 50ml 50097265.jpg
Axe Deo Roll On Black 50ml 96100561.tif
Axe Deo Roll On Dark Temptation 50ml 50098026.TIF
Axe Deo Roll On Ice Chill 50ml 59079378.tif
Axe Deo Roll-On Gold 50ml 87342802.tif
Axe Deo Spray Africa 150ml 8710447497272.tif
Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tif
Axe Deo Spray Apollo 150ml 8710447484258.tif
Axe Deo Spray Black 150ml 8710447484289.tif
Axe Deo Spray Black Night 150ml 8710908052040.tif
Axe Deo Spray Dark Temptation 150ml 8717163640821.tif
Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tif
Axe Deo Spray Dry Gold 150ml 8710447248973.tif
Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tif
Axe Deo Spray Gold 150ml 8710447249017.tif
Axe Deo Spray Gold Temptation 150ml 8710447484418.tif
Axe Deo Spray Ice Chill 150ml 8710447497340.tif
Axe Deo Spray Marine 150ml 8710447484500.tif
Axe Deo Spray You 150ml 8710447484555.tif
Axe Roll On Dry Gold 50ml 87342802 (hero).png
Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpg
Black.tif
>>> import re
>>> for item in os.listdir('.'):
	print (item)
	x = re.match("[0-9]{8,14}.",item)
	if x:
	    print ("Item " + item + "matches pattern")

	    
Axe Deo Roll On Africa 50ml 50097265.jpg
Axe Deo Roll On Black 50ml 96100561.tif
Axe Deo Roll On Dark Temptation 50ml 50098026.TIF
Axe Deo Roll On Ice Chill 50ml 59079378.tif
Axe Deo Roll-On Gold 50ml 87342802.tif
Axe Deo Spray Africa 150ml 8710447497272.tif
Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tif
Axe Deo Spray Apollo 150ml 8710447484258.tif
Axe Deo Spray Black 150ml 8710447484289.tif
Axe Deo Spray Black Night 150ml 8710908052040.tif
Axe Deo Spray Dark Temptation 150ml 8717163640821.tif
Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tif
Axe Deo Spray Dry Gold 150ml 8710447248973.tif
Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tif
Axe Deo Spray Gold 150ml 8710447249017.tif
Axe Deo Spray Gold Temptation 150ml 8710447484418.tif
Axe Deo Spray Ice Chill 150ml 8710447497340.tif
Axe Deo Spray Marine 150ml 8710447484500.tif
Axe Deo Spray You 150ml 8710447484555.tif
Axe Roll On Dry Gold 50ml 87342802 (hero).png
Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpg
Black.tif
>>> for item in os.listdir('.'):
	print (item)
	x = re.search("[0-9]{8,14}.",item)
	if x:
	    print ("Item " + item + "matches pattern")

	    
Axe Deo Roll On Africa 50ml 50097265.jpg
Item Axe Deo Roll On Africa 50ml 50097265.jpgmatches pattern
Axe Deo Roll On Black 50ml 96100561.tif
Item Axe Deo Roll On Black 50ml 96100561.tifmatches pattern
Axe Deo Roll On Dark Temptation 50ml 50098026.TIF
Item Axe Deo Roll On Dark Temptation 50ml 50098026.TIFmatches pattern
Axe Deo Roll On Ice Chill 50ml 59079378.tif
Item Axe Deo Roll On Ice Chill 50ml 59079378.tifmatches pattern
Axe Deo Roll-On Gold 50ml 87342802.tif
Item Axe Deo Roll-On Gold 50ml 87342802.tifmatches pattern
Axe Deo Spray Africa 150ml 8710447497272.tif
Item Axe Deo Spray Africa 150ml 8710447497272.tifmatches pattern
Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tif
Item Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tifmatches pattern
Axe Deo Spray Apollo 150ml 8710447484258.tif
Item Axe Deo Spray Apollo 150ml 8710447484258.tifmatches pattern
Axe Deo Spray Black 150ml 8710447484289.tif
Item Axe Deo Spray Black 150ml 8710447484289.tifmatches pattern
Axe Deo Spray Black Night 150ml 8710908052040.tif
Item Axe Deo Spray Black Night 150ml 8710908052040.tifmatches pattern
Axe Deo Spray Dark Temptation 150ml 8717163640821.tif
Item Axe Deo Spray Dark Temptation 150ml 8717163640821.tifmatches pattern
Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tif
Item Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tifmatches pattern
Axe Deo Spray Dry Gold 150ml 8710447248973.tif
Item Axe Deo Spray Dry Gold 150ml 8710447248973.tifmatches pattern
Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tif
Item Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tifmatches pattern
Axe Deo Spray Gold 150ml 8710447249017.tif
Item Axe Deo Spray Gold 150ml 8710447249017.tifmatches pattern
Axe Deo Spray Gold Temptation 150ml 8710447484418.tif
Item Axe Deo Spray Gold Temptation 150ml 8710447484418.tifmatches pattern
Axe Deo Spray Ice Chill 150ml 8710447497340.tif
Item Axe Deo Spray Ice Chill 150ml 8710447497340.tifmatches pattern
Axe Deo Spray Marine 150ml 8710447484500.tif
Item Axe Deo Spray Marine 150ml 8710447484500.tifmatches pattern
Axe Deo Spray You 150ml 8710447484555.tif
Item Axe Deo Spray You 150ml 8710447484555.tifmatches pattern
Axe Roll On Dry Gold 50ml 87342802 (hero).png
Item Axe Roll On Dry Gold 50ml 87342802 (hero).pngmatches pattern
Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpg
Item Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpgmatches pattern
Black.tif
>>> for item in os.listdir('.'):
	print (item)
	x = re.match("[0-9]{8,14}.",item)
	if x:
	    print ("Item " + item + " matches pattern")

	    
Axe Deo Roll On Africa 50ml 50097265.jpg
Axe Deo Roll On Black 50ml 96100561.tif
Axe Deo Roll On Dark Temptation 50ml 50098026.TIF
Axe Deo Roll On Ice Chill 50ml 59079378.tif
Axe Deo Roll-On Gold 50ml 87342802.tif
Axe Deo Spray Africa 150ml 8710447497272.tif
Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tif
Axe Deo Spray Apollo 150ml 8710447484258.tif
Axe Deo Spray Black 150ml 8710447484289.tif
Axe Deo Spray Black Night 150ml 8710908052040.tif
Axe Deo Spray Dark Temptation 150ml 8717163640821.tif
Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tif
Axe Deo Spray Dry Gold 150ml 8710447248973.tif
Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tif
Axe Deo Spray Gold 150ml 8710447249017.tif
Axe Deo Spray Gold Temptation 150ml 8710447484418.tif
Axe Deo Spray Ice Chill 150ml 8710447497340.tif
Axe Deo Spray Marine 150ml 8710447484500.tif
Axe Deo Spray You 150ml 8710447484555.tif
Axe Roll On Dry Gold 50ml 87342802 (hero).png
Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpg
Black.tif
>>> for item in os.listdir('.'):
	print (item)
	x = re.search("[0-9]{8,14}.",item)
	if x:
	    print ("Item " + item + "matches pattern")

	    
Axe Deo Roll On Africa 50ml 50097265.jpg
Item Axe Deo Roll On Africa 50ml 50097265.jpgmatches pattern
Axe Deo Roll On Black 50ml 96100561.tif
Item Axe Deo Roll On Black 50ml 96100561.tifmatches pattern
Axe Deo Roll On Dark Temptation 50ml 50098026.TIF
Item Axe Deo Roll On Dark Temptation 50ml 50098026.TIFmatches pattern
Axe Deo Roll On Ice Chill 50ml 59079378.tif
Item Axe Deo Roll On Ice Chill 50ml 59079378.tifmatches pattern
Axe Deo Roll-On Gold 50ml 87342802.tif
Item Axe Deo Roll-On Gold 50ml 87342802.tifmatches pattern
Axe Deo Spray Africa 150ml 8710447497272.tif
Item Axe Deo Spray Africa 150ml 8710447497272.tifmatches pattern
Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tif
Item Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tifmatches pattern
Axe Deo Spray Apollo 150ml 8710447484258.tif
Item Axe Deo Spray Apollo 150ml 8710447484258.tifmatches pattern
Axe Deo Spray Black 150ml 8710447484289.tif
Item Axe Deo Spray Black 150ml 8710447484289.tifmatches pattern
Axe Deo Spray Black Night 150ml 8710908052040.tif
Item Axe Deo Spray Black Night 150ml 8710908052040.tifmatches pattern
Axe Deo Spray Dark Temptation 150ml 8717163640821.tif
Item Axe Deo Spray Dark Temptation 150ml 8717163640821.tifmatches pattern
Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tif
Item Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tifmatches pattern
Axe Deo Spray Dry Gold 150ml 8710447248973.tif
Item Axe Deo Spray Dry Gold 150ml 8710447248973.tifmatches pattern
Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tif
Item Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tifmatches pattern
Axe Deo Spray Gold 150ml 8710447249017.tif
Item Axe Deo Spray Gold 150ml 8710447249017.tifmatches pattern
Axe Deo Spray Gold Temptation 150ml 8710447484418.tif
Item Axe Deo Spray Gold Temptation 150ml 8710447484418.tifmatches pattern
Axe Deo Spray Ice Chill 150ml 8710447497340.tif
Item Axe Deo Spray Ice Chill 150ml 8710447497340.tifmatches pattern
Axe Deo Spray Marine 150ml 8710447484500.tif
Item Axe Deo Spray Marine 150ml 8710447484500.tifmatches pattern
Axe Deo Spray You 150ml 8710447484555.tif
Item Axe Deo Spray You 150ml 8710447484555.tifmatches pattern
Axe Roll On Dry Gold 50ml 87342802 (hero).png
Item Axe Roll On Dry Gold 50ml 87342802 (hero).pngmatches pattern
Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpg
Item Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpgmatches pattern
Black.tif
>>> for item in os.listdir('.'):
	x = re.search("[0-9]{8,14}.",item)
	if x:
	    print ("Item " + item + "matches pattern")

	    
Item Axe Deo Roll On Africa 50ml 50097265.jpgmatches pattern
Item Axe Deo Roll On Black 50ml 96100561.tifmatches pattern
Item Axe Deo Roll On Dark Temptation 50ml 50098026.TIFmatches pattern
Item Axe Deo Roll On Ice Chill 50ml 59079378.tifmatches pattern
Item Axe Deo Roll-On Gold 50ml 87342802.tifmatches pattern
Item Axe Deo Spray Africa 150ml 8710447497272.tifmatches pattern
Item Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tifmatches pattern
Item Axe Deo Spray Apollo 150ml 8710447484258.tifmatches pattern
Item Axe Deo Spray Black 150ml 8710447484289.tifmatches pattern
Item Axe Deo Spray Black Night 150ml 8710908052040.tifmatches pattern
Item Axe Deo Spray Dark Temptation 150ml 8717163640821.tifmatches pattern
Item Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tifmatches pattern
Item Axe Deo Spray Dry Gold 150ml 8710447248973.tifmatches pattern
Item Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tifmatches pattern
Item Axe Deo Spray Gold 150ml 8710447249017.tifmatches pattern
Item Axe Deo Spray Gold Temptation 150ml 8710447484418.tifmatches pattern
Item Axe Deo Spray Ice Chill 150ml 8710447497340.tifmatches pattern
Item Axe Deo Spray Marine 150ml 8710447484500.tifmatches pattern
Item Axe Deo Spray You 150ml 8710447484555.tifmatches pattern
Item Axe Roll On Dry Gold 50ml 87342802 (hero).pngmatches pattern
Item Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpgmatches pattern
>>> counter = 0
>>> for item in os.listdir('.'):
	print (item)
	x = re.search("[0-9]{8,14}.",item)
	if x:
		counter += 1
	    print ("Item " + item + "matches pattern")
	    
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> for item in os.listdir('.'):
	print (item)
	x = re.search("[0-9]{8,14}.",item)
	if x:
		counter +=1
		print ("Item " + item + "matches pattern")

		
Axe Deo Roll On Africa 50ml 50097265.jpg
Item Axe Deo Roll On Africa 50ml 50097265.jpgmatches pattern
Axe Deo Roll On Black 50ml 96100561.tif
Item Axe Deo Roll On Black 50ml 96100561.tifmatches pattern
Axe Deo Roll On Dark Temptation 50ml 50098026.TIF
Item Axe Deo Roll On Dark Temptation 50ml 50098026.TIFmatches pattern
Axe Deo Roll On Ice Chill 50ml 59079378.tif
Item Axe Deo Roll On Ice Chill 50ml 59079378.tifmatches pattern
Axe Deo Roll-On Gold 50ml 87342802.tif
Item Axe Deo Roll-On Gold 50ml 87342802.tifmatches pattern
Axe Deo Spray Africa 150ml 8710447497272.tif
Item Axe Deo Spray Africa 150ml 8710447497272.tifmatches pattern
Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tif
Item Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tifmatches pattern
Axe Deo Spray Apollo 150ml 8710447484258.tif
Item Axe Deo Spray Apollo 150ml 8710447484258.tifmatches pattern
Axe Deo Spray Black 150ml 8710447484289.tif
Item Axe Deo Spray Black 150ml 8710447484289.tifmatches pattern
Axe Deo Spray Black Night 150ml 8710908052040.tif
Item Axe Deo Spray Black Night 150ml 8710908052040.tifmatches pattern
Axe Deo Spray Dark Temptation 150ml 8717163640821.tif
Item Axe Deo Spray Dark Temptation 150ml 8717163640821.tifmatches pattern
Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tif
Item Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tifmatches pattern
Axe Deo Spray Dry Gold 150ml 8710447248973.tif
Item Axe Deo Spray Dry Gold 150ml 8710447248973.tifmatches pattern
Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tif
Item Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tifmatches pattern
Axe Deo Spray Gold 150ml 8710447249017.tif
Item Axe Deo Spray Gold 150ml 8710447249017.tifmatches pattern
Axe Deo Spray Gold Temptation 150ml 8710447484418.tif
Item Axe Deo Spray Gold Temptation 150ml 8710447484418.tifmatches pattern
Axe Deo Spray Ice Chill 150ml 8710447497340.tif
Item Axe Deo Spray Ice Chill 150ml 8710447497340.tifmatches pattern
Axe Deo Spray Marine 150ml 8710447484500.tif
Item Axe Deo Spray Marine 150ml 8710447484500.tifmatches pattern
Axe Deo Spray You 150ml 8710447484555.tif
Item Axe Deo Spray You 150ml 8710447484555.tifmatches pattern
Axe Roll On Dry Gold 50ml 87342802 (hero).png
Item Axe Roll On Dry Gold 50ml 87342802 (hero).pngmatches pattern
Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpg
Item Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpgmatches pattern
Black.tif
>>> for item in os.listdir('.'):
	x = re.search("[0-9]{8,14}.",item)
	if x:
		counter +=1
		print ("Item " + item + "matches pattern")

		
Item Axe Deo Roll On Africa 50ml 50097265.jpgmatches pattern
Item Axe Deo Roll On Black 50ml 96100561.tifmatches pattern
Item Axe Deo Roll On Dark Temptation 50ml 50098026.TIFmatches pattern
Item Axe Deo Roll On Ice Chill 50ml 59079378.tifmatches pattern
Item Axe Deo Roll-On Gold 50ml 87342802.tifmatches pattern
Item Axe Deo Spray Africa 150ml 8710447497272.tifmatches pattern
Item Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tifmatches pattern
Item Axe Deo Spray Apollo 150ml 8710447484258.tifmatches pattern
Item Axe Deo Spray Black 150ml 8710447484289.tifmatches pattern
Item Axe Deo Spray Black Night 150ml 8710908052040.tifmatches pattern
Item Axe Deo Spray Dark Temptation 150ml 8717163640821.tifmatches pattern
Item Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tifmatches pattern
Item Axe Deo Spray Dry Gold 150ml 8710447248973.tifmatches pattern
Item Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tifmatches pattern
Item Axe Deo Spray Gold 150ml 8710447249017.tifmatches pattern
Item Axe Deo Spray Gold Temptation 150ml 8710447484418.tifmatches pattern
Item Axe Deo Spray Ice Chill 150ml 8710447497340.tifmatches pattern
Item Axe Deo Spray Marine 150ml 8710447484500.tifmatches pattern
Item Axe Deo Spray You 150ml 8710447484555.tifmatches pattern
Item Axe Roll On Dry Gold 50ml 87342802 (hero).pngmatches pattern
Item Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpgmatches pattern
>>> for item in os.listdir('.'):
	x = re.search("[0-9]{8,14}.",item)
	if x:
		counter +=1
		print ("Item " + item + " matches pattern")

		
Item Axe Deo Roll On Africa 50ml 50097265.jpg matches pattern
Item Axe Deo Roll On Black 50ml 96100561.tif matches pattern
Item Axe Deo Roll On Dark Temptation 50ml 50098026.TIF matches pattern
Item Axe Deo Roll On Ice Chill 50ml 59079378.tif matches pattern
Item Axe Deo Roll-On Gold 50ml 87342802.tif matches pattern
Item Axe Deo Spray Africa 150ml 8710447497272.tif matches pattern
Item Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tif matches pattern
Item Axe Deo Spray Apollo 150ml 8710447484258.tif matches pattern
Item Axe Deo Spray Black 150ml 8710447484289.tif matches pattern
Item Axe Deo Spray Black Night 150ml 8710908052040.tif matches pattern
Item Axe Deo Spray Dark Temptation 150ml 8717163640821.tif matches pattern
Item Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tif matches pattern
Item Axe Deo Spray Dry Gold 150ml 8710447248973.tif matches pattern
Item Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tif matches pattern
Item Axe Deo Spray Gold 150ml 8710447249017.tif matches pattern
Item Axe Deo Spray Gold Temptation 150ml 8710447484418.tif matches pattern
Item Axe Deo Spray Ice Chill 150ml 8710447497340.tif matches pattern
Item Axe Deo Spray Marine 150ml 8710447484500.tif matches pattern
Item Axe Deo Spray You 150ml 8710447484555.tif matches pattern
Item Axe Roll On Dry Gold 50ml 87342802 (hero).png matches pattern
Item Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpg matches pattern
>>> for item in os.listdir('.'):
	x = re.search("[0-9]{8,14}.",item)
	if x:
		counter +=1
		print ("Item " + item + " matches pattern")
		os.rename (item, x.group(0))

		
Item Axe Deo Roll On Africa 50ml 50097265.jpg matches pattern
Item Axe Deo Roll On Black 50ml 96100561.tif matches pattern
Item Axe Deo Roll On Dark Temptation 50ml 50098026.TIF matches pattern
Item Axe Deo Roll On Ice Chill 50ml 59079378.tif matches pattern
Item Axe Deo Roll-On Gold 50ml 87342802.tif matches pattern
Item Axe Deo Spray Africa 150ml 8710447497272.tif matches pattern
Item Axe Deo Spray Apollo 150ml 8710447484258 - Copy.tif matches pattern
Item Axe Deo Spray Apollo 150ml 8710447484258.tif matches pattern
Traceback (most recent call last):
  File "<pyshell#81>", line 6, in <module>
    os.rename (item, x.group(0))
FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'Axe Deo Spray Apollo 150ml 8710447484258.tif' -> '8710447484258.'
>>> for item in os.listdir('.'):
	x = re.search("[0-9]{8,14}.",item)
	if x:
		counter +=1
		print ("Item " + item + " matches pattern")
		try:
			os.rename (item, x.group(0) + ".jpg")
		except FileExistsError:
			print ("Could not rename " + item)

			
Item 50097265.jpg matches pattern
Item 8710447484258 matches pattern
Item 8710447497272 matches pattern
Item Axe Deo Spray Apollo 150ml 8710447484258.tif matches pattern
Item Axe Deo Spray Black 150ml 8710447484289.tif matches pattern
Item Axe Deo Spray Black Night 150ml 8710908052040.tif matches pattern
Item Axe Deo Spray Dark Temptation 150ml 8717163640821.tif matches pattern
Item Axe Deo Spray Dry Dark Temptation 150ml 8717644256183.tif matches pattern
Item Axe Deo Spray Dry Gold 150ml 8710447248973.tif matches pattern
Item Axe Deo Spray Dry Ice Chill 150ml 8717163640852.tif matches pattern
Item Axe Deo Spray Gold 150ml 8710447249017.tif matches pattern
Item Axe Deo Spray Gold Temptation 150ml 8710447484418.tif matches pattern
Item Axe Deo Spray Ice Chill 150ml 8710447497340.tif matches pattern
Item Axe Deo Spray Marine 150ml 8710447484500.tif matches pattern
Item Axe Deo Spray You 150ml 8710447484555.tif matches pattern
Item Axe Roll On Dry Gold 50ml 87342802 (hero).png matches pattern
Item Axe Spray Collision Leader & Cookies 150ml 8710447448199.jpg matches pattern
>>> for item in os.listdir('.'):
	x = re.search("[0-9]{8,14}",item)
	if x:
		counter +=1
		print ("Item " + item + " matches pattern")
		try:
			os.rename (item, x.group(0) + ".jpg")
		except FileExistsError:
			print ("Could not rename " + item)

			
Item 50097265..jpg matches pattern
Item 50098026 matches pattern
Item 59079378 matches pattern
Item 8710447248973..jpg matches pattern
Item 8710447249017..jpg matches pattern
Item 8710447448199..jpg matches pattern
Item 8710447484258..jpg matches pattern
Could not rename 8710447484258..jpg
Item 8710447484258.jpg matches pattern
Item 8710447484289..jpg matches pattern
Item 8710447484418..jpg matches pattern
Item 8710447484500..jpg matches pattern
Item 8710447484555..jpg matches pattern
Item 8710447497272.jpg matches pattern
Item 8710447497340..jpg matches pattern
Item 8710908052040..jpg matches pattern
Item 8717163640821..jpg matches pattern
Item 8717163640852..jpg matches pattern
Item 8717644256183..jpg matches pattern
Item 87342802 matches pattern
Item 87342802 .jpg matches pattern
Could not rename 87342802 .jpg
Item 96100561 matches pattern
>>> os.chdir('..')
>>> os.listdir('.')
['Aim', 'Axe', 'Dove', 'Rexona -done']
>>> os.chdir('Aim')
>>> for item in os.listdir('.'):
	x = re.search("[0-9]{8,14}",item)
	if x:
		counter +=1
		print ("Item " + item + " matches pattern")
		try:
			os.rename (item, x.group(0) + ".jpg")
		except FileExistsError:
			print ("Could not rename " + item)
			os.rename (item, x.group(0) +"_1.jpg")

			
Item 5201028118950.jpg matches pattern
Item 5201028124104.jpg matches pattern
Item 5201028125514.(2).jpg matches pattern
Item 5201028125514.(4).jpg matches pattern
Could not rename 5201028125514.(4).jpg
Item 8710522371787.jpg matches pattern
Item 8710522404805.jpg matches pattern
Item 8710908436758.png matches pattern
Item 8711600601253.tif matches pattern
Item 8711600821552 (2).jpg matches pattern
Could not rename 8711600821552 (2).jpg
Item 8711600821552 (3).jpg matches pattern
Could not rename 8711600821552 (3).jpg
Traceback (most recent call last):
  File "<pyshell#93>", line 7, in <module>
    os.rename (item, x.group(0) + ".jpg")
FileExistsError: [WinError 183] Cannot create a file when that file already exists: '8711600821552 (3).jpg' -> '8711600821552.jpg'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#93>", line 10, in <module>
    os.rename (item, x.group(0) +"_1.jpg")
FileExistsError: [WinError 183] Cannot create a file when that file already exists: '8711600821552 (3).jpg' -> '8711600821552_1.jpg'
>>> rename = 1
>>> for item in os.listdir('.'):
	x = re.search("[0-9]{8,14}",item)
	if x:
		counter +=1
		print ("Item " + item + " matches pattern")
		try:
			os.rename (item, x.group(0) + ".jpg")
		except FileExistsError:
			print ("Could not rename " + item)
			os.rename (item, x.group(0) +"_"+ rename +".jpg")
			rename+=1

			
Item 5201028118950.jpg matches pattern
Item 5201028124104.jpg matches pattern
Item 5201028125514.jpg matches pattern
Item 5201028125514_1.jpg matches pattern
Could not rename 5201028125514_1.jpg
Traceback (most recent call last):
  File "<pyshell#97>", line 7, in <module>
    os.rename (item, x.group(0) + ".jpg")
FileExistsError: [WinError 183] Cannot create a file when that file already exists: '5201028125514_1.jpg' -> '5201028125514.jpg'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#97>", line 10, in <module>
    os.rename (item, x.group(0) +"_"+ rename +".jpg")
TypeError: can only concatenate str (not "int") to str
>>> rename = 1
>>> for item in os.listdir('.'):
	x = re.search("[0-9]{8,14}",item)
	if x:
		counter +=1
		print ("Item " + item + " matches pattern")
		try:
			os.rename (item, x.group(0) + ".jpg")
		except FileExistsError:
			print ("Could not rename " + item)
			os.rename (item, x.group(0) +"_"+ str(rename) +".jpg")
			rename+=1

			
Item 5201028118950.jpg matches pattern
Item 5201028124104.jpg matches pattern
Item 5201028125514.jpg matches pattern
Item 5201028125514_1.jpg matches pattern
Could not rename 5201028125514_1.jpg
Item 8710522371787.jpg matches pattern
Item 8710522404805.jpg matches pattern
Item 8710908436758.jpg matches pattern
Item 8711600601253.jpg matches pattern
Item 8711600821552 (3).jpg matches pattern
Could not rename 8711600821552 (3).jpg
Item 8711600821552 (4).jpg matches pattern
Could not rename 8711600821552 (4).jpg
Item 8711600821552.jpg matches pattern
Item 8711600821552_1.jpg matches pattern
Could not rename 8711600821552_1.jpg
Item 8711700809580.jpg matches pattern
Item 8711700968997 (8).jpg matches pattern
Item 8717163434062.png matches pattern
Item 8717644563045.(1).jpg matches pattern
Item 8717644563045.(2).jpg matches pattern
Could not rename 8717644563045.(2).jpg
Item 8717644563045.(3).jpg matches pattern
Could not rename 8717644563045.(3).jpg
Item 8717644563045.(4).jpg matches pattern
Could not rename 8717644563045.(4).jpg
Item 8718114143422.01.tif matches pattern
Item 8718114256474.tif matches pattern
Item 8718114586151.01 Classic Fresh Σκληρή.tif matches pattern
Item Aim TB Professional 99% Μαλακή 8718114586489 (2).jpg matches pattern
Item Aim TB Professional 99% Μαλακή 8718114586489 (3).jpg matches pattern
Could not rename Aim TB Professional 99% Μαλακή 8718114586489 (3).jpg
Item Aim TB Professional 99% Μαλακή 8718114586489 (4).jpg matches pattern
Could not rename Aim TB Professional 99% Μαλακή 8718114586489 (4).jpg
Item Aim TB Professional 99% Μαλακή 8718114586489.jpg matches pattern
Could not rename Aim TB Professional 99% Μαλακή 8718114586489.jpg
Item Aim TB Ultra Reach Μέτρια 8718114584782.JPG matches pattern
Item Aim TB Ultra Reach Μέτρια 8718114584782.tif matches pattern
Could not rename Aim TB Ultra Reach Μέτρια 8718114584782.tif
Item Aim TB Vertical Expert DF Μέτρια 8710908386084 (2).jpg matches pattern
Item Aim TB Vertical Expert DF Μέτρια 8710908386084 (7).jpg matches pattern
Could not rename Aim TB Vertical Expert DF Μέτρια 8710908386084 (7).jpg
Item Aim TB Vertical Expert DF Μέτρια 8710908386084 (8).jpg matches pattern
Could not rename Aim TB Vertical Expert DF Μέτρια 8710908386084 (8).jpg
Item Aim TB Vertical Expert DF Μέτρια 8710908386084.jpg matches pattern
Could not rename Aim TB Vertical Expert DF Μέτρια 8710908386084.jpg
Item Aim TB Vertical Expert DF Μαλακή 8710908426773 (2).jpg matches pattern
Item Aim TB Vertical Expert DF Μαλακή 8710908426773 (3).jpg matches pattern
Could not rename Aim TB Vertical Expert DF Μαλακή 8710908426773 (3).jpg
Item Aim TB Vertical Expert DF Μαλακή 8710908426773 (4).jpg matches pattern
Could not rename Aim TB Vertical Expert DF Μαλακή 8710908426773 (4).jpg
Item Aim TB Vertical Expert DF Μαλακή 8710908426773.jpg matches pattern
Could not rename Aim TB Vertical Expert DF Μαλακή 8710908426773.jpg
Item Aim TB Vertical Expert Μέτρια 8711700968997 (6).jpg matches pattern
Could not rename Aim TB Vertical Expert Μέτρια 8711700968997 (6).jpg
Item Aim TB Vertical Expert Μέτρια 8711700968997 (7).jpg matches pattern
Could not rename Aim TB Vertical Expert Μέτρια 8711700968997 (7).jpg
Item Aim TB Vertical Expert Μέτρια 8711700968997.jpg matches pattern
Could not rename Aim TB Vertical Expert Μέτρια 8711700968997.jpg
Item Aim TB Vertical Expert Μαλακή 8711700968904 (3).jpg matches pattern
Item Aim TB Vertical Expert Μαλακή 8711700968904 (4).jpg matches pattern
Could not rename Aim TB Vertical Expert Μαλακή 8711700968904 (4).jpg
Item Aim TB Vertical Expert Πολύ Μαλακή 8710908036255.JPG matches pattern
Item Aim TB White System Μέτρια 52015304 (2).jpg matches pattern
Item Aim TB White System Μέτρια 52015304 (3).jpg matches pattern
Could not rename Aim TB White System Μέτρια 52015304 (3).jpg
Item Aim TB White System Μέτρια 52015304.jpg matches pattern
Could not rename Aim TB White System Μέτρια 52015304.jpg
Item Aim TB White System Σκληρή 52015298 (2).jpg matches pattern
Item Aim TB White System Σκληρή 52015298 (3).jpg matches pattern
Could not rename Aim TB White System Σκληρή 52015298 (3).jpg
Item Aim TB White System Σκληρή 52015298.jpg matches pattern
Could not rename Aim TB White System Σκληρή 52015298.jpg
Item Aim TP Expert Protection Fresh Natural 75ml - 8710522371817.PNG matches pattern
Item Aim TP Expert Protection Smalto Defence 75ml - 8710522371831.PNG matches pattern
Item Aim οδοντόβουρτσα 2-6 ετών - 5201028125514 (1).jpg matches pattern
Could not rename Aim οδοντόβουρτσα 2-6 ετών - 5201028125514 (1).jpg
Item Aim οδοντόβουρτσα 2-6 ετών -5201028125514.(3).jpg matches pattern
Could not rename Aim οδοντόβουρτσα 2-6 ετών -5201028125514.(3).jpg
Item Αim TB Classic Fresh Μέτρια 8718114585215.JPG matches pattern
>>> os.getcwd()
'C:\\Users\\mpitsalidis\\Desktop\\Unilever Oral & Deos Αλλαγές November 2019\\Aim'
>>> aim_local = [item.name for item in os.scandir('.') if item.is_file()]
>>> print (aim_local)
['711007_1.jpg', '711564_1.jpg', '712555_b.jpg', '75ml.png', '762015_1.jpg', '762019_1.jpg', '762756_1.jpg', '762902_1.jpg', 'Aim TB Vertical Expert Μαλακή.jpeg', 'Aim TP Expert Pure White 75ml - front.tif', 'E11843_a.jpg', 'E11895_1.jpg', 'E12410_1.jpg', 'E12505_1.jpg', 'E12505_2.jpg', 'E12505_3.jpg', 'E12507_1.jpg', 'E12507_2.jpg', 'E12507_3.jpg', 'E12551_1.jpg', 'E12551_2.jpg', 'E12551_3.jpg', 'E12551_4.jpg', 'T060126_1.jpg', 'T080959_1.jpg', 'T082158_1.jpg', 'T082158_2.jpg', 'T082158_3.jpg', 'T082158_4.jpg', 'T096891_1.jpg', 'T096891_2.jpg', 'T096900_1.jpg', 'T096900_2.jpg', 'T096900_3.jpg', 'T096900_4.jpg', 'T343370_1.jpg', 'T414346_1.jpg', 'T425648_1.jpg', 'T456305_1.jpg', 'T456305_2.jpg', 'T456305_3.jpg', 'T456305_4.jpg', 'T458483_1.jpg', 'T458483_2.jpg', 'T458522_1.jpg', 'T458616_1.jpg', 'T458649_1.jpg', 'T458649_2.jpg', 'T458649_3.jpg', 'T458649_4.jpg', 'T838609_1.jpg', 'T838609_2.jpg', 'T838609_3.jpg', 'T838609_4.jpg', 'T842689_1.jpg', 'T842689_2.jpg', 'T842689_3.jpg', 'T842689_4.jpg', 'White System Enamel 75ml.tif']
>>> aim_lc = []
>>> for code in aim_local:
	for i in range(0, len(code)):
		if code[i]==".":
			aim_lc.append(code[:i])

			
>>> print (aim_lc)
['711007_1', '711564_1', '712555_b', '75ml', '762015_1', '762019_1', '762756_1', '762902_1', 'Aim TB Vertical Expert Μαλακή', 'Aim TP Expert Pure White 75ml - front', 'E11843_a', 'E11895_1', 'E12410_1', 'E12505_1', 'E12505_2', 'E12505_3', 'E12507_1', 'E12507_2', 'E12507_3', 'E12551_1', 'E12551_2', 'E12551_3', 'E12551_4', 'T060126_1', 'T080959_1', 'T082158_1', 'T082158_2', 'T082158_3', 'T082158_4', 'T096891_1', 'T096891_2', 'T096900_1', 'T096900_2', 'T096900_3', 'T096900_4', 'T343370_1', 'T414346_1', 'T425648_1', 'T456305_1', 'T456305_2', 'T456305_3', 'T456305_4', 'T458483_1', 'T458483_2', 'T458522_1', 'T458616_1', 'T458649_1', 'T458649_2', 'T458649_3', 'T458649_4', 'T838609_1', 'T838609_2', 'T838609_3', 'T838609_4', 'T842689_1', 'T842689_2', 'T842689_3', 'T842689_4', 'White System Enamel 75ml']
>>> aim_l =[]
>>> aim_local_final = []
>>> for code in aim_lc:
	for i in range(0, len(code)):
		if code[i]=="_":
			aim_local_final.append(code[:i])

			
>>> print (aim_local_final)
['711007', '711564', '712555', '762015', '762019', '762756', '762902', 'E11843', 'E11895', 'E12410', 'E12505', 'E12505', 'E12505', 'E12507', 'E12507', 'E12507', 'E12551', 'E12551', 'E12551', 'E12551', 'T060126', 'T080959', 'T082158', 'T082158', 'T082158', 'T082158', 'T096891', 'T096891', 'T096900', 'T096900', 'T096900', 'T096900', 'T343370', 'T414346', 'T425648', 'T456305', 'T456305', 'T456305', 'T456305', 'T458483', 'T458483', 'T458522', 'T458616', 'T458649', 'T458649', 'T458649', 'T458649', 'T838609', 'T838609', 'T838609', 'T838609', 'T842689', 'T842689', 'T842689', 'T842689']
>>> os.chdir('L:')
>>> aim_server = [item.name for item in os.scandir('.') if item.is_file()]
>>> print (len (aim_server))
90987
>>> aim_to_delete_from_server = []
>>> for aim in aim_local_final:
	for code in aim_server:
		if fnmatch.fnmatch(code, aim+"*"):
			print ("Code in server: " + code " matches " + aim " in local list")
			
SyntaxError: invalid syntax
>>> for aim in aim_local_final:
	for code in aim_server:
		if fnmatch.fnmatch(code, aim+"*"):
			print ("Code in server: " + code + " matches " + aim + " in local list")

			
Code in server: 711007.jpg matches 711007 in local list
Code in server: 711564.jpg matches 711564 in local list
Code in server: 712555_a.png matches 712555 in local list
Code in server: 762015.jpg matches 762015 in local list
Code in server: 762019.jpg matches 762019 in local list
Code in server: 762756.jpg matches 762756 in local list
Code in server: 762902_a.jpg matches 762902 in local list
Code in server: E11843.jpg matches E11843 in local list
Code in server: E11895-BUND.jpg matches E11895 in local list
Code in server: E11895.jpg matches E11895 in local list
Code in server: E12410.jpg matches E12410 in local list
Code in server: E12505-BUNDLE.jpg matches E12505 in local list
Code in server: E12505.jpg matches E12505 in local list
Code in server: E12505-BUNDLE.jpg matches E12505 in local list
Code in server: E12505.jpg matches E12505 in local list
Code in server: E12505-BUNDLE.jpg matches E12505 in local list
Code in server: E12505.jpg matches E12505 in local list
Code in server: E12507.jpg matches E12507 in local list
Code in server: E12507.jpg matches E12507 in local list
Code in server: E12507.jpg matches E12507 in local list
Code in server: E12551.jpg matches E12551 in local list
Code in server: E12551.jpg matches E12551 in local list
Code in server: E12551.jpg matches E12551 in local list
Code in server: E12551.jpg matches E12551 in local list
Code in server: T060126.jpg matches T060126 in local list
Code in server: T080959.jpg matches T080959 in local list
Code in server: T082158.jpg matches T082158 in local list
Code in server: T082158.jpg matches T082158 in local list
Code in server: T082158.jpg matches T082158 in local list
Code in server: T082158.jpg matches T082158 in local list
Code in server: T096891.jpg matches T096891 in local list
Code in server: T096891.jpg matches T096891 in local list
Code in server: T096900.jpg matches T096900 in local list
Code in server: T096900.jpg matches T096900 in local list
Code in server: T096900.jpg matches T096900 in local list
Code in server: T096900.jpg matches T096900 in local list
Code in server: T343370-BUNDLE.jpg matches T343370 in local list
Code in server: T343370.jpg matches T343370 in local list
Code in server: T414346.jpg matches T414346 in local list
Code in server: T425648.jpg matches T425648 in local list
Code in server: T456305_a.jpg matches T456305 in local list
Code in server: T456305_a.jpg matches T456305 in local list
Code in server: T456305_a.jpg matches T456305 in local list
Code in server: T456305_a.jpg matches T456305 in local list
Code in server: T458483-BUNDLE.jpg matches T458483 in local list
Code in server: T458483.jpg matches T458483 in local list
Code in server: T458483-BUNDLE.jpg matches T458483 in local list
Code in server: T458483.jpg matches T458483 in local list
Code in server: T458522-BUND.jpg matches T458522 in local list
Code in server: T458522.jpg matches T458522 in local list
Code in server: T458522_a.jpg matches T458522 in local list
Code in server: T458616.jpg matches T458616 in local list
Code in server: T458649.jpg matches T458649 in local list
Code in server: T458649.jpg matches T458649 in local list
Code in server: T458649.jpg matches T458649 in local list
Code in server: T458649.jpg matches T458649 in local list
Code in server: T838609.jpg matches T838609 in local list
Code in server: T838609.jpg matches T838609 in local list
Code in server: T838609.jpg matches T838609 in local list
Code in server: T838609.jpg matches T838609 in local list
Code in server: T842689.jpg matches T842689 in local list
Code in server: T842689.jpg matches T842689 in local list
Code in server: T842689.jpg matches T842689 in local list
Code in server: T842689.jpg matches T842689 in local list
>>>  for aim in aim_local_final:
	for code in aim_server:
		if fnmatch.fnmatch(code, aim+"*"):
			
SyntaxError: unexpected indent
>>> for aim in aim_local_final:
	for code in aim_server:
		if fnmatch.fnmatch(code, aim+"*"):
			aim_to_delete_from_server.append(code)

			
>>> print (aim_to_delete_from_server)
['711007.jpg', '711564.jpg', '712555_a.png', '762015.jpg', '762019.jpg', '762756.jpg', '762902_a.jpg', 'E11843.jpg', 'E11895-BUND.jpg', 'E11895.jpg', 'E12410.jpg', 'E12505-BUNDLE.jpg', 'E12505.jpg', 'E12505-BUNDLE.jpg', 'E12505.jpg', 'E12505-BUNDLE.jpg', 'E12505.jpg', 'E12507.jpg', 'E12507.jpg', 'E12507.jpg', 'E12551.jpg', 'E12551.jpg', 'E12551.jpg', 'E12551.jpg', 'T060126.jpg', 'T080959.jpg', 'T082158.jpg', 'T082158.jpg', 'T082158.jpg', 'T082158.jpg', 'T096891.jpg', 'T096891.jpg', 'T096900.jpg', 'T096900.jpg', 'T096900.jpg', 'T096900.jpg', 'T343370-BUNDLE.jpg', 'T343370.jpg', 'T414346.jpg', 'T425648.jpg', 'T456305_a.jpg', 'T456305_a.jpg', 'T456305_a.jpg', 'T456305_a.jpg', 'T458483-BUNDLE.jpg', 'T458483.jpg', 'T458483-BUNDLE.jpg', 'T458483.jpg', 'T458522-BUND.jpg', 'T458522.jpg', 'T458522_a.jpg', 'T458616.jpg', 'T458649.jpg', 'T458649.jpg', 'T458649.jpg', 'T458649.jpg', 'T838609.jpg', 'T838609.jpg', 'T838609.jpg', 'T838609.jpg', 'T842689.jpg', 'T842689.jpg', 'T842689.jpg', 'T842689.jpg']
>>> print ('T414346' in aim_to_delete_from_server)
False
>>> os.getcwd()
'L:\\'
>>> for element in aim_to_delete_from_server:
	if "BUNDLE" not in element:
		os.remove(element)
	else:
		print (element + " not removed from L")

		
E12505-BUNDLE.jpg not removed from L
E12505-BUNDLE.jpg not removed from L
Traceback (most recent call last):
  File "<pyshell#142>", line 3, in <module>
    os.remove(element)
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'E12505.jpg'
>>> for element in aim_to_delete_from_server:
	if "BUNDLE" not in element:
		try:
			os.remove(element)
			print (element + " REMOVED FROM L")
		except FileNotFoundError as e:
			print (e)
	else:
		print (element + " not removed from L")

		
[WinError 2] The system cannot find the file specified: '711007.jpg'
[WinError 2] The system cannot find the file specified: '711564.jpg'
[WinError 2] The system cannot find the file specified: '712555_a.png'
[WinError 2] The system cannot find the file specified: '762015.jpg'
[WinError 2] The system cannot find the file specified: '762019.jpg'
[WinError 2] The system cannot find the file specified: '762756.jpg'
[WinError 2] The system cannot find the file specified: '762902_a.jpg'
[WinError 2] The system cannot find the file specified: 'E11843.jpg'
[WinError 2] The system cannot find the file specified: 'E11895-BUND.jpg'
[WinError 2] The system cannot find the file specified: 'E11895.jpg'
[WinError 2] The system cannot find the file specified: 'E12410.jpg'
E12505-BUNDLE.jpg not removed from L
[WinError 2] The system cannot find the file specified: 'E12505.jpg'
E12505-BUNDLE.jpg not removed from L
[WinError 2] The system cannot find the file specified: 'E12505.jpg'
E12505-BUNDLE.jpg not removed from L
[WinError 2] The system cannot find the file specified: 'E12505.jpg'
E12507.jpg REMOVED FROM L
[WinError 2] The system cannot find the file specified: 'E12507.jpg'
[WinError 2] The system cannot find the file specified: 'E12507.jpg'
E12551.jpg REMOVED FROM L
[WinError 2] The system cannot find the file specified: 'E12551.jpg'
[WinError 2] The system cannot find the file specified: 'E12551.jpg'
[WinError 2] The system cannot find the file specified: 'E12551.jpg'
T060126.jpg REMOVED FROM L
T080959.jpg REMOVED FROM L
T082158.jpg REMOVED FROM L
[WinError 2] The system cannot find the file specified: 'T082158.jpg'
[WinError 2] The system cannot find the file specified: 'T082158.jpg'
[WinError 2] The system cannot find the file specified: 'T082158.jpg'
T096891.jpg REMOVED FROM L
[WinError 2] The system cannot find the file specified: 'T096891.jpg'
T096900.jpg REMOVED FROM L
[WinError 2] The system cannot find the file specified: 'T096900.jpg'
[WinError 2] The system cannot find the file specified: 'T096900.jpg'
[WinError 2] The system cannot find the file specified: 'T096900.jpg'
T343370-BUNDLE.jpg not removed from L
T343370.jpg REMOVED FROM L
T414346.jpg REMOVED FROM L
T425648.jpg REMOVED FROM L
T456305_a.jpg REMOVED FROM L
[WinError 2] The system cannot find the file specified: 'T456305_a.jpg'
[WinError 2] The system cannot find the file specified: 'T456305_a.jpg'
[WinError 2] The system cannot find the file specified: 'T456305_a.jpg'
T458483-BUNDLE.jpg not removed from L
T458483.jpg REMOVED FROM L
T458483-BUNDLE.jpg not removed from L
[WinError 2] The system cannot find the file specified: 'T458483.jpg'
T458522-BUND.jpg REMOVED FROM L
T458522.jpg REMOVED FROM L
T458522_a.jpg REMOVED FROM L
T458616.jpg REMOVED FROM L
T458649.jpg REMOVED FROM L
[WinError 2] The system cannot find the file specified: 'T458649.jpg'
[WinError 2] The system cannot find the file specified: 'T458649.jpg'
[WinError 2] The system cannot find the file specified: 'T458649.jpg'
T838609.jpg REMOVED FROM L
[WinError 2] The system cannot find the file specified: 'T838609.jpg'
[WinError 2] The system cannot find the file specified: 'T838609.jpg'
[WinError 2] The system cannot find the file specified: 'T838609.jpg'
T842689.jpg REMOVED FROM L
[WinError 2] The system cannot find the file specified: 'T842689.jpg'
[WinError 2] The system cannot find the file specified: 'T842689.jpg'
[WinError 2] The system cannot find the file specified: 'T842689.jpg'
>>> 
