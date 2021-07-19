import random
lunch  = ['김밥천국', '짜장면집', "새마을식당"]
key = random.choice(lunch)
menu = {'김밥천국': '1234-1235', '짜장면집': '3452-357', "새마을식당": "2222-3333"}
print("오늘의 추천 메뉴는", key, "입니다!")
print(key, "의 전화번호는 ",menu[key], "입니다~")

