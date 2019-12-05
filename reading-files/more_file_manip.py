import os;
import shutil;
import fnmatch;

os.getcwd()

# for (root, directories, files) in os.walk('.'):
#     if fnmatch.fnmatch(root, './image*'):
#         print ("The folder" + root + " contains images \t")
#         os.chdir(root)
#         for (root, directories, files) in os.walk('.'):
#             if fnmatch.fnmatch(root, './images*'):
#                 print ("The folder" + root + " contains images; \t")
#                 os.chdir(root)
#                 for f in files:
#                     if fnmatch.fnmatch(f, "polaroid*"):
#                         os.rename(f, "polaroid_neurt")
#         print (os.getcwd())
#     print ("-"*8)

for (root, directories, files) in os.walk('.'):
    print ("The root directory is " + root)
    print ("\t The directories are: ")
    c=1
    for directory in directories:
        print ("\t" * c + directory)
    print ("\t The corresponding files are: ")
    d=1
    for fi in (files):
        print ("\t" * d + fi)
        d+=1
    d += 1
    c += 1