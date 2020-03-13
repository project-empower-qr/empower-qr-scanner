'''
OS: Raspbian
Date: 12/02/2020
Language: Python 3.7.0
Author: Marcel Kowalczyk

Overview:
Scanning frame by frame for qr code
Once qr code in frame then it will be read

To be tested and adjusted with camera module
'''`
#importing packages needed
import cv2 as cv
from picamera import PiCamera as picam 
from picamera.array import PiRGPArray as pirgb
import time
from pyzbar import pyzbar
import argparse
import imutils
import datetime

#reading qr codes
def readQr(image)
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        #getting bounding box loc for barcode
        (x, y, w, h) = barcode.rect
        #drawing bounding box
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        #converting qr code data for displaying purposesd (byte -> String)
        data = barcode.data.decode("utf-8")
        dataType = barcode.type

        #overlying barcode data and type on image
        overlayInfo = "{} ({})".format(data, dataType)
        cv.putText(image, overlayInfo, (x, y - 10),
                cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        #When barcode ! in CSV file = write qr code + timestamp to csv
        if data not in found:
            csv.write("{},{}\n".format(datetime.datetime.now(),data))
            csv.flush()
            found.add(data)

#constructing a parser
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type = str, default="barcodes.csv",
        help = "Path to output CSV file containing barcodes")
args = vars(ap.parse_args())

#opening csv output ####will need to be changed to DB
csv = open(args["output"], "w")
found = set()

#initializing camera
camera = picam()
camera.resolution = (640,480) #to be adjusted to the highest res
camera.framerate = 32 #to be adjusted to the highes framerate
rawCApture = pirgb(camera, size=(640, 480))

#################################################################
#possible idea to take in black & white images using thresholding
#################################################################twitch

#camera startup needed to initialize
time.sleep(0.1)

#capturing frames from the video
for frame in camera.capture_continous(rawCapture, format = "bgr", use_video_port = True):

    #grabbing the frame
    image = frame.array

    cv.imshow("Frame", image)#showing image if needed
    key = cv.waitKey(1) & 0xFF

    rawCapture.truncate(0)#clear stream in preperation for next frame

    if key == ord("q"):
        break

csv.close()
cv.destroyAllWindows()
