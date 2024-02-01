class A:
    def method_a(self):
        print("method of class a")

class B:
    def method_b(self):
        print("method of class b")

class C(A,B):
    def method_c(self):
        print("enter the method c")

cobject=C()
cobject.method_c()
cobject.method_b()
cobject.method_a()


class A:
    def method_a(self):
        print("method of class a")

class B(A):
    def method_b(self):
        print("method of class b")

class C(B):
    def method_c(self):
        print("method of class c")

cobject=C()
cobject.method_a()
cobject.method_b()
cobject.method_c()
