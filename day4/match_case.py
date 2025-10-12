
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