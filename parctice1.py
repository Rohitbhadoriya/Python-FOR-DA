# integar Types
order_id = 78456
customer_id = 108
items_count = 4
delivery_time_minutes = 42
# Float Type value
bill_amount =763.95
gst_percentage = 5.5
delivery_charge = 25.0
restro_rating = 4.0

# String Types
customer_name = "Virat Kholi"
restro_name = "Bikaner Sweets"
city = "New Delhi"
food_items = "Kaju Katli, 2chole Baturey, Cold Drink"
 

#  Boolean Type

is_delivered = True
is_online_order = True
is_discount_applied = True

gst_amount = bill_amount * (gst_percentage/100)
# print(gst_amount)
final_amount = bill_amount + gst_amount + delivery_charge
print("="*50)
print("Swiggy Order Summary")
print("="*50)
print("Order ID:", order_id)
print("Customer:", customer_name)
print('Restaurant:', restro_name)
print("City:", city)
print('Food Items:', food_items)
print('Total Items:', items_count)
print('Bill Amount:', bill_amount)
print("GST({}%):₹".format(gst_percentage),round(gst_amount,2))
print('Delivery Charge:', delivery_charge)
print("Toal Amount:₹",round(final_amount,2))

# INter view Question 

# What is variable: Variable ek named memory location hai jisme hum data store krte h 
# Python mein hmein type btane ki zuruat  nhi pdti h kyuki python Dynamically typed hai 


#  Data Types Kya Hote hain: Data Types Batate hain ki variable mein kis type data h 
# store hai ;. Data analyst ke liye hota hai sabse imp : Integer(pura number) , Float (Decimal value)
# String (Text = > A to Z , a to z) , aur Boolean (True/False)

# Variable Name mein  Space kyu nhi use kr skte hai: Python space ko alg token ka separator
# smjhta h. Agr hum spase use krnge to python smjhega  ki do alg variables hai 


# String Ko Integer mein kaise convert krte hai : neeche diya h example
# bill =  "1234"
# int_value = int(bill)
# print(int_value + 123)
# 