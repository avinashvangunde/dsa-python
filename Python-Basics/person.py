print("private method")


# changing name of the variable in parent class
class Person:

    name = "Anonymous"

    def __hello(self):    
        print("Welcome hello")
    
    def welcome(self):
        self.__hello()

    def updateName(self,name):
        Person.name = name
        # self.__class__.name = name

    #  class method decorator 

    @classmethod
    def changeName(cls,name):
        cls.name = name


p1 = Person()
p1.welcome()

print(Person.name)
# p1.updateName("Avinash")
p1.changeName("Avinash")
print(p1.name)
print(Person.name)


