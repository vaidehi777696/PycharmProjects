import os
os.remove('name.txt')
if os.path.exists('name.txt'):
    os.remove('name.txt')
else:
    print("the file does not exist")
os.remove('name.txt')





