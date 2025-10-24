# random 모듈

# 난수(random number)를 생성하는 모듈
import random

# 1) randint(정수1, 정수2) 함수
# 전달한 두 인수 사이의 정수를 임의로 생성한다.

print(random.randint(1,10))
# 1 이상 10 이하의 정수를 임의로 반환한다.
print()

# 2) randrange() 함수
# range()와 사용방법이 비슷하다.
# range로 만든 범위에 속한 정수 1개를 임의로 생성하는 함수

print(random.randrange(10)) # 0 이상 9 이하의 랜덤한 수
print(random.randrange(1,11)) # 1 이상 10 이하의 랜덤한 수
print(random.randrange(1,11,2)) # 1 이상 10 이하의 랜덤한 홀수
print()

# 3) random() 함수
# 0 이상 1 미만의 랜덤한 실수 생성
print(random.random()) #0.23143305197552277

# 50프로 확률로 안녕하세요
if random.random() >= 0.5:
    print('안녕하세요')

if random.randint(0,1):
    print('안녕하세요')
print()

# 4) choice(iterable)
# iterable의 요소 중 임의의 요소 1개를 가져온다.

seasons = ['봄', '여름', '가을', '겨울']
print(random.choice(seasons))
print()

# 5) sample(iterable) 함수
# 전달된 Iterable 에서 지정한 개수만큼의 요소를 임의로 가져오는 함수
# 반환되는 결과는 list 자료형으로 반환되며, 중복된 데이터 없이 임의의 요소가 선택된다.

print(random.sample(range(1,51), 5)) #[21, 9, 24, 34, 7]
# 1~50 랜덤하게 5개 뽑기
print()

# 6) shuffle(iterable) 함수
# 전달한 iterable의 요소 순서를 임의로 조정하는 재배치 함수
li = [1,2,3,4,5]
random.shuffle(li)
print(li)
# [2, 3, 1, 4, 5]
print()

# random 객체 시드값(seed) 설정하기
random.seed(5)
random.shuffle(li)
print(li)
random.seed(5)
random.shuffle(li)
print(li)
random.seed(5)
random.shuffle(li)
print(li)
random.seed(5)
random.shuffle(li)
print(li)