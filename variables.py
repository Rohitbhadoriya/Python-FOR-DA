# print("Hello World")
# customer_name = 'Rohit'
# print(customer_name)
# aap order kr rhe isko real world se refer krngey 
# python automatically smjh jata hai => ye number hai or ya integer hai
# automatic detect krne kehte Dynamic Typing 
# order_id = 2366
# customer_name = 'Sneha Singh'
# age = 25
# bill_ammount = 1249.75
# is_delivered = False
# print(order_id)
# print(customer_name)
# print(age)
# print(bill_ammount)
# print(is_delivered)
# print(customer_name,age,bill_ammount,is_delivered)
# yha error ate h 
# order_value = 500  ki ye number h 
#order_value = "500 Rupess"  baad mein hum pt chla ki ye string
# or python mein abi koi error nhi diya 
# warning hai => agar hum galti se number ko text mein badal denge or usem addition karengey to error ayega 
# vairables name rkhne ke rules kya hote h 

# letter or _ se start kr skte h 
# bulk_order = 154
# bulkOrder = 345
# _bulk_order = 123

# errro jab ata h jab wrong way declare krte h 
# 1bulkOrder =  123 ye dega error 
# bulkOrder1 = 123 ye error nhi dega
# Sirf letters , numbers , underscore
# customer_id_1 = 23
# customer_Full_Name = "Rohit Bhadoriya"
# wrong way kya h 
# customer-id = 123 hypher allowed nhai h 
# print(customer-id )
# customer ID = 23 space kre ke bi use nhi kr skte h 
# customer@ID = 34 yha pr @ bi allowed nhi 
# print(customer@ID )
# case sensitive 
# orderid = 2345
# orderId  = 987
# ORDER_ID = 345 yha pr teeno order id lag vaiable h 
# Rule 4 => ki kuch keyword use mt krna wo phele se he reserved h 
# Example => if,else,for,while,def,class,true,False,None
# if = 123
# print(if) yha a gya error kya invalid syntax
# class  = '12th'
# print(class)yha a gya error kya invalid syntax
# clasNAme = 12
# print(clasNAme) ye wala code work kar jayega apko 
#camelCase Syntax => orderName
#Snake_case => order_name
# customer_name = 'Sneha Singh'
# age = 25
# bill_ammount = 1249.75
# is_delivered = False
# print(customer_name,age,bill_ammount,is_delivered) isko boltey snake_case

# DEscriptive naam do => kuch meanining Full Name do
delivery_time = 42
# X = 42 is type ka kbbhi vaibale name use mt kro 
# kbhi bhi single letter use mt kro 
# Consitent rho => apko bilkul proper sturctured follow krna h ki apne agr
# camelCase use kiya ya apne PascalCase use kiya ya snake_case ek he format ko le kar chlna 
# What is Data Type in ptython 
#  python mein datatype kai sare hote h 
# Integers, String, Float, Boolean, None

# customer_name = 'Sneha Singh'
# age = 25
# bill_ammount = 1249.75
# bln = True
# # other_type = ;
# print(type(customer_name))
# print(type(age))
# print(type(bill_ammount))
# print(type(bln))
# # print(other_type)

# 1. Int (int) => Pura Number ka mtlb no decimal value 
# order_id = 433
# items_counts = 5
# delivery_time_minutes = 42
# Decimal nahi hota h 
# +ve -ve zero sab allowed hota h 
# Zomato mein kha use hota h 
# Order ID
# NUmber of items ordered
# DElivery time in mnutes 
# Restro vote count
# cutsomer ratings count (jaise 128 reviews)

# 2. Float Value => Decimal Number 
# bill_amount = 1345.97
# restro_rating = 4.8
# tax_percentage = 3.4
# Paisa , rating , %, GST sab float mein hota h 
# Zomato mein kha use hota h 
# 1. bill Ammount 
# 2. Restro Rating 
# 3. Delievery Distance 
# 4. Discount

bill_amount = 675.65
print(type(bill_amount))
gst  = bill_amount * 0.05
final_amount = gst + bill_amount
print(final_amount)

# 3. String (str) => Text (A to Z, a to z)

customer_name = "     Prachi Desai    "
restro_name = "Bikaner Sweets"
city = 'Bhopal'
bill_amount1 = 1350.98
gst_other = bill_amount * 0.05
final_price = gst_other + bill_amount1
print(final_price)
print(type(customer_name))
# string hum ('' isko single quote) ("" isko double quote ) or hum string ko ese ke wraped krte 
# "Prachi" , 'Prachi
# Zomato mein kese use hua hoga ye 
# customer name  = 'string'
# restro name
# city name 
# Food Items bi string mein lete like Kaju Katli , Churma ka ladooo , Dry Fruiy Sweets, Gondh ka laddu
#  String kuch h method abi kuch method hum dekh lenege baki angey dekngey hum 
print(customer_name)
print(customer_name.strip()) # jo uneccessary gaph tha usko hta diya is strip ne 


# 4. Boolean (Bool) => Sirf ture ya false 
is_delivered = True
is_veg_restro = False
has_discount = False
# restro_rooftop = false age small mein false kr rhe h to wo error create krega 
# Zomato mein kha use hota h 
# 1. is order delivered (True or Flase)
# 2. is online order (True or False)
# 3. is restro Pure veg (True or False)
# 4. is discount applied (True or False)
# 5. is membership (True or False)
#  Jab hum panda bhaiya ka use krnge hum wha kha se dkehe rhe hing eis cheej ko 
# itss_delivered = True
# Pandas df[df[itss_delivered] == True]
itss_delivered = False
print(type(itss_delivered))
if itss_delivered == True:
    print('Order Delivered SuccessFully')
else:
    print("Order Pending")


# TYPE Conversion 
#  Hume kbhi kbhi manually bi btana padta h 
# jo data a rha sab kuch string a rha h 

bill_str = "1234.79"       # ye string h na ki ye number hai 
# bill_str + 100
# print(bill_str)

bill_float = float(bill_str)     #isne yha kya kiya isne mere string float convert kr diya 
print(bill_float + 1000)

rating_str = "4.8"
rating_float = float(rating_str)
final_rating = rating_float + 0.3
# final_rating = rating_str + 0.3   ese krne pr error TypeError: can only concatenate str (not "float") to str
print(final_rating)


#  Common Mistake  & Solutions => Mostly surubar 90% ye wala pattern kr he dete mtlb mistak 
# print(agent_name) ese krne pr error ayega kyu ki apan agent_name defined nhi kia ok 
# ye problem thi but ap kbhi ese use mt krna 
# kyu ki wo type error dega
# ye poor syntax apko type error dega ok smj gye aap
# bill = 100
# tax = 24
# total = bill + tax

# Ye solutions tha 
# bill = '1234'
# bill_fl = int(bill)
# f_c = bill_fl+ 100
# print(f_c)


# StudentName = "Sanjay Dutt"
# print(studentname) agr aap ese use krneg to error ayega kyu ayega kyu k humne jav variable define tab humne Pasacal Case but 
# print krte hum lowercase use kr rhe h 


# Kbhi variable ke name space nhi dena h 

# student Name = "Sanjay Dutt "
# Roll Number  = 320098


# kbhi bhi apko key word use nhi krne h jese ki mein bta chuka like if class else 
# 



