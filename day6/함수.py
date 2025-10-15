# 알아두면 좋은 함수

'''
len(collection data)
함수에 전달 된 객체(데이터)의 길이(요소의 개수)를 반환해주는 함수
'''

li = [1,2,3,4,5]
print(len(li)) #5
print(len("hello world")) #11
print(len({'key':'value', 'key2':'value2'})) #2

'''
sorted(iterable)
전달된 iterable 의 오름 차순 정렬결과를 반환
'''

li = [2,4,8,3,1,11,7]
print(li)
print(sorted(li)) #[1, 2, 3, 4, 7, 8, 11]
print(sorted(li,reverse=True)) #[11, 8, 7, 4, 3, 2, 1]
# reverse : 내림차순 결과를 반환

'''
zip(iterable, iterable) 함수
전달 된 여러개의 iterable 객체의 각 요소를 튜플로 묶어서 반환
'''
name = ['홍길동', '유재석']
score = [60, 70]
print(zip(name, score)) #<zip object at 0x100e57cc0>
for i in zip(name, score):
    print(i)
# ('홍길동', 60)
# ('유재석', 70)

'''
enumerate(iterable)
iterable 에 저장된 요소와 해당 요소의 인덱스를 튜플로 묶여져 있는 Iterable 반환
'''

li = ["가위","바위","보"]
for i in enumerate(li):
    print(i)
    # (0, '가위')
    # (1, '바위')
    # (2, '보')

for index, value in enumerate(li):
    print(f' 인덱스 : {index}, 데이터 : {value}')
    # 인덱스: 0, 데이터: 가위
    # 인덱스: 1, 데이터: 바위
    # 인덱스: 2, 데이터: 보

'''
eval()
문자열로 된 연산식을 int 데이터의 연산으로 취급
'''
print("100 + 200") #100 + 200
print("100" + "200") #100200
print(eval("100 + 200")) #300

'''
abs()
숫자의 절대값을 반환
'''
print(abs(-100)) #100

'''
round(반올림할 데이터, 반올림할 위치)
반올림하는 함수
'''
print(round(1.5)) #2
print(round(3.141592)) #3
print(round(3.141592,2)) #3.14
print(round(3.141592,1)) #3.1
print(round(3.141592,0)) #3.0
print(round(3.141592,-1)) #0.0


