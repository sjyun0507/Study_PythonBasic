
# key가 과목명 value 값이 점수인 test 딕셔너리를 전달하면 해당 딕셔너리에 저장된 점수들의 평균을 반환하는 함수를 구현하세요
# 평균 점수는 소수점 2자리 까지 출력되어야 합니다.


# def average(value):
#     return sum(value) / len(test)
# print(average(test))

def average(data):
    sum = 0 # 합계를 저장할 변수
    for key in data: # 딕셔너리를 순회하는 for 문
        sum += data[key] # key에는 딕셔너리의 key 값이 반복마다 담기게 된다.

    # for value in data:
    #     sum += value

    # for key, value in data.items():
    #     sum += value

    avg = sum / len(data)
    return round(avg,2)
test = {'국어': 90, '영어': 63, '수학': 77}
print(average(test)) #76.67