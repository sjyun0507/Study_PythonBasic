
# 산술연산자
a = 7
b = 2

print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}%{b}={a%b}') #나머지 연산자
print(f'{a}//{b}={a%b}') #나눈 몫을 구하는 연산자
print(f'{a}**{b}={a**b}') #제곱연산자

#대입연산자 (=)
# =를 이용해서 변수의 값을 변경하는 것을 값의 대입이라고 한다

#변수 = data

# 단항 연산자 : 산술 연산자 + 대입연산자
num = 5
num = num + 10
print(num)
# 변수 산술 연산자 = 계산할 값

num += 10
print(num)

#오른쪽의 데이터(연산식)의 결과값을 등호에 붙은 산술 연산을 변수에 진행한다

num -= 5
print(num)

#비교연산자(관게연산자)
#데이터 A와 B의 관계를 연산한다
#결과값은 True나 False 둘중 하나를 반환한다.

a = 15
print(f'{a} > 10 : {a > 10}') #15 > 10 : True
print(f'{a} < 10 : {a < 10}') #15 < 10 : False

print(f'{a} >= 10 : {a >= 10}')
print(f'{a} <= 10 : {a <= 10}')

print(f'{a} == 10 : {a == 10}')
print(f'{a} != 10 : {a != 10}')

# 논리 연산자 : 비교 연산자 또는 boolean 값을 연결 해주는 연산자
# 결과 값은 True 또는 False 두 가지이다
# 종류 and, or, not

# A와 B가 각각 비교 연산 또는 boolean 값일 때
# not A : A가 False 이면 True, True 이면 False로 변환
a = 15
b = 0
print(f'{a} > 10 and {b} > 0 : {a > 10 and b > 0}')
print(f'{a} < 10 or {b} > 0 : {a > 10 or b > 0}')
print(f'not {a} : {not a}')
print(f'not {b} : {not b}')
print(f'not {""} : {not ""}')

'''
비트 연산자
숫자를 비트 단위(2진수)로 변환한 후에 비트 단위의 연산을 진행 하는 연산자 -> 2진수로 변환 하고 같은 자리 수에서 비교 연산을 진행
&(and) : 비교하는 두 비트가 1이라면 1, 그게 아니면 0
|(or) : 비교하는 두 비트 중 하나라도 1이라면 1, 그게 아니면 0
^(xor) : 비교하는 두 비트가 다르면 1, 같으면 0
~(not) : 비트가 1이라면 0으로, 0이라면 1로 변환
<<, >> : 시프트 연산자 - 비트를 부등호 방향으로 이동시키는 연산자
'''

a = 10
b = 70

print(bin(a)) #00001010
print(bin(b)) #01000110

print(f'a & b: {a & b},{bin(a & b)}') #a & b: 2,00000010
print(f'a | b: {a | b},{bin(a | b)}') #a | b: 78,01001110
print(f'a ^ b: {a ^ b},{bin(a ^ b)}') #a ^ b: 76,01001100
print(f'~a: {~a},{bin(~a)}') #~a: -11,-00001011

# 음수 표현 : 보통 가장 자리 수가 큰 비트를 부호 비트로 사용 한다.
# byte 데이터로 예시
# 1000 0000 : -128
# 1000 0001 : -127
# 1111 1111 : -1
# 0000 0000 : 0

# ~연산에서 최상위 비트가 바뀌어서 -값으로 변환한다

'''
멤버쉽 연산자
data(변수 등) in [iterable]

iterable : 반복가능 객체 -> 순회가 가능한 객체
결과값은 True, False 두가지로 반환된다
'''

print(5 in [1,2,3,4,5]) #True
print('a' in ['a','b','c','d','e']) #True