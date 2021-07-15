#! /usr/bin/env python
# https://www.pyimagesearch.com/2018/07/23/simple-object-tracking-with-opencv/

# USAGE
# python object_tracker.py --prototxt deploy.prototxt --model res10_300x300_ssd_iter_140000.caffemodel

# import the necessary packages
#from pyimagesearch.centroidtracker import CentroidTracker
from centroidtracker import CentroidTracker # AZ
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
import csv
import threading
import datetime
import time


from check_id import check_id
from compare2csv import compare2csv
import urllib.request
id = check_id()
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# initialize our centroid tracker and frame dimensions
ct = CentroidTracker()
(H, W) = (None, None)

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# initialize the video stream and allow the camera sensor to warmup
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
ids= {}
today = datetime.date.today()

# loop over the frames from the video stream
while True:
	# read the next frame from the video stream and resize it
	frame = vs.read()
	frame = imutils.resize(frame, width=400)
	
	seconds_since_midnight = time.time() - time.mktime(today.timetuple())	
	if W is None or H is None:
		(H, W) = frame.shape[:2]

	# construct a blob from the frame, pass it through the network,
	# obtain our output predictions, and initialize the list of
	# bounding box rectangles
	blob = cv2.dnn.blobFromImage(frame, 1.0, (W, H),
		(104.0, 177.0, 123.0))
	net.setInput(blob)
	detections = net.forward()
	rects = []

	# loop over the detections
	for i in range(0, detections.shape[2]):
		# filter out weak detections by ensuring the predicted
		# probability is greater than a minimum threshold
		if detections[0, 0, i, 2] > args["confidence"]:
			# compute the (x, y)-coordinates of the bounding box for
			# the object, then update the bounding box rectangles list
			box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
			rects.append(box.astype("int"))
			t= time.time()
			# draw a bounding box surrounding the object so we can
			# visualize it
			(startX, startY, endX, endY) = box.astype("int")
			cv2.rectangle(frame, (startX, startY), (endX, endY),
				(0, 255, 0), 1)

	# update our centroid tracker using the computed set of bounding
	# box rectangles
	objects = ct.update(rects)
	# loop over the tracked objects
	for (objectID, centroid) in objects.items():
		# draw both the ID of the object and the centroid of the
		# object on the output frame
		text = "ID {}".format(objectID)
		cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
		cv2.circle(frame, (centroid[0], centroid[1]), 2, (0, 255, 0), -1)
		if objectID in ids:
			ids[objectID][1]=t
		else :
			ids[objectID]=[t,t]

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if seconds_since_midnight > 86400:
	# if the frame dimensions are None, grab them :
		with open('dict.csv', 'w') as csv_file:  
			writer = csv.writer(csv_file)
			for key, value in ids.items():
				value1 = value[0]
				value2 = value[1]
				writer.writerow([key, value1,value2])
		compare2csv(id)
		break
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		with open('dict.csv', 'w') as csv_file:  
			writer = csv.writer(csv_file)
			for key, value in ids.items():
				value1 = value[0]
				value2 = value[1]
				writer.writerow([key, value1,value2])
		compare2csv(id)
		break
cv2.destroyAllWindows()
vs.stop()