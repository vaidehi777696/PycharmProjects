#zero division error
'''a=int(input("enter the number"))
b=int(input("enter the number"))
try:
   result=a/b
   print(result)
except ZeroDivisionError:
    print("zero division error")'''


#value error exception not val

'''try:
    y = int(input("name"))
    print(y)
except ValueError:
    print("value error")
else:
    print(y)'''

#def input(name):
'''try:
   c=int(input("enter the number'''


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


'''try:
    with open('tegi','r') as file:
        file5=file.read()
        print(file5)
except PermissionError:
    print('permission dined open the file')'''

#arithmetic error
def division(a,b):
    try:
        result=a/b
        print(result)
    except ArithmeticError:
        print("arithmetic error")
a=float(input('enter the number'))
b=float(input('enter the number'))
division(a,b)
#attribute error
def test_listd(nums):
   try:
       r=nums.lengtha
       print(r)
   except AttributeError:
      print("attribute error")
nums=[1,2,3,4,5]
test_listd(nums)


a="w3resourse"
print(len(a))












