# 사용자로부터 과일이름과 갯수를 입력 받아서 
# 예) "딸기" , "3" ==> "딸기딸기딸기" 출력

fruit = str(input("과일 이름을 입력하세요: "))
count = int(input("과일 갯수를 입력하세요: "))

print (f'결과: {fruit * count}')