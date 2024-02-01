#decprators are a powerful and flexible feature in python thst allows
#you to modify or extend the behavior of functions or methods without changing their actual code they apply using decorator function
def chocolate():
    print("chocolate")

def decorator(fun1):
    def wrapper():
        print("wrapper up side")
        fun1()
        print("wrapper down side")
    return wrapper
chocolate=decorator(chocolate)
chocolate()


def name():
    print("cart shopping cart")

def decorator(func):
    def wrapper():
        print("add cart")
        func()
        print("exit cart")
    return wrapper
name=decorator(name)
name()