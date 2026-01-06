#문제: 다음 도시 목록을 인구수 기준으로 정렬하세요.
cities = [
    {"name": "서울", "population": 9700000},
    {"name": "부산", "population": 3400000},
    {"name": "인천", "population": 2900000},
    {"name": "대구", "population": 2400000}
]

sorted_cities = sorted(cities, key=lambda x: x["population"])

for p in sorted_cities:
    print(p["name"])

#문제: 문자열 리스트를 정수 리스트로 변환하고, 각 숫자에 100을 더하세요.

str_numbers = ["10", "20", "30", "40", "50"]
#int_numbers = list(map(lambda x: x +100, map(int, str_numbers)))
int_numbres = str_numbres[int(x) + 100 for i in str_numbers]
print(int_numbers)

#문제: 할인율이 20% 이상인 상품만 추출하세요.
products = [
    {"name": "노트북", "discount": 15},
    {"name": "마우스", "discount": 25},
    {"name": "키보드", "discount": 30},
    {"name": "모니터", "discount": 10}
]

discounted = list(filter(lambda x: x["discount"] >= 20,products))
print(discounted)
