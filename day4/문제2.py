
'''
[문제2] 점수를 받아 평균과 합격 여부를 만들어라
'''
kor = int(input("국어 점수를 입력하세요>>> "))
eng = int(input("영어 점수를 입력하세요>>> "))
mat = int(input("수학 점수를 입력하세요>>> "))
avg = (kor+eng+mat)/3

# [나의 오답]
# result = (print("합격")) if avg >= 80 else print("불합격")

# [해답예시1]
if avg >= 80:
    print(f"평균은 {avg:.1f}이고, 결과는 합격입니다")
else:
    print(f"평균은 {avg:.1f}이고, 결과는 불합격입니다")

# [해답예시2]
print(f"평균은 {avg:.1f}이고, 결과는 ", end="")
if avg >= 80:
    print("합격입니다")
else:
    print("불합격입니다")

# [해답예시3]
result = "합격" if avg >= 80 else "불합격"
print(f"평균은 {avg:.1f}이고, 결과는 {result}입니다")

