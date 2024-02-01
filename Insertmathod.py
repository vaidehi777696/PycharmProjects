class Student:
    def __init__(self,name):  #this is an instance variable
        self.name=name

    def hello(self):  #instance mathod
        print(f"my name is {self.name}name")
    def name_length(self):
        print(len(self.name))
s1=Student("vaidehi")
s1.hello()
s1.name_length()

class Student:
    category="python"   #class variable
    category2=".net"
    @classmethod
    def info(cls):
        print(f"this is class method of{cls.category}")
    @classmethod
    def info2(cls):
        print(f"this is class method of{cls.category2}")
Student.info()
Student.info2()

class Student:
    @staticmethod
    def add(a,b):
        print(a+b)



class Parent:
    def __init__(self):
        self.balance=500000

    def display_balance(self):
        print(f"this is parent balance{self.balance}")

class child(Parent):
    pass
mike=child()
mike.display_balance()