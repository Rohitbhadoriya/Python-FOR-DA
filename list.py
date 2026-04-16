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