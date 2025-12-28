print("OOPS in python")

# class  Student:
#     def __init__(self):
#         print(self)
#         print("creating new student")
#     name = "Virat"

# s1 = Student()
# print(s1)
# print(s1.name)



class Student:

    # default constructor
    def __init__(self):
        pass

    def __init__(self,name=None,runs=None):
        self.name = name
        self.runs = runs

    def welcome(self):
        print("Welcome students to the induction")


    @staticmethod
    def hello():
        print("Hello printed")
    
s1 = Student("Avinash",23)
print(s1.name)

print(s1.welcome())

print(s1.hello())

 


# class Car :
#     color = "blue"

# c1 = Car()
# print(c1.color)

#  __init__ function is used to initialize a constructor in class

 



