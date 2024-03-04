import cv2
import numpy as np

# Initialize a Videocapture object to read the RTMP stream

cap = cv2.VideoCapture('rtmp://13.233.245.152/live/test')

while true:
  # capture frame by frame 
  ret, frame = cap.read()

if ret:
  # display the resulting frame
  cv2.imshow('frame', frame)

# press 'q' to close the window

if cv2.waitkey(1) & 0xFF == ord('q'):
  break
else:
  print("Failed to grab frame")
  brek

# when everything is done, release the capture

cap.release()
