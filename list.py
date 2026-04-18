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


# count ka use kr rhe h count frequency check krne ke liye use hota h 
#  mtlb ki kitni bar koi order repeat hua h 
order_repeat  = ["Pizza","Burger","Sandwich","Garlic Naan", "Pizza", "Burger" , "Pizza"]
cnt = order_repeat.count("Pizza")
print(cnt)

# sort() kya ascending\desceding  order mein sort krta h 
sort_list = [350,999,1399,2340,675]
sorting = sort_list.sort()
print(sort_list)
# print(sorting) yha none a rha to iska ka mtlb kis sort hume kuch return nhi krta h 
sorting2 = sort_list.sort(reverse=True)
print(sort_list)
# sort() orginal list modifiy kr deta hai 
# ALternate => sorted(list) => nayi sorted return karta hai orginal unchanged rhta h 
sort_list1 =  [350,999,1399,2340,675]
new = sorted(sort_list1)
print("Change list Print:", new)
print("uncahnged list print",sort_list1)



# Reverse 
reverse_bills = [375,775,899,3084]
# ruse = reverse_bills.reverse()
# print(ruse)   
# mtlb ki reverse kuch retrun nhi krta hai 
reverse_bills.reverse()
print(reverse_bills)


# copy()
# List ki shallow copy bna kr deta 
# original list protection dena copy mein change krna 
# backup?
# Original data backup rkhna h 
copy_bills = [450,1300,1490]
backup_bill = copy_bills.copy()
backup_bill.append(2340)
print(copy_bills)
print(backup_bill)
# IMP new = original (List) se copy nhi hoti h 
# Dono same list point krti h
original = [990,888,555]
wrong = original
wrong.append(2340)
print(original)


# Built Funnction inlist 
print(sum(original)) 
print(len(original))
print(max(original))
print(min(original))