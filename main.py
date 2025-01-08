from openai import OpenAI
from RealtimeSTT import AudioToTextRecorder
import os

"""
openaiKeyFile = open("openai.key", "r") # open API key file.
openaiAPIKey = openaiKeyFile.read()
openaiKeyFile.close()

AIclient = OpenAI(
  api_key = openaiAPIKey
)
"""

textSoFar = ""

def process_text(text):
  print(text)

def realtimeTranscribe(text):
  global textSoFar
  os.system("cls")
  textSoFar += text
  print(text)

if __name__ == "__main__":
  print("Initializing")
  recorder = AudioToTextRecorder(model="tiny.en", realtime_model_type='tiny.en', 
                                 enable_realtime_transcription=True, realtime_processing_pause=0.02,
                                 on_realtime_transcription_update=realtimeTranscribe)

  while True:
    recorder.text(process_text)