from flask import Flask, redirect, render_template, request
from flask_cors import CORS, cross_origin
from whitenoise import WhiteNoise
import converter
import os
import shutil
from mutagen.mp3 import MP3

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@cross_origin()
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/converter", methods=['POST'])
def convertText():
    txtInput = request.form['text']
    converter.getText(txtInput)


    global pathDir, origin, target, audioDuration, audioFilePath
    audioName = converter.getAudioName()

    pathDir = os.getcwd()
    origin = pathDir + '\\' + audioName
    target = os.path.join(pathDir, 'static\\audio', audioName)

    #get audio length
    audioInfo = MP3(audioName)
    audioDuration = str((audioInfo.info.length) + 15)

    audioFilePath = f"static/audio/{audioName}"

    if os.path.exists(origin):
        shutil.move(origin, target)
    
    return redirect('/getaudio')
    #return render_template('index.html', pathAudio=audioFilePath), {"Refresh": ""+audioDuration+"; url=/"}

@app.route("/getaudio")
def getAudio():
    #print(audioFilePath)
    return render_template('audio.html', pathAudio=audioFilePath), {"Refresh": ""+audioDuration+"; url=/"}



if __name__ == "__main__":
    app.run()