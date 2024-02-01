class Product:
  quantity=20 #this is a class atribute is ramaing same for every object
p1=Product() #creation of object
print(p1)
print(p1.quantity)


#self means
class Product:
    quantity=10
    def __init__(self,name,price,colour):
     self.name=name
     self.price=price
     self.colour=colour
p1=Product('iphone',50000,'purple')
print(p1.name)
print(p1.price)
print(p1.colour)
p2=Product('led',60000,'black')
print(p2.name)
print(p2.price)
print(p2.colour)


class Product:

    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour


    def summer_discount(self):
     self.price=self.price-self.price*5/100
    def winter_discount(self):
        self.price=self.price-self.price*10/100
p1=Product("tv",35000,"black")
print(p1.price)
p1.summer_discount()
print(p1.price)

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def calculate_circle_area(self):
        return 3.14*self.radius*self.radius


    def calculate_parametar(self):
        return 2*3.14*self.radius
radius=float(input("enter the number"))
p1=Circle(radius)
p1.calculate_circle_area()
print(p1.calculate_circle_area())
p1.calculate_parametar()
print(p1.calculate_parametar())


class Parson:
    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth=date_of_birth

    def calculate_age(self):
        today=7.2023()
        age=today.year-self.date_of_birth
        if today<age(today.year,self.date_of_birth.month,self.date_of_birth.day):
            age-=1
            return age
p1=Parson("vaidehi","india",(2000,3,9))
print(p1.name)
print(p1.country)
print(p1.calculate_age)



class Calculater:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self,a,b):
        print(a+b)


    def sub(self,a,b):
        print(a-b)

    def division(self,a,b):
        print(a/b)
p1=Calculater()
p1.add(7,4)
p1.sub(2,5)
p1.division(2,4)