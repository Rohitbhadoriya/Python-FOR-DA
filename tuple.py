# Tuple bHaiya kon h 
# Python ka wo immutable superhero jo ek baar ban gya to kabhi badalta nhi h 
# Jaise ki real life => Apka Best Freind 
# Tech Real Life => Tum Zomato tumahre pass order aya use order kya h 
# name : "Shalini", bill₹450, city"Noida"
# Ab data change nhi hoga kyu ki order confrom ho gya h 

# App Developer ho apne isko list mein rkh diya order[1] = 450
# loss compnany higa kyu ki apne bill ke sath change 


# Tuple Kya hai 

# kaisa bnata hai (4 method)

# Accces kese krte hai? Indexing  + Slicing

# Operation => concat, repeat, in , len

# Method  = count index

# Imuutable (DEEP DIVE) = > Yeh SBSE IMP HAI 

# List vs TUPLE 

# Advanced Topic 

# Common mistakes

# Interview Questions  
#  what is Tuple : Tuple ek ordered collection jo immutable hai 
# Ordered: Jo value phele denge wo phele index pr ayegi (0,1,2)
#  immutable: Ek bar ban gya kabhi change nhi kr skte , Na Add, Na Remove , Na update  Sir Tuple list ki tarah  array of pointers hain, lekin fixed size IMP : Tuple ke anadar  refrences hote hain, values nhi , isliye agr jab koi refrence mutable objecte (jaise list)
# ko point kare to wo object change ho skta h lekin tuple ka refrence nhi bndal skta Why Tuples used in python
# 3 main reasons 
 
#  DATA SAFTEY => koi bi galti se change nhi kr skta 
# jaise ki const (Javascript )
# Performance => List se Fasted,(Fixed Size), no-over-allocation 
# Hashbale => Dict ki ban skta h (List nhi bna skta h)

# Key Prpoperties


# Ordered => Index se access(0,1,2)

# immutable => Change nhi kar skte (sealed)

# Duplicates => Same value mutilples time a skti h 
# Heterogeneous => Different type of data ek sath rkh skte h
# Hashable => Dict ki key ban skta h 
# Fixed Size => Ek bar ban gya size increase nhi hoga 


my_tuple = (1,2,3,"apple",2,5.5)
print(my_tuple)
print(type(my_tuple))

# Duplicate Data
dup_tuple = (1,2,3,4,5,2,3)
print(dup_tuple)

# Question => Kya Tuple me duplicate data store kr skte h
# Answer => Haan store kr skte h but access krne pr wo same index pr aayega
# print(dup_tuple[1]) # 2
# print(dup_tuple[5]) # 2


# Creating Tuples with 4 method and common mistakes

# Normal Tuple
t1 = (10,20,30)
print(t1)

# Method 2 . Without Parenthesis (Tuple Packing)
t2 = 40,50,60
print(t2)
print(type(t2))
# Python ke andar jese usne comma dekha to wo smj ki aap tuple bnana chahte ho

# Method 3. Using tuple() constructor
t3 = tuple([70,80,90]) # List ko tuple me convert kr diya
print(t3)

# String ko tuple me convert krna
t4 = tuple("Hello")
print(t4)

# From range 
t5  = tuple(range(100,110))
print(t5)


# empty tuple
empty1 = ()
empty2 = tuple()
print(empty1)
print(empty2)


# Common Mistakes
wrong = (5)  # This is not a tuple, it's just an integer in parentheses
print(type(wrong))  # Output: <class 'int'>

correct = (5,)
print(type(correct))  # Output: <class 'tuple'>

coorect1 = 5,
print(type(coorect1))  # Output: <class 'tuple'>



# (5) Pararenthesis sirf grouping ke liye use hota h, tuple banane ke liye comma zaruri h
# otupt Integar hoga, not tuple
# (5,)

# Real Life Analogy => Single elemnet tuple
# EK plate mein sirf ek samosa h. Plate (Pararenthesis) hain lekin waiter
# ko batana padega ki ek smamosa plate mein => comma whi batata h ki ek he h 


