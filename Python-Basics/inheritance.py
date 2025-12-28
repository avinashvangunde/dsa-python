
class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car starts")

    @staticmethod
    def stop():
        print("car stops")

#  single inheritance  [parent class -> child class]
class Tata(Car):  
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start()
    

c1 = Tata("sumo","petrol")
print(c1.name)
print(c1.type)

c1.start()
c1.stop()


#  multiple inheritence 

class A:
    a = "Class A"

class B:
    b = "Class B"

class C(A,B):
    c = "Class C"

c1 = C()
print(c1.a)
print(c1.b)
print(c1.c)


