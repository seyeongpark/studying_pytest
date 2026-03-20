# 클래스 
# 객체 (object) : 현실 세계의 사물이나 개념을 컴퓨터 프로그램에서 표현한 것. 자신만의 고유한 특성(property)과 고유의 행동(behavior)을 가질 수 있다.
# 속성 (attribute) : 객체가 가지고 있는 고유한 특성이나 상태를 나타내는 변수. 예를 들어, 자동차 객체의 속성으로는 색상, 모델, 연식 등이 있을 수 있다. 멤버변수로도 불린다.
# 메서드(method): 객체가 가지는 행동으로, 객체가 수행할 수 있는 기능이나 작업을 나타내는 함수. 예를 들어, 자동차 객체의 메서드로는 가속하기, 브레이크 밟기 등이 있을 수 있다. 멤버함수로도 불린다.

# 클래스: 객체를 만들기 위한 설계도 또는 틀이다. 클래스는 객체의 속성과 메서드를 정의하는데 사용된다. 클래스를 사용하여 여러 개의 객체를 만들 수 있으며, 각 객체는 클래스에서 정의된 속성과 메서드를 공유한다.
# 인스턴스: 클래스로부터 만들어진 객체를 인스턴스라고 한다. 인스턴스는 클래스에서 정의된 속성과 메서드를 가지고 있으며, 각각의 인스턴스는 고유한 상태를 가질 수 있다.

class 클래스명:
    속성(property) 정의
    행동(behavior) 정의
    
# 클래스 정의
class Car:
    속성 정의 - 예시: color, model, year
    행동 정의 - 예시: accelerate(), brake(), honk()
        
# 인스턴스 생성
my_car = Car() # Car 클래스의 인스턴스인 my_car 객체를 생성한다. 이제 my_car는 Car 클래스에서 정의된 속성과 행동을 사용할 수 있다.
your_car = Car() # Car 클래스의 인스턴스인 your_car 객체를 생성한다. 이제 your_car는 Car 클래스에서 정의된 속성과 행동을 사용할 수 있다.

my_car.color = "red" # my_car 객체의 color 속성을 "red"로 설정한다.
your_car.color = "blue" # your_car 객체의 color 속성을 "blue"로 설정한다.   
print(my_car.color) # my_car 객체의 color 속성을 출력한다. 결과는 "red"가 된다.
print(your_car.color) # your_car 객체의 color 속성을 출력한다. 결과는 "blue"가 된다.

# 클래스의 이름은 대문자로 시작하는 것이 관례이다. 클래스의 이름은 객체의 유형을 나타내며, 일반적으로 명사 형태로 작성된다. 예를 들어, Car, Person, Animal 등이 있다.

# class.py

class CellPhone: 
    def __init__(self, model, factory): #생성할 때 인자를 전달하여 객체를 초기화할 수 있도록 __init__ 메서드를 정의한다. __init__ 메서드는 클래스의 인스턴스가 생성될 때 자동으로 호출되는 특별한 메서드로, 인스턴스의 초기 상태를 설정하는 데 사용된다.
        self.model = model #self.model은 인스턴스의 model 속성을 나타내며, model은 __init__ 메서드의 매개변수로 전달된 값을 나타낸다. 이렇게 하면 객체를 생성할 때 모델명과 제조사를 지정할 수 있다.
        self.factory = factory #self.factory는 인스턴스의 factory 속성을 나타내며, factory는 __init__ 메서드의 매개변수로 전달된 값을 나타낸다. 이렇게 하면 객체를 생성할 때 모델명과 제조사를 지정할 수 있다.
    
    def call(self): #self는 인스턴스 자신을 가리키는 매개변수로, 클래스의 메서드에서 인스턴스의 속성에 접근하거나 메서드를 호출할 때 사용된다. 
        print("전화 걸기")
    def receive(self):
        print("전화 받기")
    def info(self):
        print(f"모델명: {self.model}, 제조사: {self.factory}") # 만약 self를 적지 않는다면, 클래스 변수인 model과 factory를 참조할 수 없게 된다. self를 사용하여 인스턴스의 속성에 접근해야 한다.


p1=CellPhone("m3", "Apple") #생성할 때 인자를 전달하여 객체를 초기화할 수 있도록 __init__ 메서드를 정의한다. __init__ 메서드는 클래스의 인스턴스가 생성될 때 자동으로 호출되는 특별한 메서드로, 인스턴스의 초기 상태를 설정하는 데 사용된다.
p1.info() # p1 객체의 info() 메서드를 호출하여 모델명과 제조사를 출력한다. 

'''
출력값:
모델명: m3, 제조사: Apple
'''

