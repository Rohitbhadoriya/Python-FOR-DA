my_tuple = (1)
print("mein ek int jesa behave kr rha hu", type (my_tuple))
my_tuple2 = 1,
print( "mein apne roop mein dikh rha hu", type (  my_tuple2))

mixed_type = (1,2,3,"Mohan","Mohan",1,2,3,4,5,True)
print(type(mixed_type))
print(mixed_type)


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


listcheck = ["Anchal","Tannu","Unnati","Prachi","Astha","Bhumika"]
check12 = tuple(listcheck)
print(check12)

# From range 
t5  = tuple(range(100,110))
print(t5)


my_tuple = (10,20,30,40,50)
print(my_tuple[0:4])

my_tuple1 = (10,20,30,40,50)
print(my_tuple1[:3])

my_tuple2 = (10,20,30,40,50)
print(my_tuple2[-1:-3])

my_tuple3 = (10,20,30,40,50)
print(my_tuple3[:-3])

my_tuple4 = (10,20,30,40,50)
print(my_tuple4[::-1])
print(my_tuple4[1])
print(my_tuple4[-1])


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

t5 = (123,456,789,987,345,567,555)


numbers = (23,44,57,98,78)
print(min(numbers)) # 23
print(max(numbers)) # 98
print(sum(numbers)) # 300








