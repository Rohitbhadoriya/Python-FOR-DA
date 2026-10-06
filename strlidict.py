# maan lo ek restro aap mujhe uska datastore krna h 
# restroName = "XYZ" this is string 
# restroMenu = {"Pizza": 200, "Burger": 100} this is dictionary
# Menu = ["Pizza", "Burger"] this is list
# stats = {"rating": 4.5, "reviews": 100} this is dictionary



print("=" * 30)
print("Welcome to the Restaurant Data Store!")
print("=" * 30)

restro_name = "Bappu ki kuttiya"
print(f"\nRestaurant Name: {restro_name}")
menu_items = ["BPM","Pannek Tikka","Bappu Special","Dal Makhani"]
print(f"\nMenu Items: {menu_items}")

restr_stats = {
    "total_orders": 150,
    "avg_rating": 4.5,
    "deliver_time": "30 mins",
    "is_open": True,
    "best_selller": "BPM"
}
print(f"\nRestaurant Stats: {restr_stats}")


resrto_data ={
    "name": restro_name,
    "menu": menu_items,
    "stats": restr_stats,
    "revenue" :restr_stats["total_orders"] * 200  # Assuming an average price of 200 per order
}
print(f"\nComplete Restaurant Data: {resrto_data}")

# string mene naame store kiya
# Dict mein stats store kiya
# List mein menu items store kiya

# STRING  =  Human readable text, used for names, descriptions, etc.
# DICTIONARY = Key-value pairs, used for structured data like stats, details, etc
# LIST = Ordered collection, used for items like menu, reviews, etc.
# String se pta chlta h ki "Bappu ki kuttiya" ye restaurant ka name h koi random number nhi h 
# list mein order maintain hota h : jo apne sequence mein add kiya h menu items usi order mein print hoga
# Dictiinary mein aap bestseller dalaoge to turant value mil jati h loop nhi chalna padta 
# Interview question 
# 3 users ka data store karna h
users_data = {
    "user1": {
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com"
    },
    "user2": {
        "name": "Bob",
        "age": 25,
        "email": "bob@example.com"
    },
    "user3": {
        "name": "Charlie",
        "age": 35,
        "email": "charlie@example.com"
    }
}



thisdict={
    "brand":"Ford",
    "electric":False,
    "year":1964,
    "color":["red","white","blue"]
}
print(thisdict["color"])
print(type(thisdict))
thisdict["year"] = 2012
thisdict.update({"year":2028})
print(thisdict)

thisdict1 = dict(name = "Johna", age = 39)
print(type(thisdict1))
print(thisdict1)

thisdict3 = {
    "name":"Rohit",
    "age":29
}
print("sab kuch ok", thisdict3)
thisdict3["city"] = "Gwalior"



thistdict4 = {
"Brand":"Maruti",
"model":"Dzire",
"year":2027

}
thistdict4.pop("Brand")
print(thistdict4)



user = {
    "name": "Alice", 
        "role": "Admin", 
        "status": "Active"
        }

# Removes and returns the last item
last_item = user.popitem()

print(last_item)  # Output: ('status', 'Active')
print(user)       # Output: {'name': 'Alice', 'role': 'Admin'}


user1 = {
"name": "Ram ki amma", 
"role": "aag lgana"
}

key, value = user1.popitem()

print(f"Removed Key: {key}")    # Output: Removed Key: role
print(f"Removed Value: {value}") # Output: Removed Value: Admin

salesItem = {
    "Brand" : "Jockey",
    "Category" : "T-Shirt",
    "Price": 700,
    "Deilvery":True

}
print(salesItem)
salesItem["Price"] = 900
print(salesItem)
salesItem["Stock"] = 900
print(salesItem)
# del salesItem["Deilvery"]
print(salesItem)
# del salesItem
# print(salesItem)
# salesItem.clear()
# print(salesItem)
salesItem1 = salesItem.copy()
print("copy mein kya aya h ye bta rha ", salesItem1)

salesitem3 = (salesItem)
print(salesitem3)
print(type(salesitem3))


# Nested Dict
myfamily = {
    "child1":{
        "name":"Neha",
        "year": 2007
    },
    "child2":{
        "name":"Riya",
        "year":2007
    },
    "child3":{
        "name":"Monika",
        "year":2003
    }
}
print(myfamily)
print(myfamily["child2"]["name"])
print(myfamily["child1"]["year"])



