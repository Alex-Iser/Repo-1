#!/usr/bin/python3
import subprocess, os
import linecache

sourceFolder = input("The path of the Source Folder is: ")
f = open(sourceFolder+"/Timestamps.txt","w+")

for filename in os.listdir(sourceFolder):
    if filename.endswith(".mkv"):
        print(filename)
        subprocess.call(["mkvextract "+sourceFolder+"/"+filename+" timestamps_v2 0:1.txt"], shell=True)
        line = linecache.getline("1.txt", 2)[:-4]
        print(line)
        if line!="":
            print('there is a line')
            if line[0]!="-": 
                print('good line')
                timestamp = subprocess.check_output(["date --utc --date=@"+line+" +'%d/%m/%Y %H:%M:%S.%3N'"], shell=True).decode()
                print(timestamp)
                f = open(sourceFolder+"/Timestamps.txt","a")
                f.write(filename+"       "+timestamp+"\r")
                f.close()
                linecache.clearcache()
            else:
                print('bad line')
                f = open(sourceFolder+"/Timestamps.txt","a")
                f.write(filename+"         ERROR"+"\r")
                f.close()
                linecache.clearcache()

        else:
            print('empty line in file: ', filename)
    else:
        continue