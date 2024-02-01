class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        print(f" the name is{self.name}")
        print(f"the rollno is{self.rollno}")

s1=Student("vaidehi",8)
s1.display()

class Student:
    def __init__(self,name,rollno):
        self._name=name
        self._rollno=rollno
    def _display(self):
        print(f"the name is{self._name}")
        print(f"the rollno is{self._rollno}")

class Teachers(Student):
    def __init__(self,name,rollno,marks):
        super().__init__(name,rollno)
        self._marks=marks
    def display(self):
        self._display()
        print(f"the marks is{self._marks}")
t1=Teachers("vaidehi",8,745)
t1.display()

class Student:
    def __init__(self,name,rollno):
        self.__name=name
        self.__rollno=rollno
    def __display(self):
        print(f"the name is{self.__name}")
        print(f"the rollno is{self.__rollno}")
s1=Student("vaidehi",12)
s1.display()


