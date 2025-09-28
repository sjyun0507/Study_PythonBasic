# if 문
# 조건식의 결과가 True일 때 실행되는 코드

if True :
    print(True)

if False :
    print(False)

# 조건식의 데이터(식)은 무조건 True나 False로 변환이 가능한 값이어야 한다.

if 1 :
    print("조건식의 결과가 참입니다.")
    print("if문이 끝난 후 의 일반적인 코드")

'''    
코드블럭을 :과 들여쓰기를 수행

들여쓰기 규칙
1. 공백(space)나 탭(tap)을 이용해서 들여쓰기를 수행한다.
2. 공백의 개수는 신경쓰지 않는다.
3. 동일 구역(코드블럭)에서는 들여쓰기(공백의 넓이)가 동일해야 한다.
4. 주로 사용하는 들여쓰기는 공백 4칸(탭1번) or 공백 1칸이다.
'''

'''
if - elif (다중 분기문)
elif --> else if

if 조건문1 : 
    조건문 1의 결과가 True일 때 실행
elif 조거문2:
    조건문 1의 결과가 False 고, 조건식 2의 결과가 True 일 때 실행하는 코드
elif 조건문3:
    조건문1,2의 결과가 False 고, 조건식 3의 결과가 True일 떄 실행하는 코드
else:
    위의 모든 조건문이 False 인 경우 실행하는 코드블럭
'''

score = int(input("점수를 입력하세요>>>"))
if score >= 80:
    print("상")
elif score >= 50:
    print("중")
else:
    print("하")

'''
match - case문
다른 언어의 switch - case문과 비슷
파이썬 3.1.0버전에서 추가

match [data(변수) or 식] :
    case case1:
        식의 결과가 case1인 경우에 실행
    case case2:
        식의 결과가 case2인 경우에 실행
    case _:
        if문의 else문  
'''

num = 1,2,3,4
match num:
    case 1:
        print("num == 1")
    case 5:
        print("num == 5")
    case [1,2,3,4]:
        print("컬렉션 데이터를 넣을 수도 있다")
    case 2 | 4 | 6 | 8 | 0:
        print("num은 2또는 4또는 6또는 8또는 0이다")
    case num if num in [1,2,3,4,5] :
        print("num이 [1,2,3,4,5]에 포함한다")
        #멤버쉰 연산자를 이용해서 case를 작성할 수 있다.
    case _:
        print("모든 케이스에 일치하는 것이 없다")



'''
삼항연산자
'''
a = 80
b = 70
result = (a-b) if (a>=b) else (b-a)
print("참") if (a>=b) else print("거짓")