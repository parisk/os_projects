import os;
import shutil;
import fnmatch;

os.getcwd()

for (root, directories, files) in os.walk('.'):
    if fnmatch.fnmatch(root, './image*'):
        print ("The folder" + root + " contains images; \t")
        for f in files:
            print (f)
        print ("-"*8)