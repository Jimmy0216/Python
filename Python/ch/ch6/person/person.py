from abc import ABC, abstractmethod # 추상 클래스 선언방법

class Person(ABC): 
    def __init__(self, name, age, job=None):
        self.name = name
        self.__age = age
        self.job = job

    @abstractmethod
    def introduce(self): # 부모 클래서에서 구현하지않고 자식클래스에서 구현할것
        pass

    def _hello(self):
        print(f"hello, i'm {self.name}, {self.__age} years old!")

    def update_age(self, age):
        if age < 0:
            raise ValueError("나이는 음 수 일 수 없음")
        else:
            self.age = age
            print(f"Now I'm {self.__age} years old.")

# if __name__ == "__main__":
#     man = Person("John", 30)
#     man.hello()
#     man.update_age(31) 

