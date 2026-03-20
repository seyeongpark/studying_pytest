data = "python is a programming language"
print(data.count("p")) # 2 
# 문자열에서 "p"가 나타나는 횟수를 반환한다. 이 경우, "python is a programming language" 문자열에는 "p"가 2번 나타난다. 따라서, data.count("p")는 2를 반환한다.
print(data.find("p")) # 0
# 문자열에서 "p"가 처음으로 나타나는 위치의 인덱스를 반환한다. 이 경우, "python is a programming language" 문자열에서 "p"는 첫 번째 문자이므로, 인덱스 0에 위치한다. 따라서, data.find("p")는 0을 반환한다.
print(data.index("p")) # 0
# 문자열에서 "p"가 처음으로 나타나는 위치의 인덱스를 반환한다. 이 경우, "python is a programming language" 문자열에서 "p"는 첫 번째 문자이므로, 인덱스 0에 위치한다. 따라서, data.index("p")는 0을 반환한다. 만약 문자열에 "p"가 없다면, data.index("p")는 ValueError를 발생시킨다.

# find()와 index()의 차이점은, find()는 찾는 문자열이 없을 때 -1을 반환하는 반면, index()는 ValueError 예외를 발생시킨다는 것이다. 따라서, 문자열에서 특정 문자가 존재하는지 여부를 확인할 때는 find()를 사용하는 것이 더 안전하다.

print(data.replace("python","c#")) # "c# is a programming language"
# 문자열에서 "python"을 "c#"으로 대체한 새로운 문자열을 반환한다

data = "John, 010-1234-5678    "
print(data) # "John, 010-1234-5678    "
print(data.strip()) # "John, 010-1234-5678"
# 문자열의 양쪽 공백을 제거한 새로운 문자열을 반환한다. 이 경우, "John, 010-1234-5678    " 문자열의 양쪽에는 공백이 있으므로, data.strip()은 "John, 010-1234-5678"을 반환한다. 만약 문자열에 양쪽 공백이 없다면, data.strip()은 원래 문자열을 그대로 반환한다.
print(data.split(",")) # ['John', ' 010-1234-5678    ']
# 문자열을 ","를 기준으로 나누어 리스트로 반환한다. 이 경우, "John, 010-1234-5678    " 문자열을 ","로 나누면 ["John", " 010-1234-5678    "]라는 리스트가 반환된다. 따라서, data.split(",")는 ["John", " 010-1234-5678    "]를 반환한다. 만약 문자열에 ","가 없다면, data.split(",")는 원래 문자열을 요소로 가지는 리스트를 반환한다.
