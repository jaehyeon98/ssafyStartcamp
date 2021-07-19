import requests

token = "1856494491:AAHC22DnZtA8IqWL2DTdG3Cm1_TQzbZrTdE" 
key = 	"nViS6jcXvJbGauKnWr%2Fb7gjCMfDATdmdIEBw3W9uCNSMzIABaoRVjLrqRvFEyv3WKB5mefO5T8Pgu5Pv%2BUyiBw%3D%3D"
dust_url = f"http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&pageNo=1&numOfRows=100&returnType=json&serviceKey={key}&ver=1.0"

url = f'https://api.telegram.org/bot{token}'

#requests.get(f'{url}/deleteWebhook') #webhook 끄기

update_url = f'{url}/getUpdates'
data = requests.get(update_url).json()
result = data["result"]

data2 = requests.get(dust_url).json()

if (result[len(result)-1]['message']['text'] == "미세먼지"):
    chat_id = result[len(result)-1]['message']['chat']['id']
    dust = data2['response']['body']['items'][0]['pm10Value']
    text = f"서울의 미세먼지 농도는 {dust}입니다!"

else:
    chat_id = result[len(result)-1]['message']['chat']['id']
    text = "안녕하세요! 미세먼지라고 입력해보세요"


send_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(send_url)


