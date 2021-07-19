
import requests
# https://api.telegram.org/bot{토큰}/setWebhook?url={pythonanywhere}

TOKEN = "1856494491:AAHC22DnZtA8IqWL2DTdG3Cm1_TQzbZrTdE"
pythonanywhere = 'jaehyeonKo.pythonanywhere.com'
url = f'https://api.telegram.org/bot{TOKEN}/setWebhook?url={pythonanywhere}/telegram'

print(requests.get(url))


#webhook을 실행하면 켜져 있음 