#객체 지향 특징
#1. 캡슐화 (Encapsulation): 객체의 속성과 행동을 하나로 묶는 것을 말한다. 객체는 자신의 데이터를 보호하고, 외부에서 직접 접근하지 못하도록 하는 것이 캡슐화의 핵심이다. 이를 통해 객체의 내부 구현을 숨기고, 객체와 상호작용하는 인터페이스를 제공한다. 멤버 변수를 클래스 안에서만 바꿀 수 있게끔 해주고, 밖에서는 함부로 바꿀 수 없게끔 하는 것이 캡슐화의 예시이다.
class CellPhone: 
    def __init__(self, model, factory, serial_number):
        self.model = model
        self.factory = factory 
        self.__serial_number = serial_number # 시리얼 번호는 외부에서 접근할 수 없도록 캡슐화한다. __serial_number 앞에 __를 붙여서, 시리얼 번호가 외부에서 접근할 수 없도록 한다. 이렇게 하면 시리얼 번호를 보호할 수 있다.
    
    def call(self): 
        print("전화 걸기")
    def receive(self):
        print("전화 받기")
    def info(self):
        print(f"모델명: {self.model}, 제조사: {self.factory}")
        print(f"시리얼 번호: {self.__serial_number}") # 시리얼 번호는 외부에서 접근할 수 없도록 캡슐화한다. 이렇게 하면 시리얼 번호를 보호할 수 있다.


p1=CellPhone("m3", "Apple", "123456789") 
p1.__serial_number="000000000" # 시리얼 번호는 외부에서 접근할 수 없도록 캡슐화한다. 이렇게 하면 시리얼 번호를 보호할 수 있다. 시리얼 번호를 변경하려고 해도, 실제로는 변경되지 않는다.
p1.info() 

#2. 상속 (Inheritance): 기존의 클래스를 기반으로 새로운 클래스를 만드는 것을 말한다. 상속을 통해 기존 클래스의 속성과 행동을 재사용할 수 있으며, 새로운 클래스에서 추가적인 속성과 행동을 정의할 수 있다. 이를 통해 코드의 재사용성과 유지보수성을 높일 수 있다. 이 기능을 그대로 가져가서, 새로운 무언가를 만들고 싶을 때, 상속을 쓴다. 상속을 통해 기존 클래스의 속성과 행동을 재사용할 수 있으며, 새로운 클래스에서 추가적인 속성과 행동을 정의할 수 있다. 이를 통해 코드의 재사용성과 유지보수성을 높일 수 있다. 이 기능을 그대로 가져가서, 새로운 무언가를 만들고 싶을 때, 상속을 쓴다.

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "동물이 소리를 낸다."
    
class Dog(Animal):
    # __init__ 없음 -> 부모 클래스인 Animal의 __init__ 메서드를 자동으로 상속받는다.
    def speak(self):
        return f"{self.name}가 멍멍 소리를 낸다." # speak 메서드를 오버라이딩하여 Dog 클래스에 맞게 동작하도록 한다.

dog = Dog("바둑이") # Dog 클래스의 인스턴스인 dog 객체를 생성한다. 생성할 때 이름을 "바둑이"로 전달한다.
print(dog.speak()) # dog 객체의 speak() 메서드를 호출하여 결과를 출력한다. 결과는 "바둑이가 멍멍 소리를 낸다."가 된다.


#3. 다형성 (Polymorphism): 동일한 인터페이스를 사용하여 서로 다른 클래스의 객체를 다룰 수 있는 능력을 말한다. 다형성을 통해 같은 메서드 이름을 사용하여 서로 다른 클래스의 객체에서 다른 동작을 수행할 수 있다. 이를 통해 코드의 유연성과 확장성을 높일 수 있다. 함수이름이 같아도, 부모한테서 상속 받은 자식 클래스에서, 함수의 내용이 달라질 수 있다. 이게 다형성의 예시이다. 함수이름이 같아도, 부모한테서 상속 받은 자식 클래스에서, 함수의 내용이 달라질 수 있다. 


class Animal:
    def __init__(self, name):
        self.name = name
    
class Dog(Animal):
    def info(self):
        return f"{self.name}이가 소리를 냅니다."

dog = Dog('초코')
dog.name = '사랑'

print(dog.info())

class Cat(Animal):
    def __init__(self, name, colour):
        super().__init__(name) # 부모 클래스인 Animal의 __init__ 메서드를 호출하여 name 속성을 초기화한다. 이렇게 하면 Cat 클래스에서 name 속성을 사용할 수 있다.
        self.colour = colour # Cat 클래스에서 colour 속성을 추가로 정의한다. 이렇게 하면 Cat 클래스에서 colour 속성을 사용할 수 있다.
    def info(self):
        return f"{self.colour} {self.name}이가 소리를 냅니다."

cat = Cat('나비', '흰색')
print(cat.info())