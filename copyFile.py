#!/usr/bin/env python

import shutil, os

listFile = raw_input("The path of the txt List File is: ")
sourceFolder = raw_input("The path of the Source Folder is: ")
destinationFolder = raw_input("The path of the Destination Folder is: ")
f = open(listFile, "r")
line = f.readline()
while line:
	src = os.path.join(sourceFolder, line)[:-1]
	dst = destinationFolder+"/"+str(line)[:-1]
	if os.path.isfile(src):
		if os.path.isfile(dst):
			print(dst+" file already exists")
			line = f.readline()
			continue
		else:
			line = f.readline()
			shutil.copyfile(src, dst)
			print(dst+" file was copied")
	else:
		print(line[:-1]+" file doesn't exist in "+sourceFolder)
		line = f.readline()
f.close()


