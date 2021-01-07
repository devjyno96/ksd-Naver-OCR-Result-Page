import base64
from flask import Flask, Response, abort, request, render_template, jsonify, flash, redirect, url_for
import json
import requests
import os

from pathlib import Path

from werkzeug.utils import secure_filename

from  KSD_STT import stt_run as stt


NAVER_OCR_URL = "312ab1aaaad04cb4907e2bdfb246bc67.apigw.ntruss.com/custom/v1/3870/40d9e6658a8a7c8b7d764aa349b635ea318d81480956aa066bccd98e5a61f074"
NAVER_OCR_SECRET = "VXdEdFJDZ2lrWWdRZ2FmYUpWV25SWWVaT0VuZFNPU2Y="


path = Path(os.path.realpath(__file__))
UPLOAD_FOLDER = str(path.parent.parent) + '/audioFiles'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def indexHtml():
    return render_template('index.html')

@app.route('/stt', methods=['GET'])
def sttHtml():
    return render_template('Azure_STT.html')


@app.route('/api/ocr-requests', methods=['POST'])
def newOCRRequest():

    result = requests.post('https://{}/infer'.format(NAVER_OCR_URL), headers={
        'X-OCR-SECRET': NAVER_OCR_SECRET
    }, files={
        'file': request.data
    }, data={
        'message': json.dumps({
            'version': 'V2',
            'requestId': 'ocr-request',
            'timestamp': 0,
            'images': [{
                'format': 'jpg',
                'name': 'image',
                'data' : base64.b64encode(request.data).decode("utf-8")
            }]
        })
    })
            
    return json.dumps(result.json(), ensure_ascii=False)



@app.route('/api/stt', methods=['POST'])
def sttApi():
    if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    result_str = stt.run(bool_mic = False, file_name = UPLOAD_FOLDER + "/" + file.filename)

    os.remove(UPLOAD_FOLDER + "/" + file.filename)

    result = {'result' : "test_val"}

    result['result'] = result_str
    
    return jsonify(result)



if __name__ == '__main__':
    app.run()
