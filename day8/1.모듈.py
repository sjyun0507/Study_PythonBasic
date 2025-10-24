# 모듈 : 언제든지 사용할 수 있도록 변수나 함수 또는 클래스를 모아 놓은 파일
# ---> 우리가 지금 까지 매일 만들던 파이썬 파일(.py)
# 모듈 생성
# converter.py 생성!

# 모듈의 데이터 가져오기
# 기본적으로 같은 디렉터리(폴더)에 위치하고 있어야 한다.

# 가져오는 형식에는 2가지 형식이 존재한다.

# 1. 모듈(파일)의 전체 데이터를 가져오는 형식
# 모듈에 저장된 모든 클래스나 함수 또는 변수를 사용하고자 할 때

# 형식
# import 모듈명

import converter
# import를 이용해서 모듈을 가져오면 모듈명의 변수가 생성된다.

miles = converter.kilometer_to_miles(5)
print(f'{miles} miles') #3.106855 miles

pound = converter.gram_to_pound(1000)
print(f'{pound} pound') #2.205 pound

print(converter.MILES) #0.621371
# 모듈 전체를 가져오게 되면 함수 또는 변수를 사용할 때 메서드의 형식으로 사용한다.
# 모듈.함수()
# 모듈.변수

# 2. 모듈에 포함된 데이터를 중에서 특정 데이터만 골라서 가져오는 방법

# from 모듈이름 import 함수
from converter import kilometer_to_miles
miles = kilometer_to_miles(5)
print(f'{miles} miles') #3.106855 miles
# pound = gram_to_pound(1000)
# print(f'{pound} pound')
# 함수나 변수 등 데이터를 명시해서 가져온다면
# 모듈 데이터(모듈 변수)를 거치지 않고 기존 데이터를 사용하듯 사용 할 수 있다.

# from 모듈이름 import * : * 모든것을 뜻하는 문자

from converter import *
pound = gram_to_pound(1000)
print(f'{pound} pound')
print(MILES)

# 알리아스 alias (별명, 별칭 짓기)
# as 라는 키워드를 사용해서 어떤 데이터에 이름을 변경할 수 있다.
# 파일 내에서 데이터의 이름을 변경하는 것이기 떄문에 기존이름으로 사용이 안된다.
# import 모듈 or data as 별칭

import converter as cv

miles = cv.kilometer_to_miles(100)
print(f'{miles} miles') #62.137100000000004 miles

from converter import kilometer_to_miles as k_to_m
miles = k_to_m(100)
print(f'{miles} miles') #62.137100000000004 miles
k_to_m(100)

# 내장모듈이나 이미 존재하는 모듈이 존재할 때 같은 파일에 똑같은 이름의 모듈이 존재하면
# 같은 위치의 모듈을 먼저 들고오게 된다. ---> 내장 모듈이랑 이름이 같은 파일은 만들지 말자