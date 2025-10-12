# 정수 입력값 까지 제곱의 값을 출력하기

number = int(input("정수를 입력하세요 >> "))

num = 1
while num <= number:
    print(f'입력값{num} 제곱값{num*num}')
    num += 1

