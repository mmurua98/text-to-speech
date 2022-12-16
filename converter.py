from gtts import gTTS
import os

def getText(text):

    language = "es-us"

    global audioName
    audioName = "test.mp3"

    speech = gTTS(text=text, lang=language, slow=False)
    speech.save(audioName)

def getAudioName():
    return audioName