# Section Accessing Elemnets + Slicing

# Indexing (Positive + Negative)
my_tuple = (10,20,30,40,50)
print(my_tuple[0]) # 10
print(my_tuple[2]) # 30
print(my_tuple[-1]) # 50 last wala diya 
print(my_tuple[-3]) # 30 last se 3rd wala diya

# Slicing
# tup[1:4]
print(my_tuple[1:4]) # 20,30,40
print(my_tuple[:3]) # 10,20,30
print(my_tuple[:])   # ye poora copy kr rha h
print(my_tuple[2:])

# Questuion => Slicing se new tuple banta h kya ?
# Ans => Ha banata h original tuple me koi change nhi hoga


# Section 4 => TUPLE OPERTIONS

# Concatenation
t1 = (1,2,3)
t2 = (4,5,6)
result1 = t1 + t2
print(result1) # (1,2,3,4,5,6)


# Repetition
t2 = (7,8)
result2 = t2 * 3
print(result2) # (7,8,7,8,7,8)


# Membership Testing
t4 =("Mango","Banana","Grapes")
print("Banana" in t4) # True
print("Apple" in t4) # False

# Length
print(len(t4))

# Min Max Sum 

numbers = (23,44,57,98,78)
print(min(numbers)) # 23
print(max(numbers)) # 98
print(sum(numbers)) # 300

# Question => Kya hum tuple ke element ko change kr skte h
# Answer => Nahi kr skte h kyuki tuple immutable h
# min() max() sum() sirf numberic tuple allow h 
# agr aap isme string de dene to error aayega => TypeError: '<' not supported between instances of 'str' and 'int'

# Section  => 5 Tuple methods Built ins

# Method 1. count => count battata h ki kitni baar value tuple ayi h 
ctup = (1,2,3,4,2,5,2)
print(ctup.count(2)) # 3
# Method 2. index => index method value ka index return krta h
post = ctup.index(4)
print(post) # 3
# Question => Kya index method duplicate value ke liye kaam krta h
# Answer => Nahi krta h wo first occurance ka index return krta h
# with start end 
post2 = ctup.index(2,3) # 3 se start krke 2 ka index return krna h

# Note Value nhi milta h to error aayega => ValueError: tuple.index(x): x not found
# Bulit Fin Functions For Tuples
# len()=> Length => tuple ke andar kitne element h
# min() => Minimum value => tuple ke andar minimum value kya h
# max() => Maximum value => tuple ke andar maximum value kya h
# sum() => Sum => tuple ke andar jitne bhi number h unka sum kya h
# sorted() => Sorted => tuple ke andar jitne bhi element h unko sorted order me return krta h (List me return krta h)
sorttup = (5,2,8,1,4)
print(sorted(sorttup)) # [1,2,4,5,8]
# Note sorted() method tuple ko change nhi krta h wo sorted order me list return krta h

# Section 6 => IMMUATBILITY DEEP DIVE (Sabse important topic)
# What is immutability => Ek baar tuple ban gya uske andar ki cheezein ko badal nhi skte h
# 

# tup12 = (1,2,3,[4,5],6)
# print(tup12)
# Question => Kya hum tuple ke andar list ko change kr skte h
# Answer => Haan kr skte h kyuki tuple ke andar list ka reference h,
tup12 = (1,3,5,6,7,8,9)
# tup12[1] = 30
# print(tup12) # TypeError: 'tuple' object does not support item assignment
# tup12.aapend(45) # AttributeError: 'tuple' object has no attribute 'append'
# print(tup12) 
# del tup12[1]
# print(tup12) # TypeError: 'tuple' object doesn't support item deletion

# What can changed 
tup14 = (23,45,[1,2,3],78,98,88)
# Ye allowed hai 
tup14[2][0] = 99
print(tup14) # (23, 45, [99, 2, 3], 78, 98, 88)
# Yw bi allowed hai
tup14[2].append(100)
print(tup14) # (23, 45, [99, 2, 3, 100], 78, 98, 88)

