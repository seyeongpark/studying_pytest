print("Hello, World!") # ' 와 ''는 상관없지만, 통일하는 것이 좋다.
print('hi \n', 1)
print('hi \t', 1) # \t는 탭, \n은 줄바꿈

name = 'SP' # 오른쪽에 있는 것은 변수에 값을 할당하는 것, 왼쪽에 있는 것은 변수의 이름
age = 25 # 숫자는 따옴표로 감싸지 않는다. 숫자는 숫자 그대로 사용한다.
print(f'내 이름은 {name}이야') # f-string, 문자열 앞에 f를 붙여서 변수나 표현식을 중괄호 {} 안에 넣어서 사용할 수 있다.
print('내 이름은 {}이야 그리고 나이는 {}이야'.format(name, age)) # format 메서드, 문자열 안에 {}를 사용하고 format 메서드에 변수나 값을 전달하여 사용할 수 있다.

# my_name snake_case, myName camelCase, MyName PascalCase
# snake_case는 단어 사이를 언더스코어(_)로 구분하는 방식

# 특수문자는 _, $만 사용할 수 있다. 숫자로 시작할 수 없다. 파이썬에서는 주로 소문자와 언더스코어(_)를 사용하여 변수 이름을 작성하는 것이 일반적이다. 예를 들어, my_variable, user_name 등이 있다.
# 변수 이름은 의미 있는 이름을 사용하는 것이 좋다. 예를 들어, age 대신 user_age, name 대신 user_name 등을 사용하는 것이 좋다. 이렇게 하면 코드의 가독성이 향상되고, 다른 사람들이 코드를 이해하기 쉬워진다.


