import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url)

#print(response.text)

data = BeautifulSoup(response.text, 'html.parser')
print(data.select_one('#exchangeList > li.on > a.head.usd > div > span.value'))
print(data.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text)

