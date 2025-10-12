# for문

# 값의 범위나 횟수가 정해져 있을 때, 특정 데이터를 순회할 때(컬렉션 데이터의 모든 데이터에 접근할 때) 사용하면 편리
'''
형태
for i(for 문에서 사용할 변수명) in iterable(반복가능 객체):
    반복 실행할 코드
'''

for i in [1,2,3]:
    print(i)

# 다른 언어와 달리 조건식이 없음. i 변수에서 반복문이 실행될 떄마다 iterable의 요소를 가져온다.

# 1~10 출력
for i in range(1,11):
    print(i)

print(i) #for문이 끝나고 나서도 생성한 변수는 사용할 수 있다.

for _ in range(1,11):
    print("변수 생성하지 않고 요소의 개수만큼 _를 이용해 반복실행 가능")

'''
반복 가능 객체(iterable)
1. 시퀀스 자료형 : 순서(index)를 가진 컬렉션
ex) 문자열, 리스트, 튜플, range()..등
2. 비시퀀스 자료형 : 순서(index)가 없는 컬렉션
ex) 세트, 딕셔너리..등

'''

# 문자열 - 문자 하나한를 요소 1개로 보고 데이터를 가져온다 --> 반복하는 횟수는 문자열의 길이가 된다.
for ch in "안녕하세요":
    print(ch)

# 리스트
for i in [1,2,3]:
    print(i)

# 튜플 -->수정이 불가능한 리스트
for i in (1,2,3):
    print(i)

'''
range()함수 - for 문의 단짝. 정수의 범위를 만들어 주는 함수

기본 형태
range(초기값, 종료값, 증감값)

특징
1. 초기값부터 (종료값-1) 의 숫자들로 컬렉션을 생성한다. (초기값 <= n < 종료값)
2. 초기값을 생략하면 0 부터 시작한다
3. 종료값은 생략이 불가능하다
4. 증갑값을 생략하면 1로 지정된다.
'''

print(list(range(1,11))) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for _ in range(10):
    print("반복 실행")

for i in range(1,101):
    print(i)

for i in range(5,0,-1):
    print(i)


'''
set
[형태]
for i in {세트}:
print(i)

[특징]
요소의 개수만큼 반복을 진행하지만 가져오는 요소의 순서가 매 실행마다 순서가 없이 달라진다.
'''

for i in {"가위","바위",'보'}:
    print(i)


'''
dictionary
key와 value가 1개의 요소로 묶여있는 컬렉션 데이터

'''
# 가져오는 요소의 데이터는 key값 만 가져온다.
person = {'name':'홍길동','age':25,'addr':'대구'}
for i in person:
    print(i)

# value값 가져오기
for i in person:
    print(person[i])
    print(person.get(i))

for value in person.values():
    print(value)

for key, value in person.items():
    print(key)
    print(value)

# 리스트 내포 : 컬렉션 데이터를 생성할 때 for 문을 사용할 수 있다.
# 기본형식
# li = [표현식 for 변수(i) in iterable]

li = [i for i in range(1,11)]
print(li) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

li = [i + 3 for i in range(1,11)]
print(li) #[4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

li = [1 for _ in range(10)]
print(li) #[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

li = [i * 3 for i in range(1,11) if i % 3 == 0]
print(li) #[9, 18, 27]
# for문을 진행하는데 if 문에 적합한(True)dls i 에 대해서만 실행
