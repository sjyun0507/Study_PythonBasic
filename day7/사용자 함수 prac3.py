# 숫자 또는 수식을 문자열로 입력했을 때, 계산 결과의 자리수를 반환하는 함수를 만들어 보자.

# def numOfDigits(data):
#     length = 0
#     for value in data:
#         length += 1
#     return length
#
# numOfDigits('111123')

def numOfDigits(num):
    result = eval(num)
    print(result)
    print(len(str(result)))

numOfDigits('111123')
numOfDigits('11_111_111')
numOfDigits('236**4')