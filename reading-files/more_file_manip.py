import os;
import shutil;
import fnmatch;

"""
Go through subdir in file structure, find files with {_letter} ending - files have name format {SKU_ending.extension}, and rename them

Renaming must RETAIN same file extension and replace only the {_letter} ending of the file name with a {_number} (this is what dictates image position in image carousel)

The current alphabetical order must remain the same in numeric format (sku_a & sku_b will be sku_1 and sku_2)

Any inbetween {_letter} patterns that are part of the Product SKU must remain unchanged
"""
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

def find_dir_and_rename():
    #get a DirEntry list with all sub-directories of root
    try:
        lst = [dirs for dirs in os.scandir('.') if dirs.is_dir()]
        #go to images directory
        os.chdir(lst[1].name)
        for item in os.scandir('.'):
            if item.is_file():
                os.rename(item.name, letter_to_number(item.name))
    except OSError as e:
        print ("Raised an OSError with message: ", e)
    except TypeError as t:
        print ("Raised TypError with message: ", t)

find_dir_and_rename()