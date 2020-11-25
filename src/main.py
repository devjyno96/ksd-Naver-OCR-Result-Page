import base64
from flask import Flask, Response, abort, request, render_template, jsonify
import json
import requests
import os


NAVER_OCR_URL = "312ab1aaaad04cb4907e2bdfb246bc67.apigw.ntruss.com/custom/v1/3870/40d9e6658a8a7c8b7d764aa349b635ea318d81480956aa066bccd98e5a61f074"
NAVER_OCR_SECRET = "VXdEdFJDZ2lrWWdRZ2FmYUpWV25SWWVaT0VuZFNPU2Y="

app = Flask(__name__)

@app.route('/', methods=['GET'])
def indexHtml():
    return render_template('index.html')


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



if __name__ == '__main__':
    app.run()