# Ye cheej allowed nhi h kyu ki aap iska reference change krne ki koshish kr rhe h
# tup14[2] = [6,7,8]
# print(tup14)

# Tuple ke refrence [ref3] huemsah same list ko point karega 
# Lekin us list ke andar ki value ko change nhi krta h 

# Why immutability important h
# Data integrity => Data ko galti se change nhi kr skte h
# Performance => Immutable objects faster hote h kyuki unka size fixed hota h
# Hashability => Immutable objects hashable hote h, isliye unko dict ke key ke roop me use kiya ja sakta h
# Thread safety => Immutable objects thread-safe hote h, kyuki unka state change nahi hota hai, isliye multiple threads unko safely access kar sakte hain without any synchronization mechanism.

# Tupple immutable hai to yesh kaise kaam gya? tup = (1,2,3), tup = (4,5,6)
# 
tup45 = (2,3,4);
tup45 = (5,6,7)
print(tup45) # (5,6,7)  
# BBhaiya yha esa h ki , Tuple change nhi hua h Tumne naya tuple banaya hai 
# aur tup45 variable ko naya tuple ka reference de diya hai
# ORiginal tup45 memeori waise he save h => Garbage COlleection 



# List VS TUPLE
# Mutable => List hoti hai , Tuple immutable hoti hai
# Syntax => List => [] , Tuple => ()
# Menory => List zyada memory leta h , Tuple kam memory leta h
# Performance => Tuple faster hote h , List slower hote h
# Methods => List Many (append, extend, insert, remove, pop, sort, reverse), Tuple Few (count, index)
# Dict Key => List unhashable hote h , Tuple hashable hote h
# Use Cases => List => Dynamic data, Tuple => Fixed data

# Memory Comparison
import sys
list1 = [1,2,3,4,5]
tuple1 = (1,2,3,4,5)
print("Size of list:",sys.getsizeof(list1)) # 96 bytes
print("Size of tuple:",sys.getsizeof(tuple1)) # 80 bytes
# Diagram => List ke andar 5 element h , Tuple ke andar 5 element h , List zyada memory leta h kyuki wo mutable h , Tuple kam memory leta h kyuki wo immutable h


# speed comparison
import timeit
list_time = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)
print("List creation time:", list_time) # 0.1 seconds
print("Tuple creation time:", tuple_time) # 0.05 seconds

# Kba tuble use krna chaiye 

# Fixed data => Coordinate, RGB Colors, constant values

# Dict Key => Need hashable key => Tuple use krna chaiye
# Function return multiple values => name age city => Tuple use krna chaiye
# Data integrity    => Large or Fixed Data Processing
# Performance critical code => Team mein koi galti se edit nhi kr ske 

# Kab list use krni chaiye 

# Dynamic data => User input, Data that changes over time
# Same Type collection => List use krna chaiye
# Need sorting and modication => List use krna chaiye
# Uncertain size => Jab hume pata nhi hota ki kitna data store krna hoga to list use krna chaiye


# Zomato ke lie program ban rhe h 
# Tuple use kr rhe h kyu ki order ke data ko change nhi krna h
resto_locations = ("Rajiv Chowk A Block","Noida","Gurgaon","Faridabad")
order_status = ("Order Placed","Preparing","Out for Delivery","Delivered")
# List 
menu = ["Pizza","Burger","Pasta","Salad"]
daily_specials = ["Paneer Butter Masala","Dal Makhani","Chole Bhature"]
daily_specials.append("Rajma Chawal")


# Advanced Topics 
# Tuple Packing and Unpacking 

# Packing => Multiple values ko ek tuple me pack krna
packed_tuple = 1, "Hello", 3.14
print(packed_tuple) 
print(type(packed_tuple)) # <class 'tuple'>

# Unpacking => Tuple ke andar ke values ko alag alag variables me unpack krna
x,y,z = (10,20,30)
print(x,y,z)
print(type(x)) # <class 'int'>

