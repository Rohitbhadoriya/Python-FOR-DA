# A function is a block code which only runs when it is called 
# A function can return data as a result 
# A function helping avoiding code reptiton 
# Creating Function
#  In python a function is defined using the def keyword follwoed by a function named 
# Parameteres

def mu_function():
    print("Hello World")

mu_function()

# Function Names
# Function names follow the same rules are variable name in python 
# A function name must start with a letter or underscore
# A function name can only contain letters numbers and underscore
# Function names are case sensitive (myFunction and myfunction are diiffrent)

Name = "Rohit"
name = "Monika"
print(Name)
print(name)
# valid function names
# calculate_sum()
# _private_function()
# myfunction2()



temp1 = 77
celsius1 = (temp1 - 32) *5/9
print(celsius1)
temp2 = 92
celsius2 = (temp2 - 32) * 5/9
print(celsius2)
temp3 = 50
celsius3 = (temp3 - 32) * 5/9
print(celsius3)


def fahrenit_to_celsisus(fahrenheit):
   return(fahrenheit - 32) * 5/9
print(fahrenit_to_celsisus(77))
print(fahrenit_to_celsisus(55))
print(fahrenit_to_celsisus(79))


def day_greeting():
    return "Hello From a function"
print(day_greeting())

# Arguments
# Informtion can be passed into function arguments
# Arguments are specified after the function name inside the parameters. You can add as many
# Argument as you want jus seprate them comma

def anoth_function(fName, lastName):  # parameter h ye 
    print(fName +  " " + lastName)  # yha pr login likha jata yha varibale bi bnna kr krtwe h 
anoth_function("Rohit","Bhadoriya")  # yha pr arguments pass krte h 
def another_function(t,u):
    print(t + " " + u)
anoth_function("t","tyy")

def df_value_passed (name="please enter the name"):
    print("Hello", name)
df_value_passed()
df_value_passed("Rohit")

def defalutCountry(country = "Norway"):
    print("I am From", country)

defalutCountry("Sweden")
defalutCountry()
defalutCountry("India")

# Keyword Arguments
# You can send arguments with key  = value syntax

def key_Arguments(animal,name):
    print("I Have a", animal)
    print("My", animal +  "'s name is",name)
key_Arguments(name="Buddy",animal="Dog",)

# List Pass in function 

def passinglist(fruits):
    for ff in fruits:
        print(ff)
passinglist1 = ["Apple","Orange","Cherry"]
passinglist(passinglist1)

def obejct1(person):
    print("Name:", person["name"])
    print("age:", person["age"])
my_person = {"name": "Monika", "age": 25}
obejct1(my_person)

def  summ(x,y):
    return x + y
# print(summ(5,6))
oo = summ(5,6)
print(oo)

# Function ke andar list ko bi rkh skte h 

def storelist():
    return ["Mohan","Rohit","Archit","Mohit","Souru","Abhishek"]
names = storelist()
print(names[0])