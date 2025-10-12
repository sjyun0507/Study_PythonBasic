'''
삼항 연산자
참일 때 실행할 코드  if 조건식 else 거짓일 경우 실행할 코드
보통은 간단한 조건에 따른 변수에 값을 초기화할 때 자주 사용
삼항 연산자 안에서 함수도 사용 가능하다
'''

a = 70
b = 20

big_num = a if a > b else ("삼항 연산 중첩" if b > 10 else "연습")

print(f'큰수는 {big_num}')

print("참") if True else print("거짓")