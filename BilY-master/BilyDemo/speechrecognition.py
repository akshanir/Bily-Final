from cgitb import text
from unittest import TextTestResult
import speech_recognition
import pyttsx3
from pydub import AudioSegment
from pydub.silence import split_on_silence
from neuralsamples import to_english
# install: pip install --upgrade arabic-reshaper
import arabic_reshaper

# install: pip install python-bidi
from bidi.algorithm import get_display
# f = open("SpeechDemo.txt", "a")
def arabic_print(text)->None:
  reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
  bidi_text = get_display(reshaped_text)           # correct its direction
  print(bidi_text)

recoginzer = speech_recognition.Recognizer()

while True:
  
  try:
    with speech_recognition.Microphone() as mic:
      recoginzer.adjust_for_ambient_noise(mic, duration=0.2)
      audio = recoginzer.listen(mic)
      # print(type(audio))
      # print(audio)
      textAr = recoginzer.recognize_google(audio, language='ar-JO')
      # textAr = textAr.lower()
      # print(f"Recognized {textAr}")
      a = textAr.split()
      y = []
      for i in range(len(a)):
        u = to_english.get(a[i], "NotFound")
        y.append(u if u != "NotFound" else a[i])
    
      arabic_print(''.join([x+' ' for x in y]))
      # textEn = recoginzer.recognize_google(audio)
      # textEn = textEn.lower()
      # print(f"Recognized {textEn}")
      # print('')
      # printBest(textAr, textEn)
      # words = split_on_silence(audio, 
      #     # must be silent for at least half a second
      #     min_silence_len=50,

      #     # consider it silent if quieter than -16 dBFS
      #     silence_thresh=-40
      # )
      # print(len(words))
      # for word in words:
      #   text = recoginzer.recognize_google(word, language='ar-JO')
      #   text = text.lower()
      #   print(f"Recognized {text}")
      #   text = recoginzer.recognize_google(word)
      #   text = text.lower()
      #   print(f"Recognized {text}")

  except:
    continue
  # except speech_recognition.UnknownValueError():
  #   recoginzer = speech_recognition.Recognizer()
  #   continue