# Real World => Swapping variables
t = 98
u = 100
t, u = u, t     # Swap without temp variable
print("t:", t)  # t: 100
print("u:", u)  # u: 98

# isme hua kya h jo value t me thi wo u me chali gyi aur jo value u me thi wo t me chali gyi
# accha esa kyu hua h 
# esa ish liya hua ki python ne tuple packing and unpacking ka use krke ye swap kr diya h

# Star operator in unpacking
first, *rest = (1,2,3,4,5)
print("First:", first) # First: 1
print("Rest:", rest)   # Rest: [2, 3, 4, 5] list mein aayega kyuki star operator use hua h

first, *middle, last = (10,20,30,40,50)
print("First:", first)   # First: 10
print("Middle:", middle) # Middle: [20, 30, 40]
print("Last:", last)     # Last: 50

#  nested tuple
nested_tuple = (1,2,(3,4),5)
print(nested_tuple) # (1, 2, (3, 4), 5)
# Accessing nested tuple
print(nested_tuple[2])   # (3, 4)
print(nested_tuple[2][0]) # 3

# NamedTuple
# Problem kya phase kr rhe the abi with normal tuple ke sath :
# t[0],t[1] se smjha nhi atat h ki kya hai 
# Solution => NamedTuple => Ek aisa tuple jisme hum field names define kr skte h
from collections import namedtuple
# Define 
Student = namedtuple('Student',['name','age','grade'])
# create
s1 = Student(name="Sachin", age=25, grade='A')
s2 = Student(name="Rahul", age=27, grade='B')
# Access
print(s1.name) # Sachin
print(s1.age)  # 25
print(s1.grade) # A
print(s2.name) # Rahul
print(s2.age)  # 27
print(s2.grade) # B

# Indexing 
print(s1[0]) # Sachin
print(s1[1]) # 25
print(s1[2]) # A
# Why use NamedTuple
# Code Readability => Field names se code zyada readable hota h
# Immutability => NamedTuple immutable hote h, isliye data integrity maintain hoti h
# Memory Efficient => NamedTuple memory efficient hote h, kyuki wo tuple ke roop me implement hote h

# Common Mistakes
# Wrong Way
w = (5)
print(type(w)) # <class 'int'>  Ye tuple nhi h, ye int h
# coorect way
w = (5,)
print(type(w)) # <class 'tuple'>  Ye tuple h, kyuki comma use hua h

# Tuple ko modify krne ki koshish 
tp1 = (1,2,3)
# tp1[1]= 4
print(tp1) # TypeError: 'tuple' object does not support item assignment
# tupple mein cange krna  h 
newtup = (100,) + tp1[1:]
print(newtup) # (100, 2, 3) Ye naya tuple ban gya h, original tuple me koi change nhi hua h
print(tp1) # (1, 2, 3) Original tuple unchanged

# List ko tuple smjh lena 
tup34 = (345,555,[998,778])
# tup34[2] = [111,112]
# print(tup34)         
# TypeError: 'tuple' object does not support item assignment
tup34[2][0] = 111
tup34[2][1] = 112
print(tup34) # (345, 555, [111, 112]) Tuple ke andar list ka reference h, isliye list ke andar ki value change ho skti h,

# Tupel sort krte mistake 
tupsort = (5,2,8,1,4)
# tupsort.sort() # AttributeError: 'tuple' object has no attribute 'sort'
# print(tupsort) # (5, 2, 8, 1, 4) Tuple ke andar sort method nhi h, isliye error aayega

sortedlist = sorted(tupsort)
print(sortedlist) # [1, 2, 4, 5, 8] sorted() method tuple ko change nhi krta h, wo sorted order me list return krta

# Tuple as function default argument
# Tuples as default arguments are safe (immutable)
def process_order(order, statususe=(200,201,400)):
    return statususe
# Ye safe h kyuki default argument tuple immutable h, isliye koi bhi galti se change nhi kr skta h
print(process_order("Pizza")) # (200, 201, 400)
print(process_order("Burger", (500, 501))) # (500, 501) Custom status code pass kr rhe h

