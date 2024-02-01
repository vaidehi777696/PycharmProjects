def save_userdata():
    name=input("enter the name:")
    roll_no=int(input("enter the roll no:"))
    email=input("enter the email:")
    contact=input("enter the contact:")

    user_data=f"Name:{name}\nRoll_no{roll_no}\nEmail{email}\nContact{contact}\n\n"

    with open('user_data.txt','a')as file:
        file.write(user_data)

save_userdata()

def read_userdata():
    with open('user_data.txt','r')as file:
        print(file.read())
read_userdata()
