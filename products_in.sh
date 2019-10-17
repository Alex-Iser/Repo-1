#!/bin/bash

#the folder that recieves the videos
read -p "Enter path of folder " path


#a 50 product loop that keeps the script running
for (( j=0; j<50; j++ ))
do

	if [ "$#" -gt 1 ]; then
		echo "this script exepects a maximum of 1 optional parameter - <path_to_save_video>"
		echo "exiting"
		exit 1
	fi


	#read the barcode with scanner
	read -p "enter barcode " barcode
	

    

	#each barcode has its own folder in the path folder
	mkdir $path/$barcode
	#echo $path/$barcode

	
	video_location=$path/$barcode
	#echo $path/$barcode


	if [ "$#" -ne 1 ]; then
		echo "this script accepts 1 optional parameter - <path_to_save_video> --> by default the videos are saved to current directory"
	else
		#video_location=$1
		video_location=$path/$barcode
	fi

	ip_list=(192.168.1.162 192.168.1.152 192.168.1.167 192.168.1.199 192.168.1.150 192.168.1.151)

	num_devices=${#ip_list[@]}

	for (( i=0; i<$num_devices; i++ ))
	do
		sshpass -p "dw" ssh pi@${ip_list[$i]} /home/pi/AIC_EdgeClient/scripts/./raspivid_to_gstreamer_sports.sh ${ip_list[$i]} > local_log_${ip_list[$i]}.txt 2>&1 &
	done

	sleep 3

	echo "finished running video streamers remotely - opening streams to listen locally"

	for (( i=0; i<$num_devices; i++ ))
	do
		./capture_tcp_video_tofile.sh ${ip_list[$i]} $video_location > remote_log_${ip_list[$i]}.txt 2>&1 &
		echo i
	done

	echo "---Ready----"
	sleep 0.5
	echo "---Steady---"
	sleep 0.5
	echo "-----Go-----"
	

done
	

