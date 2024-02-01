'''#logical
cart=[]
item=input("enter value of item that you wont add in cart")
cart.append("items")
print(cart)
#loop
cart=[]
n=int(input("enter the number of item you want to add to cart"))
for x in range(n):
    item = input("enter value of item that you wont add in cart")
    cart.append(item)
     print(cart)
cart=[]
while True:
    choice=input("do you wont add item")
    if choice=='yes':
        item=input("enter value of item that you wont add in cart")
     cart.append(item)
        print(cart)
    else:
        break

products=[{"name":"samartphone","price":40000,"description":"it is nice phone"},
    {"name":"laptop","price":50000,"description":"it is nice laptop"},
    {"name":"headphone","price":80000,"description":"it is nice headphone"},
    {"name":"samrttv","price":50000,"description":"it is nice samrttv"}]
cart=[]
while True:
    choice=input("do you wont continues shoping")
    if choice=='yes':
        print("here is the list of the product along with their price and description")
        for product in products:
            print(f"{product['name']}:{product['description']}:{product['price']}")
        items=input("enter items you wont to add in cart")
        if items==products:
            print("yes you can get this")
        else:
            print("sorry sir,we dont have this product")
            items=input("enter items you want to add in cart")
        cart.append(items)
        print(cart)
    else:
        break
else:
    ("thanks for visiting")
#select the value index
products=[{"name":"samartphone","price":40000,"description":"it is nice phone"},
    {"name":"laptop","price":50000,"description":"it is nice laptop"},
    {"name":"headphone","price":80000,"description":"it is nice headphone"},
    {"name":"samrttv","price":50000,"description":"it is nice samrttv"}]
cart=[]
while True:
    choice = input("do you wont continues shopping")
    if choice == 'yes':
        print("here is the list of the product along with their price and description")
        for index,product in enumerate(products):
            print(f"{index}:{product['name']}:{product['description']}:{product['price']}")
        product_id=int(input("enter the product id that you want to add to cart"))
        cart.append(products[product_id])
        print(f"current cart item are here")
        for product in cart:
            print(f"{product['name']}:{product['price']}")
    else:
        break
print(f"thank you shopping here is the final content of {cart}")'''

products=[{"name":"samartphone","price":40000,"description":"it is nice phone"},
    {"name":"laptop","price":50000,"description":"it is nice laptop"},
    {"name":"headphone","price":80000,"description":"it is nice headphone"},
    {"name":"samrttv","price":50000,"description":"it is nice samrttv"}]

#check if product alread present in cart
cart=[]
while True:
    choice = input("do you wont continues shopping")
    if choice == 'yes':
        print("here is the list of the product along with their price and description")
        for index, product in enumerate(products):
            print(f"{index}:{product['name']}:{product['description']}:{product['price']}")
        product_id = int(input("enter the product id that you want to add to cart"))
            # check if product alread present in cart
        if products[product_id] in cart:
            products[product_id]['quntity']+=1  #in this case increase the quntity of product rather yhan add it to cart
        else:
            products[product_id]['quntity']=1
            cart.append(products[product_id])
          #  code to display the current cart contents,including the name,price,and quntity
            print("here are the ontents in your cart")
            for product in cart:
                print(f"{product['name']}:{product['price']}:{product['quntity']}")
    else:
        break
print(f"thank you shoping here is the final content of cart{cart}")

total = 0
print('here are the contents in your cart:')
for product in cart:
    print(f"{product['name']}:{product['description']}:{product['price']} :quantity:{"quantity"}")
    total+= product['price'] * product['quantity']
    print(f"cart total is:${total}")
else:
     break
