# 구구단 2단부터 9단까지 출력하기

dan = 2
while dan <= 9:
    print(f'===={dan}단====')
    num = 1
    while num <= 9:
        print(f'{dan} X {num} = {dan * num}')
        num += 1
    dan += 1
