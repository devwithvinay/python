# Variables  = A container which contains some values - "String" , Integers , Float , Boolean 
 
               #Each varibles Should have unique name.


#Strings
first_name = "Vinay"   
email = "vinay@dev.com"
food = "pizza"
#String variables also use single quotes
print(first_name)
print(f"I like {food}")
print(f"Hello {first_name}")
print (f"my email is {email}")

#Integers

age = 22
quantity = 3
num_of_students = 30

print(f"There are {num_of_students} in my class")
print(f"You are buying {quantity} items")
print(f"You are {age} years old")
print(f"Your class has {num_of_students} students")

#Float  

price = 10.23
cgpa = 8.23
distance = 5.5

# it contains decimal numbers

print(f"The price is ${price}")
print(f"My cgpa is: {cgpa} ")
print (f"You ran {distance}KM")

#Boolean 

is_student = False
for_sale = True
is_graduate = True

print(f"I am a Student {is_student}")
print(f"Now I am Graduated {is_graduate}")

if is_graduate:
    print("yes I am graduated")
else:
    print("I am Not Graduated")

if for_sale:
    print("Item is for sale.")
else:
    print("Item is NOT Availabel")    

