# 구구단 가로로 출력해보기
# [힌트]아랫줄로 내려오면 윗줄로는 돌아갈 수 없다. 머릿말 부분은 따로 만들자

# [나의 답] = [선생님 답]
for dan in range(2,10):
    print(f'===={dan}단=====',end='\t')
print('\b')
for num in range(1,10):
    for dan in range(2,10):
        print(f'{dan} X {num} = {dan*num}',end='\t')
    print()

