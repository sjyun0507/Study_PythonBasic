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

