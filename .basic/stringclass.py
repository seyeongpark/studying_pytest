#문자열

# 문자를 나열해 놓은 형태
# 작은 따옴표, 큰 따옴표, 세 개의 작은 따옴표, 세 개의 큰 따옴표로 표현할 수 있다.
# 작은 따옴표로 표현한 문자열
a = 'Hello, World!'

# 큰 따옴표로 표현한 문자열
b = "Hello, World!"

# 긴 문자열(여러줄)은 """, '''로 표현할 수 있다.
# 세 개의 작은 따옴표로 표현한 문자열
c = '''Hello, World!'''
# 세 개의 큰 따옴표로 표현한 문자열
d = """Hello, World!""" 

# +, *, [] 연산자를 사용할 수 있다.
# 문자열을 더할 때는 + 연산자를 사용한다.
e = a + b

# 문자열을 반복할 때는 * 연산자를 사용한다.
f = a * 3

# 문자열의 특정 위치의 문자에 접근할 때는 [] 연산자를 사용한다.
g = a[0]  # 'H'
h = a[7]  # 'W'
i = a[-1]  # '!'


# 문자열 함수

# 문자열.strip(), 문자열.lstrip(), 문자열.rstrip()
# 문자열의 양쪽 공백 제거, 왼쪽 공백 제거, 오른쪽 공백 제거
text = "   Hello, World!   "  
print(text.strip())  # "Hello, World!"

# 문자열.upper(), 문자열.lower()
# 문자열을 모두 대문자로 변환, 모두 소문자로 변환
text = "Hello, World!"
print(text.upper())  # "HELLO, WORLD!"

# 문자열.replace(old, new)
# 문자열에서 old를 new로 대체
text = "Hello, World!"
print(text.replace("World", "Python"))  # "Hello, Python!"

# 문자열.split(separator)
# 문자열을 separator로 나누어 리스트로 반환
text = "Hello, World!"
print(text.split(", "))  # ["Hello", "World!"]

# 문자열.find(substring)
# 문자열에서 substring이 처음으로 나타나는 위치의 인덱스를 반환, 없으면 -1 반환
text = "Hello, World!"
print(text.find("World"))  # 7
print(text.find("Python"))  # -1

# 문자열.count(substring)
# 문자열에서 substring이 나타나는 횟수를 반환   
text = "Hello, World! Hello!"
print(text.count("Hello"))  # 2

# 문자열.index(substring)
# 문자열에서 substring이 처음으로 나타나는 위치의 인덱스를 반환, 없으면 ValueError 예외 발생
text = "Hello, World!"
print(text.index("World"))  # 7
# print(text.index("Python"))  # ValueError 예외 발생

# 문자열.startswith(prefix), 문자열.endswith(suffix)
# 문자열이 prefix로 시작하는지, suffix로 끝나는지 여부를 반환
text = "Hello, World!"
print(text.startswith("Hello"))  # True
print(text.endswith("!"))  # True