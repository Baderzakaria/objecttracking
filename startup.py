import os
#os.system('pwd')
#os.system('source simpleobjecttracking/bin/activate')
os.chdir('/home/pi/objecttracking-main')
#os.system('cd /home/pi/objecttracking-main')
#os.system('pwd')
os.system('python3 object_tracker.py --prototxt deploy.prototxt --model res10_300x300_ssd_iter_140000.caffemodel')
