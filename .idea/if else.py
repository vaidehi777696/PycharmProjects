#if else
age=int(input("enter the age" ))
if age>=15:
          print("you are adule")
else:
      print("you are not adule")

marks=int(input("enter marks"))
if marks>=90:
            print("grade A")
elif marks>=70:
               print("Grade B")
elif marks>=60:
              print("Grade C")
elif marks>=50:
               print("Grade D")
A=10
B=12
if a>=5:
      print("A is grater than 5")

elif b>=15:
        print("B is greater than 15")
else:
    print("A is less than 5")

a=2
if a>0:
    print("number is positive")

if int(input):
    print("number is positive")
else:
    print("negative")
marks=67
if marks>=90:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=60:
    print("Grade C")
else:
    print("Grade D")

a=10
b=20
if 10>20:print("a is grater than 20")
else:
    print("a is not grater than b")

age= int(input("enter the age"))
name=input("enter the citizen")
if age>15:
    print("you r adult")
    if "indian":
        print("you r indian")
    elif age<15:
        print("you r not adult")
    elif "tokiyo":
         print("you r not indian")
else:
    print("you r s")


#nested if
user_buy=input("enter items that your purchase")
category=input("enter the category of clothes")
if user_buy=="clothes":
    print("you will get 25% discount")
    if category=='jeans':
        print("you will  get 30% discount")
    elif category=='saree':
        print("you will get 40% discount")
    else:
        print("15% discount on other clothes items")
else:
    print("category other than clothes will not get discount")
#password
password = input("enter the password")
if password == "vaidehi":
     print("right password")
else:
    print("wrong password")
#number
number=float(input("enter the number"))
if number>0:
    print("positive")
elif number==0:
    print("zero")
else:
    print("negative")

for i in range(1,100):
    print(i)