import requests

name = 'jaehyeon'

url = f'https://api.agify.io/?name={name}&country_id=KR'

response = requests.get(url).json()

#print(type(response),response)
#print(response["age"])

ans = f'{name}의 나이는 {response["age"]}입니다.'
print(ans)



