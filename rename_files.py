import os
def rename_files():
    #1. get file names from dir
    file_list = os.listdir("/Users/ayoolaao/Desktop/udacity/Full Stack Web Developer Nanodegree/Intro to python/Secret Message app/prank")
    print(file_list)
    
    #2. for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()
