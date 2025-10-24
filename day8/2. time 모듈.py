# time 모듈
import time

# time() 함수
# 1970년 1월 1일 0시 0분 0초 부터 현재까지 경과된 시간(초 == timestamp)를 반환해주는 함수
print(time.time())
# 1761277417.278882
# 정수 부분은 초, 소수점 이하는 마이크로 초를 의미한다.

# ctime() 함수
# 인수로 전달된 시간(timestamp데이터)를 날짜 형식에 맞춰 변환해준다.
print(time.ctime(time.time()))
# Fri Oct 24 12:43:16 2025

# sleep() 함수
# 인수로 전달된 초(second)만큼 시스템을 일시 정지한다.
# time.sleep(5)
# print("5초 뒤에 실행됩니다.")

# datatime 모듈
# 날짜와 시간 데이터를 처리할 때 사용하는 모듈
import datetime

# now() 메서드
# datetime모듈 내의 datetime 변수의 Now 메서드
# 컴퓨터 시스템의 현재 날짜와 시간을 반환하는 메서드
now = datetime.datetime.now()
print(now) #2025-10-24 12:46:51.638504

# date() 함수
# 입력한 인수를 기반으로 datetime객체(데이터)를 생성한다.
day = datetime.date(2025, 12, 25)
print(day) #2025-12-25

# time() 함수
# 입력한 인수를 기반으로 datetime 객체(데이터)를 생성한다.
user_time= datetime.time(15,30,10)
print(user_time) #15:30:10

# datetime() 함수
# 입력한 인수를 기반으로 datetime객체(데이터)를 생성한다.
d_day = datetime.datetime(2025,12,25,15,30,10)
print(d_day) #2025-12-25 15:30:10

result = now - d_day
print(result)  #-63 days, 21:20:27.591680
# datetime 객체(데이터)끼리는 연산이 가능하다.
# 이 때 계산결과는 timestamp 데이터가 된다.

# total_seconds() 메서드
# timestamp 데이터를 인수를 건데주면 날짜 시간을 초로 반환해준다.
print(result.total_seconds())  #-5366277.669441