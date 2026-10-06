# lis2345 = ["Divya","Himanshi","Umang","Yash","Divya","Umang","Rohit"]
# lis2345.remove("Divya")
# print(lis2345)
# pop
# list12 = [1,2,3,4,5,6,7,8,9,9,10,11]
# list12.pop()
# print(list12)
# ret = list12.pop(2)
# print(ret)
# print(list12)


# clear 
# assigmnet_orders = [123,98,332]
# assigmnet_orders.clear()
# print("mein clear hu", assigmnet_orders)



# del
# list13 = [1,2,3,4,5,6,7,8,9,9,10,11]
# del list13
# print(list13)


# zomato_bills = [450,375,899,1385,776,899,450,377,334]
# stre = zomato_bills.index(899,3)
# print(stre)

# count ka use kr rhe h count frequency check krne ke liye use hota h 
#  mtlb ki kitni bar koi order repeat hua h 
# order_repeat  = ["Pizza","Burger","Sandwich","Garlic Naan", "Pizza", "Burger" , "Pizza"]
# cnt = order_repeat.count("Pizza")
# print(cnt)



# sort() kya ascending\desceding  order mein sort krta h 
# sort_list = [350,999,1399,2340,675]
# sorting = sort_list.sort()
# print(sort_list)
# # print(sorting) yha none a rha to iska ka mtlb kis sort hume kuch return nhi krta h 
# sorting2 = sort_list.sort(reverse=True)
# print(sort_list)
# sort() orginal list modifiy kr deta hai 
# ALternate => sorted(list) => nayi sorted return karta hai orginal unchanged rhta h 
# sort_list1 =  [350,999,1399,2340,675]
# new = sorted(sort_list1)
# print("Change list Print:", new)
# print("uncahnged list print",sort_list1)



# Reverse 
# reverse_bills = [375,775,899,3084]
# ruse = reverse_bills.reverse()
# print(ruse)   
# mtlb ki reverse kuch retrun nhi krta hai 
# reverse_bills.reverse()
# print(reverse_bills)



# copy()
# List ki shallow copy bna kr deta 
# original list protection dena copy mein change krna 
# backup?
# Original data backup rkhna h 
# copy_bills = [450,1300,1490]
# backup_bill = copy_bills.copy()
# backup_bill.append(2340)
# print(copy_bills)
# print(backup_bill)
# IMP new = original (List) se copy nhi hoti h 
# Dono same list point krti h
# original = [990,888,555]
# wrong = original
# wrong.append(2340)
# print(original)



# list555 = [1,2,3,4,56.78]
# list777 = [90,10,87,76,75,55]
# list777.extend(list555)
# list555.append(777)
# print(list777)

# original = [990,888,555]
# print(min(original))
# print(max(original))
# print(len(original))
# print(sum(original))
# print(899 in original)

leytnew = []
number = [1,234,456,90.09]
mixeddata = ["Rohit",True,1234,27,]
numbers = list(range(1,10))
print(leytnew)
print(number)
print(mixeddata)
print(numbers)

list123 = [1,2,3,4,5,6,7,89]
print("mein iske length hu", len(list123))
# print(list123[2])
# Slicing
bills = [450,1200,899,2340,675,1500]
print("slice 1:4", bills[1:4])
print(bills[:])
print(":3", bills[:3])
print("3:", bills[3:])
print("mein hu :-1", bills[:-1])
print("mein hu ::-1", bills[::-1])
print("mein hu ::2", bills[::2])
print("mein hu ::3", bills[::3])
