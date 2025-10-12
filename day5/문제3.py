# 사용자로 부터 임의의 정수를 입력받아 리스트에 보관. 0을 입력하면 프로그램을 종료하고 리스트를 출력. 이때 0은 리스트에 보관하지 않음

number = int(input("정수를 입력하세요. (종료는 0입니다.) >>> "))
li = []
while number != 0:
    li.append(number)
    number = int(input("정수를 입력하세요. (종료는 0입니다.) >>> "))
# else :
print(li)
