class Parent:
    def __init__(self):
        self.balance=50000

    def dispaly_balance(self):
        print(f"the balance of parent{self.balance}")


class Child:
    def __init__(self):
        self.masg="hello"

    def hello(self):
        print("hello team")

p1=Parent()
p1.dispaly_balance()
c1=Child()
c1.hello()
