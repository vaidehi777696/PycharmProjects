class Test:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
    def add(self,a,b,c,d):
        return a+b+c+d
T1=Test()
T1.add(2,3)
T1.add(2,3,4)
T1.add(1,2,3,4)  # one class and method u can pass that time


class Test:
    def add(self,a,b,c=0):
       return a+b+c
T1.Test()
print(T1.add(2,3))

class Test:
    def add(self,*args):
        Total=0

        for I in args:
            Total =Total+I
            return Total
T1=Test()
print(T1.add(2,3))
print(T1.add(2,4,3,4))
print(T1.add(1,2,3,4,5,6))




