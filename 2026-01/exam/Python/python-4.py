#문제: 두 숫자와 연산자(+, -, *, /)를 받아 계산 결과를 반환하는 함수를 만드세요.
def calculator(a,b,operator):
    if operator == "+":
        return a+b
    if operator == "-":
        return a-b
    if operator == "*":
        return a*b
    if operator == "/":
        if a == 0 or b == 0:
            return "0으로 나눌 수 없습니다."
        else:
            return a/b
    else:
        return "지원하지 않는 연산자 입니다."

print(calculator(10, 5, '+'))  # 15
print(calculator(10, 5, '-'))  # 5
print(calculator(10, 5, '*'))  # 50
print(calculator(10, 5, '/'))  # 2.0
print(calculator(10, 0, '/'))  # 0으로 나눌 수 없습니다
print(calculator(10, 5, '%'))  # 지원하지 않는 연산자입니다

#문제: 학생 이름과 점수 리스트를 받아 성적표를 출력하는 함수를 만드세요.

def print_report(name, scores):
    temp_avg = 0
    for i in range(scores.__len__()):
        temp_avg += scores[i]
    temp_avg /= scores.__len__()

    temp_max = 0
    for i in range(scores.__len__()):
        if scores[i] > temp_max:
            temp_max = scores[i]
    temp_min = temp_max
    for i in range(scores.__len__()):
        if scores[i] < temp_min:
            temp_min = scores[i]

    grade = ""
    if temp_avg > 90:
        grade = "A"
    elif temp_avg > 80:
        grade = "B"
    elif temp_avg > 70:
        grade = "C"
    elif temp_avg > 60:
        grade = "D"
    else:
        grade = "F"

    print(f"==={name} 성적표 ===")
    print(f"점수 : {scores}")
    print(f"평균 : {temp_avg}")
    print(f"최저점 : {temp_min}")
    print(f"최고점 : {temp_max}")
    print(f"등급 : {grade}")
    pass

print_report("김철수", [85, 92, 78, 96, 88])
# 예상 출력:
# === 김철수 성적표 ===
# 점수: [85, 92, 78, 96, 88]
# 평균: 87.8점
# 최고점: 96점
# 최저점: 78점
# 등급: B

# 문제: 비밀번호가 조건을 만족하는지 검증하는 함수를 만드세요.
def validate_password(password):
    if len(password) < 8:
        return "비밀번호는 8자 이상이어야 합니다."

    has_digit = False
    has_upper = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True

    if not has_digit:
        return "숫자를 포함해야 압니다."
    if not has_upper:
        return "대문자를 포함해야 합니다."

    return "유효한 비밀번호 입니다."

print(validate_password("abc"))        # (False, "8자 이상이어야 합니다")
print(validate_password("abcdefgh"))   # (False, "숫자를 포함해야 합니다")
print(validate_password("abcdefg1"))   # (False, "대문자를 포함해야 합니다")
print(validate_password("Abcdefg1"))   # (True, "유효한 비밀번호입니다")
