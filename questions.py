# 1 se 50 tak ke even number ka sum nkalo 
total = 0
for i in range(1,51):
    print(i)
    if i % 2 ==0:
        total = total + i
print(total)

# lsite mien kitne number 50 se bde h count
numbers = [20,30,40,50,60,70,80,90,100]
count  = 0
for i in numbers:
    if i > 50:
        count = count + 1
print(count)


# sum nikalo

numbers2 = [12,2,4,5,6,7,8,9,111]
total = 0
for i in numbers2:
    total = total + i
print(total)

# 1 se 100 tak prime number 
for i in range(1,101):
    count = 0
    for ii in range(1, i +1):
        # print("mei ii hu", ii)
        if i % ii ==0:
            count = count +1
    if count ==2:
        print(i)


# kisi number ka fractorial

num = int(input("Enter your number"))
factorial = 1
for i in range(1, num +1):
    factorial = factorial *i
print("fact = ", factorial)
