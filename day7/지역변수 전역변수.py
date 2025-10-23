# 지역변수(local), 전역변수(global)
# c언어, java에서는 {}코드블럭 내에서 선언한 변수를 지역변수라고 한다.
# 단, 파이썬에서는 함수 내부에서 선언한 변수들을 지역변수라고 한다.

def temp():
    num = 10
    print(num)
# temp()
# print(num) # 함수 내부에서 변수를 선언하면 함수 밖에서 그 변수를 알아보지 못한다.
# ---> 지역변수는 선언한 구역에서 벗어나면 생성한 변수를 삭제한다.

num = 5
def temp2():
    num = 10
    print(num)
temp2() #10
print(num) #5
# 전역변수와 지역변수는 이름이 같아도 다른 변수로 취급된다.

def temp3():
    global num # 전역 변수로 설정
    num = 10
    print(f'num={num}') #num=10
temp3()
print(f'num={num}') #num=10


def temp4():
    n = 10
    def temp5():
        # nonlocal n # 상위 레벨의 지역변수를 가져와서 사용할 수 있다. temp4의 n을 가져와 100을 만듬 num=100
        n = 100
        print(n)
    temp5() #100
    print(f'num={n}') #10
temp4() #num=10