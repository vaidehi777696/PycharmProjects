'''file=open('text','r') #reading data from file is avaliable in current directory.
c=file.read()
print(c)'''

#reading data from file where file from specific loction destop
'''file2=open('C://Users//KOMAL//OneDrive//Desktop//textfilepyth.txt','r')
c1 = file2.read()
print(c1)
#if we wont to read only a specific number if bytes from we can pass the number of bytes as
c1=file2.read(10)
print(c1)
#we can also read a single line from file using readline method
c1=file2.readline()
print(c1)
#close file after close method can 
file2.close()
#writing data to a file
#to write a file using python you can the built-in open function and call its write method.
file2=open('C://Users//KOMAL//OneDrive//Desktop//textfilepyth.txt','w')
c11=file2.write("this is ")'''


#3=file2.write("\n741524522524552155211025252")

#print(c3)


#file2=open('')

'''file=open('text','w')
c=file.write('this a taxt')
print(c)
file.close()

file2=open('C://Users//KOMAL//OneDrive//Desktop//testfile.txt','r')
c1=file2.read(1)
print(c1)

c1=file2.read(5)
print(c1)

file2=open('C://Users//KOMAL//OneDrive//Desktop//testfile.txt','w')
c1=file2.write('59698996')
print(c1)
c1=file2.write("\n45829685652669")
print(c1)'''

'''with open('text','r') as file:
    c=file.readline()
    print(c)

with open('text','r') as file:
   c1=file.readlines()
for x in c1:
        print(x)'''
'''#strip method
text="    hello world   "
new_text=text.strip()
print(new_text)

text="   hello world  !"
new_text=text.lstrip()
print(new_text)


text="!  hello word"
new_text.rstrip()
print(new_text)'''


#write data to file
'''with open('name','a') as file:
    name=input("enter your name")
file.write(name+'\n')'''


'''while True:
    with open('name.xt', 'a') as file:
        name = input("enter your name")
        file.write(name + '\n')
        choice=input("do you want to enter name? (y/n")
        if choice=='n':
            break'''

'''with open('name.txt','r') as file:
    lines=file.readlines()
for line in lines:
    print(line.strip().capitalize())'''

'''file=open('name','r')
c=file.readlines()[-1]
print(c)


file=open('text','r')
c=file.read()
print(c)'''
def name(fname):
     with open('name.xt','r')as file:
          x=file.read()
          print(x)
name(name)