# List as default arguments are unsafe (mutable)
def wrong_function(data,cache=[]):
    cache.append(data)
    return cache
print(wrong_function("First Call")) # ['First Call']
print(wrong_function("Second Call")) # ['First Call', 'Second Call']  Ye



# InterView Questions
# 1. List vs Tuple mein Diifference kya h
# Ans=> Lists are mutable and can be modified after creation, while tuples 
# are immutable . List use squre brackets[], tupel use parenthesis() .
# List have more method and consume more memory , while tuples are faster and memory-efficient. Lists cannot be used as dict keys, while tuples can be used as dict keys.

# 2. Tuple ko dic key kyu bana skte ho List ko nhi 
# Ans => Dictionary key must be hashable and immutable. tuples are immutable so theri hash 
# value never changes, making then valid key . List are mutable and cannot be hashed because their content can change

#3. Single elemenet tuple kaise banta h
# Ans (5,)

# 5. Tupel immutable h to ye yeh kaise kaam kr gya t=(4,,5,6); t=(9,8,7)
# Ans: The tuple itself isn't being modified . The variable 
# t is being reaasigned to point a new tuple. The original tuple(4,5,6) remains unchnaged in memeory 

# 4. Tuple ke andar andar list h to kya lisy ko hum change kr skte h 
# Ans:  Yes you can mondifiy the mutable object (list) inside a tuole because the tuple only stores refernces not the actual objects.
# The tuples references remain unchanged, but the mutable object (list) can be modified through its reference. This is a common source of confusion when working with tuples that contain mutable objects.

#6. Tuple faster kyu hoti list se 
# Ans => Tuples are immutable so python can allocate exact memory with-out over allocating for future growth.
# List accolate extra spaced for append operations. Tuples als have less overhead in method lookups 

# 7. a, b = b, a kaise kaam krta hai 
# Ans => python create a tuple (b,a) on the right side (tupel packing), then unpacks 
# it into vairables a and b (tuple unpacking). This allows for elegant variable swapping without needing 
# a temporary variable. The immutability of tuples ensures that the original values of a and 
# b are not modified during the swap process.

# 8. Tuple([1,2,3]) aur (1,2,3) me kya difference h
# Ans: Both create the same tuple (1,2,3) and ([1,2,3]) convert a list to tuple 
# while (1,2,3) is a tuple literal. The literal is slightly faster becasue it doesn't involve the overhead of calling
#  the tuple constructor, but in practice the performance 
# difference is negligible. 
# The main difference is in syntax and readability, with the literal being more concise and c
# commonly used for creating tuples directly.

# 9. tuple compherension hoti h kya python
# Ans => No Python doesn't have tuple compherenesion . using (x for x in range(5)) create a generator expression not a tuple. 
# To create a tuple from compherension use tuple(x for x in range(5))

# 10. Real Project me Tubper kan prefer kroge 
# Ans => When data is fixed (cordinate, RGB COLOR, values, constants)
# when we returning multiple values from functions, when use dictionary 
# keys , when performnace is critical and when data intergrity is imp (preveneting accidental changes)

# 11. namedTuple kya hota 
# Ans=> NamedTuple is a factory function from the collections module that create tuple subclasses with names fields. It provides readable attribute access like point.x instead of point[0]
#  while maintaing tuple immutability 

# 12. Tuple ka size kaise check krte h
# Ans => Use sys.getsizeof() function from the sys module to check the size of a tuple in bytes. For example, sys.getsizeof((1,2,3)) will return the memory size of the tuple (1,2,3). Note that the size may vary based on the Python implementation and the contents of the tuple.

# 13. Tuple ke andar tuple h to usme se value kaise access krte h
# Ans => Use nested indexing to access values in a nested tuple. For example, if you have a tuple like nested_tuple = (1,2,(3,4),5), you can access the inner tuple (3,4) using nested_tuple[2], and then access individual elements like nested_tuple[2][0] for 3 and nested_tuple[2][1] for