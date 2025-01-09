if __name__ == "__main__":
  print("Dawg this isn't main.py wtf are you doing")
  exit(0)

import cv2
import sys
import os

videoCapture = None
count = 0

def setVideo(videofile):
  global videoCapture
  videoCapture = cv2.VideoCapture(videofile) 

def getNextFrame():
  global videoCapture
  global count
  success,image = videoCapture.read()
  count += 1

def extract(videofile, folder, framelimit = -1, vidWidth = 640, vidHeight = 360):
  #make sure string isnt empty so things dont go to shit
  if(folder == ""):
    print("please input valid path please please")
    return

  # Fail if folder doesn't exist
  if not os.path.isdir(folder):
    print(f"Path \"{folder}\" doesn't exist")
    return
    
  vidcap = cv2.VideoCapture(videofile)
  success,image = vidcap.read()
  count = 0
  totalsize = sys.getsizeof(image)

  # image is orignally 640x360
  # To get the width of the image if we crop it to 9:16 vertical
  # We cross multiply 9/16 = x/360
  newWidth = int(9*vidHeight) >> 4
  middle = int(vidWidth) >> 1

  while success:
    cv2.imwrite(folder + "/frame%d.jpg" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    image = image[0:vidHeight, (middle - (newWidth >> 1)):(middle + (newWidth >> 1)) ]
    print('Read a new frame: ' + str(success) + " " + str(count) + " size in memory (bytes): " + str(sys.getsizeof(image)))
    count += 1
    totalsize += sys.getsizeof(image)

    if(count >= framelimit):
      break
  
  print(f"Total size in memory if you load the entire thing at once: {totalsize} bytes ({totalsize / 1024} MB)")