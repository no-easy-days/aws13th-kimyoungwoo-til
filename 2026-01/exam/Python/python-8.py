import os
import datetime

def save_txt(filename):
    with open(filename,"w",encoding="utf-8") as f:
        f.write("안녕하세롱zzz\n")
        f.write("안녕하세롱z\n")
        f.write("안녕하세롱zz\n")
    print(f"{filename}에 저장되었습니다.")

def load_txt(filename):
    with open(filename,"r",encoding="utf-8") as f:
        lines = f.readlines()
    total_lines = len(lines)
    total_words = 0
    total_chars = 0
    max_line_len = 0

    for line in lines:
        words = line.split() # 공백 기준으로 단어 리스트 생성
        total_words += len(words)
        #전체 문자 수 (줄 바꿈 문자 제외)
        total_chars += len(line.strip())

        if len(line) > max_line_len:
            max_line_len = len(line)
    print(f"--- {filename} 통계 결과 ---")
    print(f"1. 전체 줄 수: {total_lines}")
    print(f"2. 전체 단어 수: {total_words}")
    print(f"3. 전체 문자 수: {total_chars}")
    print(f"4. 가장 긴 줄의 길이: {max_line_len}")

save_txt("test.txt")
load_txt("test.txt")


def write_diary():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"diary_{today}.txt"

    print(f"\n--- {today} 일기 쓰기 ---")
    content = input("오늘의 내용을 입력하세요 (엔터로 완료): ")

    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {content}\n")
    print(f"저장 완료: {filename}")


def read_diary():
    date = input("\n읽고 싶은 날짜를 입력하세요 (예: 2026-01-04): ")
    filename = f"diary_{date}.txt"

    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            print(f"\n--- {date}의 기록 ---")
            print(f.read())
    else:
        print(f"에러: {date}에 작성된 일기가 없습니다.")


def list_diaries():
    print("\n--- 저장된 일기 목록 ---")
    files = os.listdir('.')  # 현재 디렉토리 파일 목록

    diary_files = [f for f in files if f.startswith("diary_") and f.endswith(".txt")]

    if not diary_files:
        print("작성된 일기가 하나도 없습니다.")
    else:
        for f in sorted(diary_files):  # 날짜순 정렬
            print(f"- {f}")


while True:
    print("\n[심플 일기장 매니저]")
    print("1. 오늘 일기 쓰기")
    print("2. 특정 날짜 읽기")
    print("3. 모든 목록 보기")
    print("4. 종료")
    menu = input("선택: ")

    if menu == '1':
        write_diary()
    elif menu == '2':
        read_diary()
    elif menu == '3':
        list_diaries()
    elif menu == '4':
        break
    else:
        print("잘못된 선택입니다.")


def copy_file(src_path, dst_path):
    #원본 파일 존재 여부 확인
    if not os.path.exists(src_path):
        print(f"에러: 원본 파일 '{src_path}'을(를) 찾을 수 없습니다.")
        return

        # 바이너리 모드로 읽기(rb) 및 쓰기(wb)
    with open(src_path, 'rb') as src, open(dst_path, 'wb') as dst:
        chunk_size = 4096  # 4KB 단위로 처리

        while True:
            chunk = src.read(chunk_size)
            if not chunk:  # 더 이상 읽을 내용이 없으면 중단
                break
            dst.write(chunk)

        # 파일 크기 비교 및 결과 출력
        src_size = os.path.getsize(src_path)
        dst_size = os.path.getsize(dst_path)

        print(f"복사가 완료되었습니다.")
        print(f"- 원본 크기: {src_size} bytes")
        print(f"- 복사본 크기: {dst_size} bytes")

        if src_size == dst_size:
            print("결과: 파일 정합성 검사 성공 (크기 일치)")
        else:
            print("결과: 파일 크기가 다릅니다. 복사 과정을 확인하세요.")



copy_file("origin.jpg", "backup.jpg")  # 바이너리 파일 예시
copy_file("test.txt", "test_copy.txt")  # 텍스트 파일 예시
