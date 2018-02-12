
"""
Created on Sat Feb  3 17:29:54 2018

@author: Abhilash Srivastava
"""


import cv2
import time
import datetime
import numpy as np
import math

def import_video(video):
    cap=cv2.VideoCapture(video)

    while(True):
        ret,frame=cap.read()
        image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',image)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# place a prompt on the displayed image
def prompt_on_image(txt):
    global gray
    cv2.putText(image, txt, (10, 35),
    cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
     
# calculate speed from pixels and time
def get_speed(pixels, ftperpixel, secs):
    if secs > 0.0:
        return ((pixels * ftperpixel)/ secs) * 0.681818  
    else:
        return 0.0
 
# calculate elapsed seconds
def secs_diff(endTime, begTime):
    diff = (endTime - begTime).total_seconds()
    return diff
# record speed in .csv format
def record_speed(res):
    global csvfileout
    f = open(csvfileout, 'a')
    f.write(res+"\n")
    f.close
# mouse callback function for drawing capture area
def draw_rectangle(event,x,y,flags,param):
    global ix,iy,fx,fy,drawing,setup_complete,image, org_image, prompt
 
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
 
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            image = org_image.copy()
            prompt_on_image(prompt)
            cv2.rectangle(image,(ix,iy),(x,y),(0,255,0),2)
  
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        fx,fy = x,y
        image = org_image.copy()
        prompt_on_image(prompt)
        cv2.rectangle(image,(ix,iy),(fx,fy),(0,255,0),2)
# define some constants
DISTANCE = 76  #<---- enter your distance-to-road value here
MIN_SPEED = 0  #<---- enter the minimum speed for saving images
SAVE_CSV = False  #<---- record the results in .csv format in carspeed_(date).csv
 
THRESHOLD = 15
MIN_AREA = 175
BLURSIZE = (15,15)
IMAGEWIDTH = 640
IMAGEHEIGHT = 480
RESOLUTION = [IMAGEWIDTH,IMAGEHEIGHT]
FOV = 53.5    #<---- Field of view
FPS = 30
SHOW_BOUNDS = True
SHOW_IMAGE = True
# the following enumerated values are used to make the program more readable
WAITING = 0
TRACKING = 1
SAVING = 2
UNKNOWN = 0
LEFT_TO_RIGHT = 1
RIGHT_TO_LEFT = 2
# calculate the the width of the image at the distance specified
frame_width_ft = 2*(math.tan(math.radians(FOV*0.5))*DISTANCE)
ftperpixel = frame_width_ft / float(IMAGEWIDTH)
print("Image width in feet {} at {} from camera".format("%.0f" % frame_width_ft,"%.0f" % DISTANCE))

if __name__== '__main__':
    video='video1.avi'
    import_video(video)
