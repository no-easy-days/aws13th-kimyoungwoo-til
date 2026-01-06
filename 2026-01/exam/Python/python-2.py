import random
#문제: 점수를 입력받아 등급을 출력하세요.
number = int(input("점수를 입력하세요: "))
if number > 90:
    print("A")
elif 80 < number < 90:
    print("B")
elif 70 < number < 80:
    print("C")
elif 60 < number < 70:
    print("D")
else :
    print("F")

#사용자가 원하는 구구단을 출력하세요:
n = int(input("원하는 단수를 입력하세요:"))
for i in range(1,10):
    print(f"{n}*{i} = {n*i}")


primenumber = 0
for i in range(2,100):
    is_prime = True

    for div in range(2,i):
        if i%div == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")

try_num = 0
answer = random.randint(1,100)

while(True):
    num = int(input("랜덤 숫자를 맞춰보세요: "))
    try_num += 1
    if num == answer:
        print(f"정답 입니다.,{try_num}번 만에 맞추셨습니다.")
        break
    elif num > answer:
        print("입력한 숫자가 정답보다 큽니다.")
    elif num < answer:
        print("입력한 숫자가 정답보다 작습니다.")
