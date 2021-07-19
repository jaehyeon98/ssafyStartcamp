'''
from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'

token = '1856494491:AAHC22DnZtA8IqWL2DTdG3Cm1_TQzbZrTdE'
url = f'https://api.telegram.org/bot{token}/'


@app.route('/telegram', methods=['POST'])
def receive_telegram():
    # 텔레그램으로부터 수신한 요청(request)    
    response = request.get_json()

    if response.get('message') != None:
        chat_id = response.get('message').get('from').get('id')
        text = response.get('message').get('text')

        if text == '광주2반':
            answer = '광주2반 화이팅!!\n ㅎㅎㅎㅎㅎㅎㅎ'
        else:
            answer = '머선 소리고?'

        requests.get(url + f'sendMessage?chat_id={chat_id}&text={answer}')

    return '', 200

    '''