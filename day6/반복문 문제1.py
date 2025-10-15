# for 문을 이용해서 다음과 같이 숫자를 출력해보자
'''
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''

#[나의 답]
li = [i for i in range(1,6)]
li2 = [i for i in range(6,11)]
li3 = [i for i in range(11,16)]
li4 = [i for i in range(16,21)]
li5 = [i for i in range(21,26)]
print(li)
print(li2)
print(li3)
print(li4)
print(li5)


#[선생님 답]
for i in range(1,26):
    print(i, end="\t")
    if i % 5 == 0:
        print('\b')

for i in range(1,22,5):
    for j in range(5):
        print(i+j, end="\t")
    print('')