import os;
import fnmatch;

def return_list_of_image_files(s, middle, extension):
    #initiates empty list
    file_listing = []
    #initiate matching rule
    m = "*" + extension
    #if middle digits exists, then update matching rule
    if middle == None:
        print ("ok, no middle digits then")
    else:
        m = "*" + middle + "*" + extension
    with os.scandir(s) as entries:
        for entry in entries:
            #checks if file is indeed file and if it matches extension given
            if entry.is_file() and fnmatch.fnmatch(entry.name, m):
                file_listing.append(entry.name)

        return file_listing
spaces = 0

lst = return_list_of_image_files('images', '41', '.png')
print (lst)
