import requests

key = 'iTpdD5hhMW71PQus57ztCitlpMM8T4ntl3mEe%2FTzhseoUcgTpG5kR29kq7%2FcxYy4ky3ufUl%2B5wvT5JURzmFmTg%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=5&pageNo=1&sidoName=서울&ver=1.0&returnType=json'
response = requests.get(url).json()

#print(response)

sido_name = response['response']['body']['items'][0]['sidoName']
dust = response['response']['body']['items'][0]['pm10Value']
station_name = response['response']['body']['items'][0]['stationName']

print(f'{sido_name} {station_name}의 미세먼지 농도는 {dust}입니다.')