class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def get_data(self):
        self.name=input("enter the product name")
        self.price=input("enter the product price")

    def put_data(self):
        print(self.name)
        print(self.price)

class DigitalProduct(Product):
    def __init__(self, link):
        self.link=link

    def get_link(self):
        self.link = input("enter the link")

    def put_link(self):
        print(self.link)

p1=DigitalProduct("")
p1.get_data()
p1.put_data()
p1.get_link()
p1.put_link()

