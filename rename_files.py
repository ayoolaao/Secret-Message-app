import os
def rename_files():

    #1. get file names from dir

    file_list = os.listdir("/Users/ayoolaao/Desktop/udacity/Full Stack Web Developer Nanodegree/Intro to python/Secret Message app/prank")
    print(file_list)

    saved_path = os.getcwd()
    print("current dir:" + saved_path)
    os.chdir("/Users/ayoolaao/Desktop/udacity/Full Stack Web Developer Nanodegree/Intro to python/Secret Message app/prank")
    
    #2. for each file, rename filename

    for file_name in file_list:
        print ("Old name - " + file_name)
        print ("New name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()
