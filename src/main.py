import base64
from flask import Flask, Response, abort, request, render_template, jsonify, flash, redirect, url_for
import json
import requests
import os
import time

from pathlib import Path

from werkzeug.utils import secure_filename

from KSD_STT import stt_run as azure_stt

from Clova_STT.ClovaSpeechClientObject import ClovaSpeechClient as clova_stt

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


@app.route('/stt/ksd', methods=['GET'])
def sttKsdHtml():
    return render_template('ksd-result.html')


@app.route('/stt/keyword-analysis', methods=['GET'])
def KsdkeywordAnalysis():
    return render_template('keyword-analysis.html')


@app.route('/stt/sentiment-analysis', methods=['GET'])
def KsdSentimentAnalysis():
    return render_template('sentiment-analysis.html')


@app.route('/api/ocr-requests', methods=['POST'])
def newOCRRequest():
    # print(request.data[:1000])
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
                'data': base64.b64encode(request.data).decode("utf-8")
            }]
        })
    })
    return json.dumps(result.json(), ensure_ascii=False)


@app.route('/api/ocr-requests/s3', methods=['POST'])
def newOCRRequestS3():
    data = request.data.decode('utf-8').split('=')[1]

    request_json = {
        'images': [
            {
                'format': data.split('.')[-1],
                'name': 'image',
                'url': data
            }
        ],
        'requestId': 'ocr-request',
        'version': 'V2',
        'timestamp': int(round(time.time() * 1000))
    }

    payload = json.dumps(request_json).encode('UTF-8')
    headers = {
        'X-OCR-SECRET': NAVER_OCR_SECRET,
        'Content-Type': 'application/json'
    }

    return json.dumps(
        requests.request("POST", 'https://{}/infer'.format(NAVER_OCR_URL), headers=headers, data=payload).json(),
        ensure_ascii=False)


# @app.route('/api/stt', methods=['POST'])
# def sttApiAzure():
#     if 'file' not in request.files:
#         flash('No file part')
#         return redirect(request.url)
#
#     file = request.files['file']
#
#     if file.filename == '':
#         flash('No selected file')
#         return redirect(request.url)
#
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
#
#     result_str = azure_stt.run(bool_mic=False, file_name=UPLOAD_FOLDER + "/" + file.filename)
#
#     os.remove(UPLOAD_FOLDER + "/" + file.filename)
#
#     result = {'result': "test_val"}
#
#     result['result'] = result_str
#
#     return jsonify(result)


@app.route('/api/stt', methods=['POST'])
def sttApiClova():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    # result_str = azure_stt.run(bool_mic=False, file_name=UPLOAD_FOLDER + "/" + file.filename)
    result_str = clova_stt().speech_cognition(UPLOAD_FOLDER + "/" + file.filename)

    os.remove(UPLOAD_FOLDER + "/" + file.filename)

    result = {'result': "test_val"}

    result['result'] = result_str

    return jsonify(result)


if __name__ == '__main__':
    app.run()
