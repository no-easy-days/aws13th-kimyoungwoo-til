#3.1. 자료형 실습 문제
#사용자로부터 이메일 주소를 입력받아 사용자 이름과 도메인을 분리하여 출력하세요.
#입력 예시: jeff@example.com

#문제
#비밀번호가 8자 이상인지 확인하는 프로그램을 작성하세요.
#조건: 길이가 8자 이상이면 "✅ 유효한 비밀번호입니다." 출력

password = input("비밀번호가 8자 이상인지 확인하는 프로그램 입니다.")
if len(password) > 8:
    print("유효한 비밀번호입니다.")
else:
    print("유효하지 않은 비밀번호입니다.")

#철수와 영희의 관심사 리스트가 주어졌을 때, 공통 관심사를 찾아보세요.
chulsoo = ["축구", "영화", "음악", "게임", "독서"]
younghee = ["영화", "음악", "요리", "여행", "독서"]

set_chulsoo = set(chulsoo)
set_younghee = set(younghee)

interest = set_chulsoo & set_younghee # 교집합
print(f"공통 관심사 : {interest}")

#학생들의 점수가 딕셔너리로 주어졌을 때, 최고 점수를 받은 학생을 찾아보세요.
scores = {
    "철수": 85,
    "영희": 92,
    "민수": 78,
    "지수": 95,
    "현우": 88
}
top_students = max(scores,key=scores.get)
max_score = scores[top_students]
print(f"최고 점수 학생은 : {top_students}, 최고 점수는 : {max_score}")
