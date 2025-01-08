from openai import OpenAI
from RealtimeSTT import AudioToTextRecorder
import os
import sys
import frameextraction
import cv2

"""
openaiKeyFile = open("openai.key", "r") # open API key file.
openaiAPIKey = openaiKeyFile.read()
openaiKeyFile.close()

AIclient = OpenAI(
  api_key = openaiAPIKey
)
"""

def process_text(text):
  print(text)

def realtimeTranscribe(text):
  global textSoFar
  os.system("cls")
  textSoFar += text
  print(text)

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
  
  frameextraction.extract(videofile, outputFolder, framelimit) # extract
  
  print("Initializing mic")
  recorder = AudioToTextRecorder(model="tiny.en", realtime_model_type='tiny.en', 
                                 enable_realtime_transcription=True, realtime_processing_pause=0.02,
                                 #on_realtime_transcription_update=realtimeTranscribe)
                                 on_realtime_transcription_stabilized=realtimeTranscribe)

  while True:
    recorder.text(process_text)