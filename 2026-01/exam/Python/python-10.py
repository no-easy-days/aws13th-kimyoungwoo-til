#아래 코드에서 위험한 부분을 찾고, 왜 위험한지 설명하세요!
# name = input("이름: ")
# age = input("나이: ")
#
# sql = f"INSERT INTO students VALUES ('{name}', {age})"
# cursor.execute(sql)

"""
    sql에 f-string으로 입력을 하게 되면 해커가 name에 or 1=1 (무조건 참)을 대입해서
    비밀번호 없이 로그인을 성공하게 된다.
    또한 username에 drop table을 입력하게 되면 테이블이 삭제 되게 된다.
    (name = "'; Drop table users'")
    또는 name = "'UNION SELECT * from credit_cards --'"를 하게 되면 신용정보 까지 조회 될 수 있다.
    사용자가 입력한 값을 그대로 SQL에 입력하게 되므로 매우 위험하다
"""

#[실습 10.1-2] 안전한 코드로 수정하기
#%s를 붙이게 되면 파이썬에서 자동으로 백슬래시와 작은따옴표에 \를 붙여주게 된다.
name = input("이름: ")
age = input("나이: ")

sql = "insert into students values (%s,%s)"
cursor_execute(sql,(name,age))

#[실습 10.1-3] 공격 시나리오 분석

product_name = input("검색할 상품: ")
sql = f"SELECT * FROM products WHERE name = '{product_name}'"

#OR '1'='1'

#[도전 10.1-4] 이름 기반 Placeholder 활용
#아래 코드를 이름 기반 placeholder `%(key)s`를 사용하여 수정하세요.
#같은 값을 여러 번 사용하는 경우의 장점을 확인해보세요.
# 위험한 코드

keyword = input("검색어: ")
sql = f"""
    SELECT * FROM posts 
    WHERE title LIKE '%{keyword}%' 
    OR content LIKE '%{keyword}%'
    OR author LIKE '%{keyword}%'
"""
#아직 잘모르겠음..
sql = """
    SELECT * FROM posts 
    WHERE title LIKE '%{key}s%' 
    OR content LIKE '%{key}s%'
    OR author LIKE '%{key}s%'
"""
cursor_execute(sql,{"key":f"%{keyword}%"})
