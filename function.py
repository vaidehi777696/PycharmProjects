# funcation
'''def speed(d=100, t=2):
    s = d / t
    speed(100, 2)
    print(speed)

#static function
def same(a,b):
    a=10
    b-20
    print(a+b)
same(10,20)

#daynamic function
def same(a,b):
    print(a+b)
same(10,20)
same(40,10)

def my_name():
    print("hello ")


my_name()

def speed(d=100, t=2):
    s = d / t
    speed = 100, 2
    print(speed)

speed(100, 2)

def speed(d=100,t=2):
    print(d/t)
speed()

def info():
    print("email")
info()

def speed():
 print("marathi")
 
speed("math")

def info(fruits):
    print(f"is colors "+fruits)
info("apple")'''

def sum(a,b,c=100):
    print(a/b*c)
sum(600,500)
sum(600,400)




 #position parameter/argument
#in a keywordas argument arguments are assigned bsed on the name of the paramenter




'''def info_display(fname, lname):
    print(fname)
    print(lname)


info_display("shrishati", "yadav")
info_display('payal', 'paunkar')

def name(fname,lname):
    print(fname,lname)
name(fname="vzidehi",lname="ullurwar")'''


#deficult argument
'''def name(name="vaidehi"):
    print(name)
name("enmail")
name()
name(123)


def area_circle(r, pi=3.14):
    area = pi * r ** 2
    print(area_circle)


area_circle(2)
area_circle(3)





def greet(name, msg="good morning"):
    print(msg + name)


greet("shristi")

greet("anjali", "good afternoon")


#Arbitary function
def add(*number):
    result = 0
    for x in number:
        result = result + x
    print(result)


add(1, 2)
add(1, 2, 3)


def msg(*msgvalue):
    print(msgvalue)


msg("hello")





#Arbitary keyword arguments
def my_fun(**information):
    for x in information:
        print(f" {x} " + information [x])

my_fun(valitity="20",sam="21",dilt="25")

def my_function(**frustname):
    for x in frustname:
        print(f"clore of fruit  is{x} " + frustname[x])


my_function(bananas="yellow", apple="red", green="guava")

def my_fun(**information):
    for x in information:
        print(f" {x} " + information [x])

my_fun(valitity="20",sam="21",dilt="25")


def info(**fruits):
    print(fruits)
info(banana="yellow",apple="red",gruses="green")

def info(**fruits):
      for x in fruits:
          print(x)
info(banana="yellow",apple="red",gruses="green")'''



#return
'''def add(a,b):
    return a+b
a1=add(10,20)
print(a1)

def add(a,b):
    total=a+b
    return total
def update(total):
     update_value=total + 50
     return update_value
a1=add(10,20)
a2=update(a1)
print(a2)'''

#Calling function to same function directly
def function_a():
    print("function A is executing")
    function_b()
def function_b():
    print("function B is executing")
function_a()



#Local and global variable
total=0
def add(a,b):
    print(a+b) # Local variable is that print function under that is local.
add(10,20)
print(total)

a=10
def sum(a,b):
    c=a*b

    print(c)
sum(10,20)
print(a) #global is that print function after that is global

def example_function():
    x=10
    print("inside the function:" ,x)
example_function #local variable is

total=20
def example_function():
    print(total)
example_function()
print(total)  #global variable

#function definition cannot be empty but if you for same reason have a function definition with no content
#put in the pass satement avoid getthing error
def my_function():
    pass


def square():

 def name_s(string, vowel):
     tota = [each for each in string if each in vowel]

     print(len(tota))
     print(tota)


string = "email"
vowel = "tooda"
name_s(string, vowel);


recursion
#facutoryal
#recursion is a programming concept  where a function calls itself in its own definition it is way solve the problem
#by breaking them down in to smaller
#5=5*4*3*2*1=120
#1=1*1=1
#10*20

def factorial(n):
     n==1
     return 1
result=factorial(1)
print(result)


def factorial(n):
   if n==1:
       return 1
   else:
       return n*factorial(n-1)
result=factorial(6)
print(result)






