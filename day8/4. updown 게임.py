# 1 ~ 100 범위에서 랜덤값을 가져와 updown게입을 만들어 보자.
# 틀리면 Up이나 down을 말해주고, 맞추면 정답까지 걸린 시간을 알려주자

import random
import datetime

# game = random.randrange(1,101)
# for i in int(game):
#      updown = int(input("어떤 값일까요? "))
#      if updown == game :
#          print(f"정답입니다.")
#          break
#      elif updown > game :
#          print("오답입니다. 다시 입력해주세요")
#          print("down")
#      elif updown < game :
#          print("오답입니다. 다시 입력해주세요")
#          print("up")
# print("시스템을 종료합니다")

game = random.randint(1,100)
print(f'정답: {game}')
print("updown 게임을 시작합니다.")
start = datetime.datetime.now()

while 1:
    user = int(input("어떤 값일까요? "))
    if user == game:
        end = datetime.datetime.now()
        time = end - start
        print(f"정답입니다. 걸린시간 {time.total_seconds():.2f}초")
        print("시스템을 종료합니다")
        break
    else :
        print("오답입니다. 다시 입력해주세요")
        if user > game:
            print("down")
        else:
            print("up")

