'''
[문제] 나이를 입력받아 7살 이하면 '미취학 아동', 8~13 이면 '초등학생', 14~16살이면 '중학생' 17~19살이면 '고등학생'
20살 이상이면 '성인'을 출력하는 프로그램
'''

# age = int(input("몇 살 입니까? "))
# if 0 < age <=7 :
#     print("미취학 아동")
# elif 8 <= age <= 12:
#     print("초등학생")
# elif 13 <= age <= 16 :
#     print("중학생")
# elif 17<= age <= 19 :
#     print("고등학생")
# elif age >= 20 :
#     print("성인")
# else:
#     print("음수는 작성할 수 없습니다")


'''
[문제2] 점수를 받아 평균과 합격 여부를 만들어라
'''
# kor = int(input("국어 점수를 입력하세요>>> "))
# eng = int(input("영어 점수를 입력하세요>>> "))
# mat = int(input("수학 점수를 입력하세요>>> "))
# avg = (kor+eng+mat)/3

# [나의 오답]
# result = (print("합격")) if avg >= 80 else print("불합격")

# [해답예시1]
# if avg >= 80:
#     print(f"평균은 {avg:.1f}이고, 결과는 합격입니다")
# else:
#     print(f"평균은 {avg:.1f}이고, 결과는 불합격입니다")

# [해답예시2]
# print(f"평균은 {avg:.1f}이고, 결과는 ", end="")
# if avg >= 80:
#     print("합격입니다")
# else:
#     print("불합격입니다")

# [해답예시3]
# result = "합격" if avg >= 80 else "불합격"
# print(f"평균은 {avg:.1f}이고, 결과는 {result}입니다")


'''
[문제3] 미세먼지 저감 활동의 일환으로 차량 2부제를 실시한다. 사용자로 부터 차량번호를 입력받아 짝수로 끝나면 운행가능, 아니면 운행 불가를 출력
실행예시 
차량번호를 입력하세요>>> 237가1234
차량번호는 '23가1234'는 오늘 운행가능입니다.
'''
#
# [나의 오답]
# num = input("차량 번호를 입력하세요>>> ")
# available = "운행가능" if int(num) % 2 == 0 else "운행불가"
# print(f"차량번호 '{num}'는 오늘 {available}입니다")

# [답변예시1]
car = input("차량 번호를 입력하세요>>> ")
car_last_num = int(car[-1])
if car_last_num % 2 == 0 :
    print(f"차량번호 '{car}'는 오늘 운행가능입니다")
else :
    print(f"차량번호 '{car}'는 오늘 운행불가입니다")

# [답변예시2]
if car_last_num in ["2","4","6","8","0"]:
    print(f"차량번호 '{car}'는 오늘 운행가능입니다")
else:
    print(f"차량번호 '{car}'는 오늘 운행불가입니다")