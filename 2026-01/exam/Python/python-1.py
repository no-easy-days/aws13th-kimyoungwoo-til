#1. 자신의 이름, 나이, 좋아하는 숫자를 각각 변수에 저장하고 출력하는 코드를 작성하세요.
name = "김영우"
age = 25
favorite_number = 10

print(name,age,favorite_number)

#2. first = "A"와 second = "B" 두 변수의 값을 서로 교환하세요.
first = "A"
second = "B"
first,second = second,first
print(first,second)

#3.balance = 10000에서 시작하여 3000을 빼고, 2를 곱한 뒤 최종 값을 출력하세요.
balance = 10000
balance -= 3000
balance *= 2
print(balance)

#4. 아래 코드의 오류를 찾고 수정하세요
second_place = "은메달"
user_name = "홍길동"
first_class = "1학년"

#5.🔥 실습 5: 자료형 확인하기 (기초)
print(type(45),type(3.14),type("Hello"),type(True),type(None))

#실습 6: 형변환 연습 (기초)
num1 = int(input("두 숫자를 입력하세요:"))
num2 = int(input("두 숫자를 입력하세요:"))
print(num1+num2)

#실습 7: 사용자의 이름, 나이, 키를 입력받아 자기소개 문장을 출력하세요.
#- 내년 나이도 함께 계산하여 출력
#- f-string을 사용할 것
user_Name = input("이름을 입력하세요: ")
user_Age = int(input("나이를 입력하세요: "))
user_Height = int(input("키를 입력하세요: "))

print(f"이름은 {user_Name}, 나이는 {user_Age}, 키는 {user_Height} 이고 내년 나이는 {user_Age+1} 입니다.")

#실습 8: 계산기 만들기 (심화)
#두 숫자와 연산자를 입력받아 계산 결과를 출력하는 간단한 계산기를 만드세요.
#- 덧셈, 뺄셈, 곱셈, 나눗셈, 몫, 나머지를 모두 지원

num1 = float(input("첫 번째 숫자를 입력하세요:"))
operator = input("연산자를 입력하세요:")
num2 = float(input("두 번째 숫자를 입력하세요:"))

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    if(num1 == 0 or num2 == 0):
        print("0으로 나눌 수 없습니다.")
    else:
        print(num1/num2)
elif operator == "%":
    print(num1%num2)
elif operator == "//":
    print(num1//num2)
else:
    print("지원하지 않는 연사자 입니다.")
