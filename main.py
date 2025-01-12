from openai import OpenAI
from RealtimeSTT import AudioToTextRecorder
import os
import sys
import frameextraction
import cv2
import time
from threading import Thread

"""
openaiKeyFile = open("openai.key", "r") # open API key file.
openaiAPIKey = openaiKeyFile.read()
openaiKeyFile.close()

AIclient = OpenAI(
  api_key = openaiAPIKey
)
"""

# Text drawing shit
font = cv2.FONT_HERSHEY_SIMPLEX
textScale = 1
textThickness = 2
borderThickness = 5
textColor = (255, 255, 255) # BGR
borderColor = (0, 0, 0)

# Frame drawing shit
framerate = 30
lastFrameDrawn = time.time()
videoWidth = 404

transcribedThisCycle = []
displayedText = ""

def process_text(text):
  pass

def realtimeTranscribe(text):
  global transcribedThisCycle
  global displayedText

  os.system("cls")

  splittext = text.split(" ")

  if len(transcribedThisCycle) > 1 and len(splittext) > len(transcribedThisCycle):
    displayedText = " ".join(splittext[len(transcribedThisCycle) + 1:])
    print(len(transcribedThisCycle), len(splittext))
  else:
    displayedText = text

  transcribedThisCycle = text.split(" ")

def micListenLoop():
  while True:
    recorder.text(process_text)

def frameLoop():
  global framerate
  global lastFrameDrawn
  global transcribedThisCycle
  global font
  global displayedText

  while True:
    frame = frameextraction.getNextFrame()
    
    textSize = cv2.getTextSize(displayedText, font, 1, 2)[0]
    textX = (frame.shape[1] - textSize[0]) // 2
    textY = (frame.shape[0] + textSize[1]) // 2

    cv2.putText(frame, displayedText, (textX, textY), font, textScale, borderColor, textThickness + borderThickness)
    cv2.putText(frame, displayedText, (textX, textY), font, textScale, textColor, textThickness)
    
    cv2.imshow("Brainrot", frame)
    if cv2.waitKey(1) & 0xFF == ord("`"):
        break
        exit(0)
    time.sleep(1/framerate)

if __name__ == "__main__": # put everything in here to prevent any shit from happening because the STT library uses multiprocessing
  # Extract all frames from video
  args = sys.argv[1:] # get args
  videofile = "videos/parkour.mp4"
  outputFolder = "frames"
  framelimit = 1000

  if len(args) >= 3:  # set vars if args were inputted
    videofile = args[0]
    outputFolder = args[1]
    framelimit = args[1]

  textSoFar = ""
  
  frameextraction.setVideo(videofile)
  #frameextraction.extract(videofile, outputFolder, framelimit) # extract
  
  print("Initializing mic")
  recorder = AudioToTextRecorder(model="tiny.en", realtime_model_type='tiny.en', 
                                 enable_realtime_transcription=True, realtime_processing_pause=0.02,
                                 on_realtime_transcription_update=realtimeTranscribe)
                                 #on_realtime_transcription_stabilized=realtimeTranscribe)
  
  micThread = Thread(target=micListenLoop)
  frameThread = Thread(target=frameLoop)
  #recorder.text(process_text)
  micThread.start()
  frameThread.start()
  