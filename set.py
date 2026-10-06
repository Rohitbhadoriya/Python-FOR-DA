myset = {
    "apple", 
    "Banana" , 
    "cherry"
    }

# sets are used to store multiple items a single variable 
# Set is one of 4 built-in data types in python used to store
# collections of data the other 3 are list Tuple and Dict all with different
# qualities uasage
# Notes : Sets items are unchangeable but you can remove items and add new items
print(type(myset))  
# Se items are unoredred unchangeable and do not allow duplicate values
# Unordered
# Unordered means that the items in a set do no have a defined order
# Set items can appear in a different order every time you use them 
# and cannot be refered by index or key 

# Unchangeable
# Set items are unchangeable meaning ha we cannot change the items after he se has been created 
mysetdup = {
    "Rohit",
    "Monika",
    "Mansee",
    "Kanchan",
    "Rohit"
}
print(mysetdup)
myetsetmixed  = {
    "apple",
    "Banana",
    "Cherry",
    True,
    1,
    2
}
print(myetsetmixed)

myetsetmixed1  = {
    "apple",
    "Banana",
    "Cherry",
    True,
    False,
    1,
    0,
    2
}
print(myetsetmixed1)
print(len(myetsetmixed1))

# Set items Data Types
set1 = {"apple", "Banana", "Cherry"}
set2 = {1, 5, 7, 8, 9}
set3 = {True, False, True}
print(set1)
print(set2)
print(set3)

# Constructor Method
thisset1 = set(("Kanchan","Rohit","Deeksha","Swati"))
print(type(thisset1))
print("Swati" in thisset1)
print("Rohit" not in thisset1)
thisset1.add("Mansee Don")
print(thisset1)

# Update
thiset2 = {"kiwi","Dragon Fruit","Chikoo"}
tropical = {"pineapple","mango","papaya"}
thiset2.update(tropical)
print("mein update hu", thiset2)

# Remove
# To remove an item in a set use he remove(), or he discard() method
removeset3 = {"kiwi","Dragon Fruit","Chikoo", "Kiwi"}
removeset3.remove("kiwi")
print(removeset3)

zintstrdnt = {"Monika","Nishank","Riya","Kanchan","Mansee","Kiran","Monika","Rohit","Riya"}
# zintstrdnt.discard("Monika")
# zintstrdnt.pop()
print(zintstrdnt)
nm1  = {1,2,3,4,5,6,7,8,9,1,2,3}
nm1.pop()
print(nm1)
nm1.clear()
print(nm1)
# del poora delete kr dega or uska refrence khtm kr deta h mtlb ki 
# memory se bi hta deta h 

# => The union() method returns a new set with all items from both setrs
set12 = {"name","age","gender"}
set13 = {"Rohit",25,"Male"}
set14 = set12.union(set13)
print("mein union hu", set14)

set15 = {"name","age","gender"}
set16 = {"rohit",24,"male"}
# set17 = set15 + set16
set17 = set15 | set16
print(set17)
set18 = {"a","b","c"}
set19 = {1,2,3}
set20 = {"jhon","apple","cat"}
set21 = {"amma","apppa","guru","karan"}
myset134 = set18.union(set19,set20,set21)
print(myset134)


# Creating Frozend set
# use the forzenset 
# constructor to create a fronset from any iterable 
xx = frozenset({"apple","banana","cherry"})
print(xx)
print(type(xx))