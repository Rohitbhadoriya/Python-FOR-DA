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



# Real DATA Cleaning liye ata 

new_customer_database = ["    ROHIT  ","amit","NEHA    ","      vikash"]
#  clean alll names strip spaces + Title case  (For letter capital)
cleaned_data = [cc.strip().title() for cc in new_customer_database]
print(cleaned_data)



# Common Mistakes Solutions and Debugging
# WRONG
og1 = [1,2,3]
# copyg1 = og1
# copyg1.append(4)
# print(og1)
# ese krne se orhinal list bi change ho rhi h 

# Coorect Way 
copyg1 = og1.copy()
print(copyg1)
copyg1.append(5)
print(copyg1)
print(og1)

#Mistake 2. Index Out Range
billsbhai  = [1200,334,445,556,125,234,386,775]
# index2 = zomato_bills.index(899,1)
# index5 = billsbhai.index(899,7)
# print(index5)
# this is correct way 
# if len(billsbhai) > 7:
#     print(billsbhai[7])
# else:
#     print("Does NOT Exist")


# Mistake 3 Remove() on non-existent value
# billsbhai.remove(20000)
# print(billsbhai)
#  billsbhai.remove(20000)
    # ~~~~~~~~~~~~~~~~^^^^^^^
# ValueError: list.remove(x): x not in list

# correct way
if 20000 in billsbhai:
    billsbhai.remove(20000)
print(billsbhai)



# Mistake 4. sort() return none
# sortbhai = billsbhai.sort()
# print(sortbhai)
# billsbhai.sort()
# print(billsbhai)

# sorted
sortedbhai = sorted(billsbhai)
print(sortedbhai)
print(billsbhai)


# Mistake 5. List as default Argument in function 

def add_order1(forder,forder2=[]):
    forder2.append(forder)
    return forder2
print(add_order1(100))
print(add_order1(200))

def add_order2(forder,forder3=[]):
    forder3.append(forder)
    return forder3
print(add_order2("*"))
print(add_order2("**"))
print(add_order2("***"))
print(add_order2("****"))
print(add_order2("*****"))
# same list resued kr rha h 

def add_order3(forder,forder5=None):
    if forder5 is None:
        forder5=[]
    forder5.append(forder)
    return forder5
print(add_order3(300))
print(add_order3(400))
print(add_order3(500))
print(add_order3(600))

# Mistake 6. Modyfying List While iterating

bill_iterate = [123,445,666,799,899,999,1999]
for bit in bill_iterate:
    if bit > 666:
        bill_iterate.remove(bit)

print(bill_iterate)
#  isme issue skip issue

# Coorect Method
for bit2 in bill_iterate[:]:
    if bit2 > 666:
        bill_iterate.remove(bit2)
print(bill_iterate)

# OR USE list comperhension 
finaloutput = [bit3 for bit3 in bill_iterate if bit3 <= 666]
print("Ye wala print Finaluotput Wale variable", finaloutput)



# Mere pass data a rha  5 ya 6 Thousand
high_value = [highorder for higorder in ogi if higorder[amount] > threshold]
# 


# Inter View Question 


# Q1. List aur Tuple mein Difference kya hota
# Ans: List mutable hai tuple immutable List ko change kr skte h Tuple ko nhi 

# Q2. append() or extend() diiference
# Ans. append ek value add krta hai list mein wo bi last indexing pr, extend ek list ke sare elements add krta hai 

# Q3. List comperhension kya h
# Ans. Ek line mein list prepared krna syntax hai. [expression for item in iterable if conditon] ye syntax h . Fast aur readable hote 


# Q4. List mein remove(), pop(), del() mein difference ?
# Q5. sort() sorted()
# Q6. How to ready shallow copy in list 
# Ans:  listcopy(), list[:], list(list)

