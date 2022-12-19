from gtts import gTTS
import os
import random

def getText(text):

    language = "es-us"

    global audioName
    num1 = str(random.randint(0,100))
    num2 = str(random.randint(0,100))
    audioName = num1+"test"+num2+".mp3"

    speech = gTTS(text=text, lang=language, slow=False)
    speech.save(audioName)

def getAudioName():
    return audioName