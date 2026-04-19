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



print("="*50)
print("List Comprehension ")
print("="*50)
# Ek line mein list banane ka syntax
# Expression (Kya krna hai value ke sath)
# Loop (Kaise loop chalna hai )
# Conditon (option-Filter krna)
# Syntax [expression for item in iterable if condition]
# Whys use 
# Code Short = 5 line ka code ke line mein a jata
# Faster => Pythonke internal Optimization se
# Examples =  From Normal To Compare
# Questions Sabhi bills mein hundred add kro 
# Normal Way
all_bills = [234,761,333,445]
# f_bills = all_bills + 100
# print(f_bills)
# all_newbills = []
# for bills2 in all_bills:
#     all_newbills.append(bills2 + 100)
#     print(all_newbills)

# # List Compare
# all_newbills = [bills1 + 100 for bills1 in all_bills]
# print(all_newbills)

# High Bills Dikhao
# high_bills = []
# for bills3 in all_bills:
#     if bills3 > 234:
#         high_bills.append(bills3)
#         print(high_bills)

# high_bills = [bills3 for bills3 in all_bills if bills3 > 234]
# print(high_bills)

# High bills 50 value add kro 
# result = []
# for bills3 in all_bills:
#     if bills3 > 234:
#         result.append(bills3 + 50)
#         print(result)


result = [bills3 + 50 for bills3 in all_bills if bills3 > 234]
print(result)
order_byme = ["Banana","Apple","Green Salad","Pizza","Burger","Sandwich"]
complimentary_order = [comp1 + "Cold Drink" for comp1 in order_byme ]
print(complimentary_order)
print(order_byme)

category = ["High" if bills4 > 333 else "Low" for bills4 in all_bills]
print(category)
multiplie = [bills6 * 5 for bills6 in all_bills if bills6 > 234]
print(multiplie)


# REal World
zomato_orders1 = [450,1200,899,2340]
with_gst_bill = [bills9 * 1.05 for bills9 in zomato_orders1]
print(with_gst_bill)
avg = sum(zomato_orders1) / len(zomato_orders1)
print(avg)
above_avg = [bills12 for bills12 in zomato_orders1 if bills12 > avg ]
print(above_avg)



# Convert string list to int list
str_bills  = ["1234","443","9876"]
int_bills = [int(x) for x in str_bills]
print(int_bills)


# Extract even index item

even_index = [zomato_orders1[i] for i in range(len(zomato_orders1)) if i % 2 == 0]
print(even_index)


# Nested Array ko sahi krna ho 
matrix = [[1,2,3],[9,8,7],[3,8,6]]
print(matrix)
flat1 = [num for row in matrix for num in row]
print(flat1)
# List comprehension Fast KYU hai 
# Jyunki Ye C level pe execute hota hai . Normal 
# loop Python level pr iteratoion krta mein function call krta hai (append)
# Comperhension mein append internal optixation se hota hai 

print("="*50)
print("String Method")
print("="*50)
# STRING METHODS KYU KI LIST STRING METHOD BHUT USE HOTE hai 
# Zomato Data mein customer_names, cities,restro_names sab string hain inka clean krna pdta 
# STRINGS MOST IMP METHOD FOR DA
#strip() => Extra space remove kr deta hai => " Rohit  " =>"Rohit"
# upper()/lower => Case Uniform karo => "bhopal" => "BHOPAL"
# split => String se list Bnao => "PIZZA,COKE" => ["Pizza","Coke"]
# join() => List se string banao =>["Pizza","Coke"] => "PIZZA"
# replace => Replace => "Kumar" =>"Sharma"
# startwith()/endwith() => Check prefix/suffix => Filter Start with R
# Ab inke examples dekh lete h 
# strip() Method
name = "  Rohit  "
clean_name = name.strip()
print(clean_name)

# upper/lower Method

city = 'bhopal'
print(city.upper())


# split() String To list
food = "Pizza,Naan,Butter Paneer Masala"
food_items = food.split(',')
print(food_items)


# join() list se string
food1 = ["Soya CHaap","BPM","Burger"]
order_Text = " , ".join(food1)
print(order_Text) 

# replace()
phone_number = "+91-1234567890"
clean_phone = phone_number.replace("-","")
print(clean_phone)


# String To List of Characters

word = "ZOMATO"
chars = list(word)
print(chars)


# Split with mutiliple delimitres useing regex (useful)

import re
text = "Bhopal,Indore;    Pune  | Delhi  "
cities = re.split('[,;|]',text)
print(cities)
print([c.strip() for c in  cities])


# Real Life Example Food ED Prop FinTech
raw_customer = [" ROHIT   ","amit","NEHA","   VIKASH        "]
cleaned = [name.strip().title() for name in raw_customer]
print(cleaned)
# HW FOR LOOP SE BI READY KRNA H 


# Common Mistakes and Debugging

# Mistakes 1.
# Wrong Pattern
original12 = [1,2,3]
# copy1 = original12
# copy1.append(4)
# print(original12)

# Correct
copy12 = original12.copy()
copy12.append(4)
print(original12)
print(copy12)



# MISTAKES 2. INDEX OUT OF RANGE
# WRONG WAY
bills32 = [332,223,4334,2222,2222]
# print(bills32[3]). IndexError: list index out of range
# Coorect Way
if len(bills32) > 3:
    print(bills32[3])
else:
    print("Index Doesn't exists")

# MISTAKE REMOVE MEIN 3.
# print(bills32.remove(1200)) ValueError: list.remove(x): x not in list
# corrrect way
if 120 in bills32:
    bills32.remove(120)
    print("There is no value match")
else:
    print(bills32)


# MISTAKE SORT() returns NONE
result45 = bills32.sort()
# print(result45) None
# Correct Way
bills32.sort()
print(bills32)



# List as default argument in Function 

def add_order(order2,orders32=[]):
    orders32.append(order2)
    return orders32
print(add_order(100))
print(add_order(200))
# iske andar kya hua ki usne same list reused kr li 

# Correct

def add_order1(order3,orders34=None):
    if orders34 is None:
        orders34 =[]
    orders34.append(order3)
    return  orders34
print(add_order1(100))
print(add_order1(200))



# Mistake 6: Modifying List While ietrating
for bills34 in bills32:
    if bills34 > 1000:
        # bills32.remove(bills34) => Skipr issuee


# coreect
        for bills35 in bills32[:]:
            if bills35 >1000:
                bills32.remove(bills35)



# OR USE LIST 
bills37 = [bill38 for bill38 in bills32 if bill38 <= 1000]
print(bills37)


# REAL JOB STORy 
# QUESTion Interview mein puch he lete 
# Usme ek baar kaam kiya tha Ek din manager ne 5000 orders ka deta hai inme se top 10 
#  High-vlaue orders nikal kar do 
high_value = [orderxyz for orderxyz in ordertyt if orderxyz['amount'] > threshold]
#  Ek line mein kaam ho gya h 


#



    
