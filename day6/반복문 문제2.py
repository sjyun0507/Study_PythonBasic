# numbers가 있을 때 최대값과 최소값의 차이를 출력하세요

numbers = [45, 23, 67, 12, 89, 34, 56]

#[나의 답] = [선생님 답]
max_num = numbers[0]
min_num = numbers[0]
for i in numbers:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i
print(max_num)
print(min_num)
print(f'최대값과 최소값의 차이는 {max_num - min_num} 입니다.')
