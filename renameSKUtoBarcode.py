#!/usr/bin/env python3

import shutil, os

listFileFrom = "/home/alex/Documents/listFileFrom.txt" # a file containing the original names of the folders (SKUs)
listFileTo = "/home/alex/Documents/listFileTo.txt" # a file containing the desirable folder names (barcodes)
sourceFolder = "/home/alex/sku_purchased/" # the folder where we have the SKUs 

f = open(listFileFrom, "r")
d = open(listFileTo, "r")
lineFrom = f.readline()
lineTo = d.readline()

dirLength = len(next(os.walk("/home/alex/sku_purchased"))[1]) # counts how many folders are to be changed 
for x in range(dirLength):
    print("from: "+lineFrom[:-1]+"  to: "+lineTo[:-1])
    shutil.move(sourceFolder+lineFrom[:-1],sourceFolder+lineTo[:-1])
    lineFrom = f.readline()
    lineTo = d.readline()
f.close()
