#변수 초기화
name = "윤서정"
age = 34
address = "대구 중구 명륜로"

print(name)
print(age)
print(address)

#한번에 여러 변수 초기화

#여러 변수를 같은 값으로 초기화 할 때
a=b=c=4
print(a,b,c) #4 4 4

#여러 변수를 다른 값으로 초기화 할 때 - 데이터는 변수에 순서대로 대입된다.
a, b, c = 1, 2, 3
print(a,b,c) #1 2 3

#변수의 값 수정하기
a = 10
# 변수에 새로운 데이터를 대입하면 기존의 데이터에 덮어쓰기가 진행된다.
print(a)
print(b)

#변수간의 데이터 조합
print("a=", a, "b=", b) #a= 10 b= 2

#다른 언어 ex) c언어, java
c=a #새로운 변수를 생성해서 임시로 두 변수 중 1개의 값을 저장한다.
a=b
b=c
print("a=", a, "b=", b)

#파이썬의 경우
a,b= b,a
print("a=", a, "b=", b)

#[문제] print문을 이용해서 다이아몬드 모양 출력해보기
print('    *')
print('   ***')
print('  *****')
print('*********')
print('  *****')
print('   ***')
print('    *')
