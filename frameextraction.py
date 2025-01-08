if __name__ == "__main__":
  print("Dawg this isn't main.py wtf are you doing")

import cv2
import os

def extract(videofile, folder):
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
  while success:
    cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1