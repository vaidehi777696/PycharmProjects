number=[1,2,3,4,5]
def square(x):
     return x*x
New_list = list(map (square,number))
print(New_list)

#use map function to convert string into as list

numbers=["1","2","3","4","5"]
New_list=list(map(int,numbers))
print(New_list)

#Filter in python

numbers=[1,2,3,4,5,6,7,8,9,10]
odd_number=[]
for i in numbers:
    if i%2==1:
        odd_number.append(i)
print(odd_number)

numbers=[1,2,3,4,5,6,7,8,9,10]
def odd(x):
    if x%2==1:
        return(x)
new1=list(filter(odd,numbers))
print(new1)




def fun1():
    counter=0
    while counter<=10:
        yield counter
        counter=counter+1
V1=list(fun1())
print(V1)

def even(x):
    for i in range(x):
        if i%2==0:
            yield i
v1=list(even(11))
print(v1)





