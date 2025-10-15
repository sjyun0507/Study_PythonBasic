# 과일이 2개 담긴 과일 리스트가 있다. 리스트에 없는 임의의 과일 3개를 리스트에 추가 했을 때 프로그램이 종료 되면서 리스트를 출력하세요
# 이미 리스트에 있는 과일을 추가할 시에는 과일이 추가되지 않고 지정된 문구를 출력합니다.

fruits = ['사과','감귤']

# [나의 답]
# for i in fruits:
#     fruit = input("어떤 과일을 저장할 까요? >>> ")
#     if fruit in fruits:
#         print("동일한 과일이 있습니다.")
#     else:
#         fruits.append(fruit)
#         print(fruits)
#

# [정답]
# count = 3 # 입력받을 과일의 개수
# while count > 0:
#     fruit = input("어떤 과일을 저장할 까요? >>> ")
#     if fruit in fruits:
#         print("동일한 과일이 있습니다.")
#     else:
#         fruits.append(fruit)
#         count = count - 1
#         print(f"입력이 {count}번 납았습니다.")
# print(fruits)

# [정답2]
max_count = 5
while len(fruits) < max_count:
    fruit = input("어떤 과일을 저장할 까요? >>> ")
    if fruit in fruits:
        print("동일한 과일이 있습니다.")
    else:
        fruits.append(fruit)
        print(f"입력이 {max_count-len(fruits)}번 납았습니다.")
print(fruits)

