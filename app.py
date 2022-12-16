from flask import Flask, render_template, request, send_file
import converter
import os
import shutil

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
    global pathDir, origin, target
    audioName = converter.getAudioName()
    #origin = "/textspeech/"+audioName
    pathDir = os.getcwd()
    origin = pathDir + '\\' + audioName
    target = os.path.join(pathDir, 'static\\audio', audioName)

    # print(origin)
    # print(target)

    if os.path.exists(origin):
        shutil.move(origin, target)
    
    return render_template('index.html')


@app.after_request
def deleteVideo(response):
    if request.endpoint=="converter":
        if os.path.exists(target):
            try:
                #print(target)
                os.remove(target)
            except OSError as e: # name the Exception `e`
                print ("Failed with:", e.strerror)# look what it says
                print ("Error code:", e.errno )
    return response

# @app.route("/getaudio", methods=['POST', 'GET'])
# def showAudio():
#     #pathDir = os.getcwd()
#     # audioName = converter.getAudioName()
#     # pathFile = pathDir + '\\' + audioName

#     return render_template('index.html')


if __name__ == "__main__":
    app.run()