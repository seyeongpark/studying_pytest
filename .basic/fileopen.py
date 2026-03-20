# 파일오픈
try: 
    open("basic/output.txt", "r") # 읽기 위함은 r, 쓰기 위함은 w, 추가하기 위함은 a
except FileNotFoundError: # 파일이 존재하지 않을 때 발생하는 예외
    print("파일을 찾을 수 없습니다.")
except Exception as e: # 모든 예외의 부모 클래스인 Exception을 사용하여 다른 예외도 처리할 수 있습니다.
    print(f"에러가 발생했습니다: {e}")
else: # 예외가 발생하지 않았을 때 실행되는 블록
    print("파일을 성공적으로 열었습니다.")
finally: # 예외 발생 여부와 상관없이 항상 실행되는 블록
    print("파일 열기 시도 종료.")