from flask import Flask, render_template, request,send_file
from werkzeug.utils import secure_filename
# from win32api import ShellExecute
import os
import sys
import logging
import subprocess

appPath=os.path.abspath('.')
app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
app.config['UPLOAD_FOLDER']="collection/"
 
@app.route("/")
def root():
    # index.html
    return render_template('index.html')

@app.route("/processEnd")
def proEnd():
    return render_template('processEnd.html')


@app.route("/startProcess",methods=['post'])
def process():
    a00=request.form.get("fileID")
    # 目前这个文件名不支持中文，以后做修改。
    f=request.files['audioFile']
    inFileName=a00+"_"+f.filename[f.filename.index('.'):]
    outFileName=inFileName+"_output"+inFileName[inFileName.index('.'):]
    args=' -i "'+appPath+"\\collection\\"+inFileName+'" -o "'+appPath+"\\collection\\"+outFileName+'" --overwrite'
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], inFileName))
    
    a01=request.form.get("outputHz")
    a02=request.form.get("outputBitRate")
    args=args+" --output-option "+a01+" "+a02
    if request.form.get("filter")!=None:
        args=args+" --filter"
        
    if request.form.get("q-reverb")=="default":
        args=args+" --reverb-default"
    elif request.form.get("q-reverb")=="setting":
        a03=request.form.get("reverbPcs")
        a04=request.form.get("reverbMaxVolumeDb")
        a05=request.form.get("reverbOffsetSecond")
        a06=request.form.get("reverbSoundFieldVol")
        args=args+" --reverb "+a03+" "+a04+" "+a05+" "+a06
        
    if request.form.get("q-pitch")=="default":
        args=args+" --pitch-default"
    elif request.form.get("q-pitch")=="setting":
        a07=request.form.get("pitchPitchFactor")
        a08=request.form.get("pitchSpeedFactor")
        args=args+" --pitch "+a07+" "+a08

    if request.form.get("q-gain")=="default":
        args=args+" --gain-default"
    elif request.form.get("q-pitch")=="setting":
        a09=request.form.get("gainValueLeft")
        a10=request.form.get("gainValueRight")
        args=args+" --gain "+a09+" "+a10+" db"

    if request.form.get("q-mix")=="default":
        args=args+" --mix-default"
    elif request.form.get("q-mix")=="setting":
        a11=request.form.get("mixLeft_leftRate")
        a12=request.form.get("mixLeft_rightRate")
        a13=request.form.get("mixRight_leftRate")
        a14=request.form.get("mixRight_rightRate")
        args=args+" --mix "+a11+" "+a12+" "+a13+" "+a14

    if request.form.get("q-trim")=="setting":
        a15=request.form.get("deletePartStart")
        a16=request.form.get("deletePartEnd")
        args=args+" --trim "+a15+" "+a16+" second"

    if request.form.get("q-addMute")=="insert":
        a17=request.form.get("addMuteStart")
        a18=request.form.get("addMuteLength")
        args=args+" --addMute "+a17+" "+a18+" second insert"
    elif request.form.get("q-mix")=="override":
        a19=request.form.get("addMuteStart")
        a20=request.form.get("addMuteLength")
        args=args+" --addMute "+a19+" "+a20+" second override"
    
    app.logger.info(args)
    # ShellExecute(0, "open", "DAPC.exe", args, appPath, 0)
    os.system('python3 DAPC.py '+args)
    return "{status:processing}"


@app.route('/downloadFile', methods=['GET'])
def downloadFile():
    fn=request.args.get("fileName")
    return send_file(appPath+"\\collection\\"+fn, as_attachment=True)

@app.route('/queryFile', methods=['GET'])
def queryFile():
    fn=request.args.get("fileName")
    if os.path.exists(appPath+"\\collection\\"+fn):
        return "success"
    else:
        return "processing"


if __name__ == '__main__':
    app.run(debug=False,port='80')
 
