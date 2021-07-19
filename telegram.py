import requests
from pprint import pprint

token = "1856494491:AAHC22DnZtA8IqWL2DTdG3Cm1_TQzbZrTdE"

url = f'https://api.telegram.org/bot{token}'
update_url = f'{url}/getUpdates'

data = requests.get(update_url).json()
chat_id = data['result'][0]['message']['chat']['id']

text = '그래 안뇽 답변'
send_url =f'{url}/sendMessage?chat_id={chat_id}&text={text}'

data2 = requests.get(send_url)


#1844535627