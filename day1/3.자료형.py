# 자료형
# 프로그래밍을 할 댸 사용되는 숫자, 문자, 등 어떤 데이터가 담기는 형태를 형식화 해둔 것
# 다른 언어에 비해 배우기 쉬운 이유 중 1 가지로 변수를 생성할 때
# 자료형(타입)을 지정해야 하는데 파이썬의 경우 값을 변수에 할 당할 때 데이터에 맞게 타입을 자동으로 결정해서 초기화

# 자료형 4가지
# int(정수), float(실수), bool(논리값), str(문자열)

# char : 문자 데이터 (단일 문자)
# boolean의 줄임말 bool
# string의 줄임말 str


# 정수(int)
print(10)
print(10+20)
print(10+int("20"))
print(int(True))
print(int(False))
print(int(3.14))

# float(실수)
# 소수점 부분이 있는 데이터

# float(data) : data를 float 형태로 형변환 한다.
print(float(True))
print(float(False))
print(float("3.14"))
print(float(1))
# 파이썬 True와 False를 사용할 때 첫 글자를 대문자로 작성해야 한다.

# 문자열 : 문자의 배열
# 문자 : 단일 문자 자료형(char)

# 문자열의 인덱싱(indexing)
# 인덱스(index) : 순서(번호)
# 문자열이 생성되면 데이터의 문자에 자동으로 index(순서)를 매긴다.
# 문자열의 순서대로 index를 매기는데 숫자의 시작은 0으로 시작한다!

# 인덱싱
# 인덱스를 지정해서 그 인덱스에 위치한 문자를 가져오는 것

s = "hello"
print(s)
print(s[2])
print(s[0])

# 마이너스 인덱스 : 문자열의 뒤에서 부터 순서를 세는 인덱스
# 단, 마지막 문자의 인덱스는 -1이다.
# 마이너스 인덱스의 시작은 -1이다.
print(s[-1])
print(s[-2])
print(s[-5])

# 문자열의 슬라이싱(slicing)
# 인덱스를 활용해서 한 문자 이상의 단어나 문장을 추출할 때 사용

# 사용 형태
# 문자열 데이터[start:stop(:step)]

# start : 시작 인덱스를 지정, 생략하면 0으로 지정된다.
# stop : 종료 인덱스를 지정, 생략하면 문자열의 끝까지 추출한다.
# step : 인덱스의 증감값을 지정, 생략하면 +1이 지정된다.

s="hello world"
print(s[0:4]) #hell
print(s[:5]) #hello
print(s[:]) #hello world
print(s[::2]) #hlowrd
print(s[-5:]) #world
print(s[::-1]) #dlrow olleh