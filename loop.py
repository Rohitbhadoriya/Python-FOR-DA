# A for loop is used for iteration in other programing lang
#  and works more like ietrtaor 
# method as found in other oops lang
# with the for loop we can executes a set of statements once for
# each items  in a list tuple set etc

fruits = ["Apple","Mango","Orange","Kiwi"]
# print(fruits)
# print(fruits)
# fruits = fr
# print(fr)

for x in fruits:
    print(x)
# string method 
for e in "banana":
    print(e)

for y in fruits:
    print(y)
    if  y == "Mango":
        break

for z in fruits:
    if z =="Mango":
        continue
    print(z)


for tt in range(6):
    print(tt)
for ty in range(2,6):
    print("ty",ty)

# ye method is liye use kiya h kiya jab hume 3 chod kr vakue chaiyer hoti ha tab use krte h 
for td in range(2,30,3):
    print("td", td)

for tm in range(10):
    print(tm)
else:
    print("Finally Finsihed")

# user  = int(input("enter your tabel number"))
# for tb in range(1,11):
#     print(user, "x", tb, "=", user * tb)



jk = 1
while jk < 6:
    print(jk)
    jk += 1

jk = 1
while jk <= 6:
    print(jk)
    jk += 1

kk = 1
while kk < 9:
    print(kk)
    if kk ==8:
        break
    kk +=1



tj = 0
while tj < 9:
    tj += 1
    if tj ==8:
        continue
    print("mein ek tj hu", tj)

tu = 3
while tu < 6:
    print(tu)
    tu +=1
else:
    print("match hua to nhi chalega nhi hua to chl jayega ")


kk = 0
while kk < 9:
    kk += 1
    if kk ==3:
        break
        # continue
    print(kk)
fruits12 = ["apple", "banana", "mango", "orange"]

i = 0  # index start karo
while i < len(fruits12):
    print(fruits[i])
    i += 1  # index badhao


fruits = ["apple", "banana", "mango"]

for fruit in fruits:   # Direct item milta hai
    print(fruit)


# For Loop
# Jab aapko kisi collection (list, tuple, string, range) ke har ek item par jaana ho, tab for loop use karte hain.

# Aapko khud index nahi badhana padta.

# Yeh iterable (cheezon ke collection) ke saath 
# kaam karta hai.

# Jab aapko pata ho ki loop kitni baar chalna 
# hai (ya aapko sirf items chahiye, index nahi).
# Kab use kre 
# Jab items ka collection ho (list, range, string)
# Automatic milta hai (agar chahiye toh)
# Infinite loop ka risk Bohot kam (rare)
# Simple aur clean
# for i in range(10):








# While loop
# Jab aapko kisi condition ke true rehne tak loop chalana ho, tab while use karte hain.

# Aapko khud index/counter maintain karna padta hai.

# Yeh condition-based hai — jab tak condition true hai, tab tak chalega.

# Jab aapko nhi pata ki loop kitni baar chalna hai (jaise user input wait karna, ya koi specific event hone tak).
# kab use krna 1. Jab condition ke true rehne tak chalana ho
# Khud maintain karna padta hai
# Zyada (agar increment bhool gaye toh)
# Thoda complex ho sakta hai
# while i < 10: