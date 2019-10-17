#!/bin/bash

aws s3 sync s3://txp-photolab /home/alex/YellowSub/raw

#ls -f /home/alex/YellowSub/raw | while read -r file; do cut -f1 -d"_" $file; done
cd /home/alex/YellowSub/raw
#ls -p | grep -v / | cut -f1 -d"_"
file_name=$(ls -p | grep -v / | cut -f1 -d"_")
echo $file_name

exit
