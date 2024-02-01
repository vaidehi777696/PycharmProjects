class Food:
    def type(self):
        print('this is food method')
class Fruit(Food):
    def type(self):
        print("this is friut class")

apple=Fruit()
print(apple.type())
print(apple)

class Food:
    def Hello(self):
        print("how are you")
class Fun(Food):
    def Boy(self):
        super().Hello()
        print("who are you")
s=Fun()
s.Boy()

class Father:
    def sleep(self):
        print("sleep from 10pm-5am")

    def eat(self):
        print("eats breakfast at 9am")
class Son(Father):
    def sleep(self):
        print("sleep from 2am to 10am")

vaidehi=Son()
vaidehi.sleep()
