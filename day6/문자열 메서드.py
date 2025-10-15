# 메서드 : 특정 객체(데이터)가 가지고 있는 함수를 의미한다
# 함수와 달리 특정 객체가 가지고 있는 함수 이기 떄문에 호출(사용)하려면 특정 객체가 필요하다

# 문자열 메서드 : 문자열이 가지고 있는 함수

'''
count(찾을 문자열)
문자열 내부에서 찾는 문자열의 개수를 반환하는 메서드
'''

s = "내가 그린 기린 그림은 목 긴 기린 그림이고..."
print(s.count("기린")) #2

# 인덱스를 지정해서 내가 찾을 범위를 지정할 수 있다.
# count(찾을 문자열, 시작 인덱스, 종료 인덱스)
print(s.count("기린", 10)) #1

# find(찾을 문자열) 메서드
# 내가 찾는 문자열의 위치(index)를 반환하는 메서드
print(s.find("그린")) #3
print(s.find("기린")) #6
# 찾는 문자열이 여러 개 존재한다면 가장 먼저 나오는 문자열의 index를 반환

print(s.find('z'))
# 찾는 문자열이 존재하지 않는다면 -1을 반환한다.

# count와 마찬가지로 index 를 이용해서 범위 지정이 가능하다
# find(찾을 문자열, 시작 인덱스, 종료 인덱스)

'''
대소문자 변환 메서드
upper()     : 모든 문자를 대문자로 변환
lower()     : 모든 문자를 소문자로 변환
capitalize(): 첫 글자를 대문자로, 나머지는 소문자로 변환
'''

s="PYthon"
print(s.upper()) #PYTHON
print(s.lower()) #python
print(s.capitalize()) #Python

print('-'.join("python")) #p-y-t-h-o-n
print('+'.join(['a','b','c','d'])) #a+b+c+d
print(''.join(['a','b','c','d'])) #abcd

'''
split(구분자)
하나의 문자열을 여러 개의 문자열로 분리해서 요소로 저장한 리스트를 반환하는 메서드
'''

s = 'Study is too hard'
s2 = s.split()
print(s2) #['Study', 'is', 'too', 'hard']
# 기분적으로 구분자를 지정하지 않았다면 공백을 기준으로 문자열을 분리해서 리스트에 담아준다.

s = "010-1234-5678"
print(s.split('-')) #['010', '1234', '5678']


'''
replace() 메서드
문자열의 일부 문자열을 다른 문자열로 바꿔서 반환해주는 메서드
'''
s = 'hello world'
print(s.replace('hello','goodbye')) #goodbye world

s = "010-1234-5678"
print(s.replace('-','')) #01012345678

'''
strip(삭제할 문자열) 메서드
문자열의 양끝에 있는 불필요한 문자를 제거하는 메서드

lstrip : 왼쪽 부분만 strip
rstrip : 오른쪽 부분만 strip
'''
s = '      data'
print(s)
print(s.strip())
#       data
# data

s='<<<<<<<<<data<<<<<<<<'
print(s.strip('<')) #data
print(s.lstrip('<')) #data<<<<<<<<
print(s.rstrip('<')) #<<<<<<<<<data

