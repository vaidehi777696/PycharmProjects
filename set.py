#set
a={1,2,3,5}
a.add(7)
print(a)





price={10000,20000,30000}
new_price={50000,20000,40000}
price.update(new_price)
print(price)
price.discard(30000)
print(price)
print(len(price))
print(max(price))
print(min(price))