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

# for (root, directories, files) in os.walk('.'):
#     print ("The root directory is " + root)
#     print ("\t The directories are: ")
#     c=1
#     for directory in directories:
#         print ("\t" * c + directory)
#     print ("\t The corresponding files are: ")
#     d=2
#     for fi in (files):
#         print ("\t" * d + fi)
#         d+=1
        
dicti = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26
}

def letter_to_number(filename):
    st = ""
    for i in range(0, len(filename)):
        #checks if filename digit is letter
        if filename[i] in dicti.keys():
            st += str(dicti[filename[i]])
        elif filename[i] == "_":
        #checks if filename digit is _
            st += "_"
        elif filename[i]=='.':
        #checks if we have reached the extension part of the filename
            a = len(filename) - i
            st += filename[-a:]
            break
        else:
        #checks if filename digit is number
            st += filename[i]
    return st

def return_last_image_number(path):
    os.chdir(path)
    for item in os.listdir('.'):
        print (item)
        
return_last_image_number("/images")