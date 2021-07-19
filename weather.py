import requests

woeid = '1132599'
url = f'https://www.metaweather.com/api/location/{woeid}/'

data = requests.get(url).json()

response = data['consolidated_weather'][2]
city = data['title']

tomorrow = response["weather_state_name"]

print(f'{city}의 모레 날씨는 {tomorrow}로 예상됩니다.')

