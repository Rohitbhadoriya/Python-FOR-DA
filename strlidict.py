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