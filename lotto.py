import random
numbers = []
for i in range(1,46):
    numbers.append(i)

lotto = random.sample(numbers,6)

print('이번주 로또의 예상 번호는 ', end="")
for i in lotto:
    print(i, end=" ")

print("입니다.")

'''
li = [1, 2, 3] 
# 리스트에서 2개 랜덤 추출(중복 허용) 
# choiceLIst = [random.choice(li) for i in range(2)]
'''