#users.csv 파일을 읽어서 모든 사용자의 이름과 직업을 출력하세요.
import csv
import json
#문제 1: CSV 읽기 (기본)
with open("users.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        print(f"{row[0]} - {row[3]}")

#문제 2: CSV 필터링
with open("users.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if int(row[1]) >= 30:
            print(f"{row[0]} - {row[1]}세")

students = [
    {'학번': 'S001', '이름': '김민수', '학과': '컴퓨터공학'},
    {'학번': 'S002', '이름': '이수진', '학과': '전자공학'},
    {'학번': 'S003', '이름': '박영호', '학과': '기계공학'},
]

#문제 3: CSV 쓰기
with open("students.csv","w",encoding="utf-8",newline='') as f:
    header = ["학번","이름","학과"]
    # csv에서 dict로 하니깐 더 쉽다.. 이걸로 할 걸..ㅠㅠ
    writer =csv.DictWriter(f,fieldnames=header)
    writer.writeheader()
    writer.writerows(students)

#문제 4: JSON 읽기 (기본)
with open("config.json","r",encoding="utf-8") as f:
    data = json.load(f)

print(data["app_name"])
print(data["version"])
print(data["database"]["host"])

#문제 5: JSON 수정 및 저장
with open("config.json","r",encoding="utf-8") as f:
    data = json.load(f)

data["debug"] = True
data["features"].append("notifications")

with open("config.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=2)

#users.csv를 읽어서 users.json으로 변환하세요.
with open("users.csv","r",encoding="utf-8") as f:
    data = list(csv.DictReader(f))

with open("users.json","w",encoding="utf-8",newline='') as f:
    json.dump(data,f,ensure_ascii=False,indent=2)


#다음 JSON 로그 데이터에서 "ERROR" 레벨의 로그만 추출하여 errors.json으로 저장하세요.
with open("logs.json","r",encoding="utf-8") as f:
    data = json.load(f)

errors = []
for log in data:
    if log["level"] == "ERROR":
        errors.append(log)

with open("errors.json","w",encoding="utf-8") as f:
    json.dump(errors,f,ensure_ascii=False,indent=2)
