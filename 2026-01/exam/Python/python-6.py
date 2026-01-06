#학생 정보를 관리하는 Student 클래스를 만드세요.
from dataclasses import dataclass


class Student:
    def __init__(self,name,student_id,grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def introduce(self):
        print(f"안녕하세요, {self.grade}학년 {self.name} 입니다. ({self.student_id} 학번)")

kim = Student("김철수","2024001",1)
kim.introduce()

# 은행 계좌를 관리하는 BankAccount 클래스를 만드세요.
class BackAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            #문제의 코드 return을 하지 않음
            print("잔액이 부족합니다")
            return
        self.balance -= amount

    def get_balance(self):
        return self.balance

account = BackAccount("홍길동")
account.deposit(10000)
account.withdraw(3000)
print(account.get_balance())  # 7000

account.withdraw(10000)  # 잔액이 부족합니다

# 할 일 목록을 관리하는 TodoList 클래스를 만드세요.

class TodoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self,task):
        self.tasks.append(task)
        
    def complete_task(self,task):
        self.tasks.remove(task)
        
    def show_tasks(self):
        for task in self.tasks:
            print(task)

my_todo = TodoList()
my_todo.add_task("Python 공부")
my_todo.add_task("Git 연습")
my_todo.show_tasks()
# 출력:
# 1. Python 공부
# 2. Git 연습

my_todo.complete_task("Python 공부")
my_todo.show_tasks()
# 출력:
# 1. Git 연습

@dataclass
class DatabaseConfig:
    host: str
    port: int
    username: str
    password: str
    database: str
    timeout: int = 30
    pool_size: int =5

config = DatabaseConfig(
    host="localhost",
    port=3306,
    username="admin",
    password="secret123",
    database="myapp"
)
print(config)

class EC2Instance:
    def __init__(self,instance_id,name):
        self.instance_id = instance_id
        self.name = name
        self.status = "stopped"

    def start(self):
        print(f"{self.instance_id}에 EC2 인스턴스가 시작합니다.")
        self.status = "running"

    def stop(self):
        print("EC2 인스턴스가 정지합니다.")
        self.status = "stopped"

class EC2Manager:
    def __init__(self):
        self.instances = []

    def add_instance(self,instance):
        self.instances.append(instance)

    def start_all(self):
        for instance in self.instances:
            instance.start()

    def stop_all(self):
        for instance in self.instances:
            instance.stop()

    def get_running_count(self):
        count = 0
        for instance in self.instances:
            if instance.status == "running":
                count+=1
        return count

# 인스턴스 생성
web = EC2Instance("i-001", "web-server")
db = EC2Instance("i-002", "db-server")
cache = EC2Instance("i-003", "cache-server")

# 매니저에 등록
manager = EC2Manager()
manager.add_instance(web) # web 인스턴스를 EC2Manager에 등록
manager.add_instance(db)# db 인스턴스를 EC2Manager에 등록
manager.add_instance(cache) # cache 인스턴스를 EC2Manager에 등록

# 모두 시작
manager.start_all()
print(manager.get_running_count())  # 3

# 일부 중지
db.stop()
print(manager.get_running_count())  # 2
