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
	if os.path.isdir(src):
		if os.path.isdir(dst):
			print(dst+" folder already exists")
			line = f.readline()
			continue
		else:
			line = f.readline()
			shutil.copytree(src, dst, symlinks=False, ignore=None)
			print(dst+" folder was copied")
	else:
		print(line[:-1]+" folder doesn't exist in "+sourceFolder)
		line = f.readline()
f.close()


