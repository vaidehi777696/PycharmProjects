from abstract2 import Vehicle
class Bike(Vehicle):
    def __init__(self,n):
        self.no_of_tyres=n
    def start(self):
        print("start with kick")

class Scooty(Vehicle):
    def __init__(self, n):
        self.no_of_tyres = n
    def start(self):
        print("start with self")

class Car(Vehicle):
     def __init__(self, n):
         self.no_of_tyres = n
     def start(self):
         print("start with key")







