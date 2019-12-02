import os;
import fnmatch;

def return_list_of_image_files(s, middle, extension):
    #initiate empty list
    file_listing = []
    #initiate matching rule
    m = "*." + extension
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

def rename_file (current_name, added_part):
    
    new_name = ""
    for i in range(0, len(current_name)):
        if current_name[i] == ".":
            new_name += added_part + "."
        else:
            new_name += current_name[i]
    try:
        os.rename(current_name, new_name)
    except FileNotFoundError:
        print ("There is no file with that name.")
        
lst = return_list_of_image_files('images', None, "png")

rename_file("images/3.png", "-1")



