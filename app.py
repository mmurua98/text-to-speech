from flask import Flask, render_template, request
import converter
import os
import shutil
from mutagen.mp3 import MP3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/converter", methods=['POST'])
def convertText():
    txtInput = request.form['text']
    converter.getText(txtInput)

    # pathDir = os.getcwd()
    # audioName = converter.getAudioName()
    # pathFile = pathDir + '\\' + audioName
    # print(pathFile)
    global pathDir, origin, target, audioDuration
    audioName = converter.getAudioName()
    #origin = "/textspeech/"+audioName
    pathDir = os.getcwd()
    origin = pathDir + '\\' + audioName
    target = os.path.join(pathDir, 'static\\audio', audioName)

    #get audio length
    audioInfo = MP3(audioName)
    audioDuration = str((audioInfo.info.length) + 15)
    #print (audioDuration)
    # print(origin)
    # print(target)

    if os.path.exists(origin):
        shutil.move(origin, target)
    
    #return render_template('index.html')
    return render_template('index.html', pathAudio=target), {"Refresh": ""+audioDuration+"; url=/"}


# @app.after_request
# def refreshSite(response):
#     if request.endpoint=="converter":
#         return redirect(url_for('home')), {"Refresh": ""+audioDuration+"; url=/"}
#         # if os.path.exists(target):
#         #     try:
#         #         #print(target)
#         #         os.remove(target)
#         #     except OSError as e: # name the Exception `e`
#         #         print ("Failed with:", e.strerror)# look what it says
#         #         print ("Error code:", e.errno )
#     return response

# @app.route("/getaudio", methods=['POST', 'GET'])
# def showAudio():
#     #pathDir = os.getcwd()
#     # audioName = converter.getAudioName()
#     # pathFile = pathDir + '\\' + audioName

#     return render_template('index.html')


if __name__ == "__main__":
    app.run()