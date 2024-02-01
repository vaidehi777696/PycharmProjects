d=int(input("enter the value of numerator"))
n=int(input("enter the value of denomentar"))
try:
 result=d/n
 print(result)
except ZeroDivisionError:
 print("zero division error")

x=int(input("enter the number"))
y=int(input("enter the number"))
c=int(input("enter the number"))
z=int(input("enter the number"))
try:
   c=x+y+z
   print(c)
except NameError:
    print("z value is not defined")
else:
    print(c)
finally:
    print("this block is executed no matter what")
#value error
'''try:
    y = int(input("name"))
    print(y)
except ValueError:
    print("value error")
else:
    print(y)'''
#file not found error
'''def funct():
 try:
    file=open('textt','r')
    c=file.read()
    print(c)
 except FileNotFoundError:
    print("file does not exit")
 else:
    print(c)
 finally:
    print("file is excuted")
funct()'''
#type error
try:
    b=int(input("number"))
    d=int(input("number"))
    result=d/b
    print(result)
except TypeError:
    print("type erro")
#Arithmetic error
def division(a,b):
    try:
        result=a/b
        print(result)
    except ArithmeticError:
        print("arithmetic error")
a=float(input('enter the number'))
b=float(input('enter the number'))
division(a,b)
#Attribute error
def test_listd(nums):
   try:
       r=nums.lengtha
       print(r)
   except AttributeError:
      print("attribute error")
nums=[1,2,3,4,5]
test_listd(nums)