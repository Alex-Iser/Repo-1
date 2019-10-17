#!/usr/bin/python3

import subprocess, os, shutil, sys, glob

src = "/mnt/nfs/full_products_data"
dst = "/mnt/nfs/AI_RESEARCH/full_products_data_too_large"
limit = 710
listFile = "/mnt/nfs/Alex/fpd1400.txt"


for barcode in os.listdir(src):
    
    
#barcode = ([name for name in os.listdir(src)
            #if os.path.isdir(os.path.join(src, name)) and name.endswith("0") or name.endswith("1")]) # get all directories
    for folder in os.listdir(src+"/"+barcode):
        if not folder.endswith(".json")  and not folder.endswith(".png") and not folder.endswith(".DS_Store") and not folder.endswith(".py"):
            
            if folder.endswith("m0") or folder.endswith("m1") or folder.endswith("m2") or folder.endswith("m3"):
                contents = os.listdir(os.path.join(src+"/"+barcode,folder)) # get list of contents
                if len(contents) > limit: # if greater than the limit, print folder and number of contents
                    print(len(contents))
                    print (barcode+"  ", folder+"   ",len(contents))
                    if not os.path.isdir(dst+"/"+barcode+"/"+folder):
                        os.makedirs(dst+"/"+barcode+"/"+folder)
                        print (dst+"/"+barcode+"/"+folder+"  was created")
                        sourceFolder = src+"/"+barcode+"/"+folder
                        destinationFolder = dst+"/"+barcode+"/"+folder
                        f = open(listFile, "r")
                        line = f.readline()
                        while line:
                            cur_src = os.path.join(sourceFolder, line)[:-1]
                            cur_dst = destinationFolder+"/"+str(line)[:-1]
                            if os.path.isfile(cur_src):
                                if os.path.isfile(cur_dst):
                                    print(cur_dst+" file already exists")
                                    line = f.readline()
                                    continue
                                else:
                                    line = f.readline()
                                    shutil.copyfile(cur_src, cur_dst)
                                    print(cur_dst+" file was copied")
                            else:
                                print(line[:-1]+" file doesn't exist in "+sourceFolder)
                                line = f.readline()
                        f.close()
                        contents = os.listdir
                    else:
                        print(dst+"/"+barcode+"/"+folder+"  already exist")
                        break
                    
                        
                    
