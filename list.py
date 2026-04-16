# How TO create array
daily_orders = []
# print(type(daily_orders))


# 2. Methods Direct values
# bills = [450,1200,899,2340,675,1500]
# print(bills)


# Mixed Types
order = [3422,"Rohit Singh",376.89,True,"New Delhi"]
# print(order)

# List() constructor 
numbers = list(range(10))
# print(numbers)


# Indexing 
# bills = [450,1200,899,2340,675,1500]
# print(bills[0])
# print(bills[2])
# print(bills[-1])
# print(bills(-1)) agr aap ese print kroge TypeError: 'list' object is not callable


# Slice
bills = [450,1200,899,2340,675,1500]

print(bills[1:4])
# is method use krne se first ke three output a rha [450, 1200, 899]
print(bills[:3])

# is method use krne se first ke four output a rha [450, 1200, 899, 2340]
print(bills[:4])

# is method use krne se last ke three a rhe h [2340, 675, 1500]
print(bills[3:])

# even positions mein chl rha h [450, 899, 675]
print(bills[::2])

# mtlb ki poori list copy ho gyi 
print(bills[:])

# [1500, 675, 2340, 899, 1200, 450] reverse chlega
print(bills[::-1])

print("="*50)
print("Methods")
print("="*50)
# append kya krta last mein value add kr deta h list ke andar mltb ki array
daily_bills = [450,737,884]
daily_bills.append(2055)
print(daily_bills)

# Extend() list ke saare elements ko dossre list ke elements ke add krta h
morning_orders = [123,789,932]
evening_orders = [441,576,932]
morning_orders.extend(evening_orders)
print(morning_orders)

# Insert kaya lrta value krta h
orders_restro = ["Pizza","Sandwich","Garlic Naan","Cold Coffe"]
other = orders_restro.insert(0,"Pizza Double Cheese")
print(other)


# remove use kr rha hu jab hume uski positions nhi pta hoti h 
pizza_hut = ['Pizza',"Burger","Garlic Naan","Bread"]
pizza_hut.remove('Burger')
print(pizza_hut)
# if Burger in pizza_hut pizza_hut.remove(Burger)

# pop Kisi index ki value remove krta hai air return bi krta hai 
many_orders = [450,850,975,1200]
print(many_orders)
# yha apne pop use kiya h to usne return bi kiya h 1200
last_order = many_orders.pop() 
print(last_order)
print(many_orders)
# mujhe maan lo indexing ke sath pop uske krna ho 
second_orders = many_orders.pop(1)
print(second_orders)


# clear 
# assigmnet_orders = [123,098,007]
#  agar aap ese isko values denge to error ayega jese meien line number 89 pr diya 
# ye error ayega                             ^
# SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
assigmnet_orders = [123,98,332]
assigmnet_orders.clear()
print(assigmnet_orders)

# Index() hume index ki value btata hai. Value ki first occurreance ka index batata hai 
zomato_bills = [450,375,899,1385,776]
# index1 = zomato_bills.index(899)
# print(index1)
index2 = zomato_bills.index(899,1)
print(index2)



