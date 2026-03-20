# 1. 실제 동작하는 로직 함수 (이름에서 test_를 제거하여 픽스처 오해 방지)
def check_number(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"

# 2. pytest용 테스트 함수 (인자를 받지 않고 내부에서 값을 넣어 검증)
def test_check_number():
    assert check_number(5) == "positive"
    assert check_number(-3) == "negative"
    assert check_number(0) == "zero"

# 3. 직접 실행할 때만 동작하는 부분
if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number: "))
        print(f"Result: {check_number(user_input)}")
    except ValueError:
        print("Please enter a valid integer.")