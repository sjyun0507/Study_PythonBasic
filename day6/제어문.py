# 제어문 : 프로그램의 실행 흐름을 제어하는 구문
# if, 반복문, break, continue문

'''
break문
while 이나 for 문과 같은 반복문에서 사용하는 제어문
자신이 속한 코드블럭의 반복문을 강제로 종료하는 제어문

while 문에서 만이 사용
'''

for i in range(10):
    print(i)
    if i == 5 :
        break

li = []
while True:
    num = int(input("숫자를 입력하세요 >>> "))
    if num == 0: break
    li.append(num)
print(li)


for i in range(3): # 3번 반복
    for j in range(4): # [0,1,2,3]
        print(j)
        break # 영향을 줄수 있는 반복문의 개수는 1개 이다.

# continue 문
# 반복문에서 사용하는 제어문
# 반복문에서 continue를 만나면 반복문의 시작 지점으로 제어의 흐름을 옮긴다. (다음 회차의 반복을 실행한다)

# 1-50 사이의 숫자를 출력할 때 3의 배수는 제외한다.

for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)
# For 문의 경우에는 변수(i)에 다음 요소를 가져와서 코드블럭의 첫 부분으로 돌아간다.

num = 1
while num < 5:
    if num == 3:
        print("continue문")
        num += 1
        continue
    print(num)
    num += 1
'''
while 문에서는 반복문의 시작 시점이 조건식을 확인 하는 것 이기 때문에, continue 문을 만나면 그 위치로 이동한다.
따라서, continue문이 실행되기 전에 증감식을 작성해서 코드의 무한 루프를 조심해야 한다.
'''

# pass 문
# 이름만 정의해두고 실행 부분을 나중에 구현할 때, 특정 조건문이나 반복문에서 아무 동작도 구현할 필요가 없을 때
