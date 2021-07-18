#!/bin/sh
#cd /home/pi/Desktop/objecttracking-main
pwd

#bash venv.sh
echo "source $/home/pi/Desktop/objecttracking-main/simpleobjecttracking/bin/activate"
python object_tracker.py --prototxt deploy.prototxt --model res10_300x300_ssd_iter_140000.caffemodel
cd