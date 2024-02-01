#function question
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
result=factorial(6)
print(result)

#palindrome check is given string replace

def is_palindrome(n):
    n==n
    return n==n
word="level"
result=is_palindrome(word)
print(f"{word} is palindrome :{result}")



def is_palindrome(s):
    s=s.replace("","").lower()
    return s==s[::-1]
word="rader"
result=is_palindrome(word)
print(f"{word}is a palindrome:{result}")

#fibonacci series
a,b=0,1
for a in range(10):
    print(a)
    a,b=b,a+b

def fibonacci(n):
    fib_series=[0,1]
    for i in range(2,n):
        fib_series.append(fib_series[i-1]+fib_series[i-2])
    return fib_series
n=10
result=fibonacci(n)
print(result)


#prime or not function


def is_prime(number):
    if number<=1:
        return False
    for i in range(2,number):
        if number % i ==0:
            return False
    return True
num=7
if is_prime(num):
    print(f"{num}is a prime numb")
else:
    print("{num}is not prime numb")
#.square root
import math
def square_root(number):
    return math.sqrt(number)
result=square_root(2)
print(result)

#reverse string 
def original_string(hello):
    return hello[::-1]
result="hello,word"
reverd_string=original_string(result)
print(reverd_string)




