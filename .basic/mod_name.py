
def info():
    print("현재 __name__: ", __name__) # __name__은 현재 모듈의 이름을 나타내는 특별한 변수입니다. 모듈이 직접 실행될 때는 __name__이 "__main__"으로 설정되고, 다른 모듈에서 import될 때는 __name__이 해당 모듈의 이름으로 설정됩니다. 따라서, info() 함수를 호출하면 현재 모듈의 이름이 출력됩니다.
    
info()

if __name__ == "__main__":    
    print("이 모듈은 직접 실행되었습니다.")
else:
    print("이 모듈은 다른 모듈에서 import되었습니다.")