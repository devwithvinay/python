# List [] = mutable (change the elements) , most Flexible ;
# Tuple() = imutable , faster ; 
# set {} = mutable (add/remove) , unordered , No duplicates , best for membership testing

# List []

fruits = ["Apple" , "Banana" , "Orange" , "Coconuts"]

print(fruits) # list of fruits

print(fruits[1]); #indexing :Banana

fruits[1] = "Mango" # change index value
fruits.append("Grapes") #append in last
fruits.remove("Coconuts") # remove the element
fruits.pop(1) #remove element by indexing.
fruits.clear() #remove all elemnts from lists

for fruit in fruits :
    # print(fruit) # print in next line
    print(fruit , end=" ") # same line with space


#Tuples()
# we used (paranthesis) for put elements..
# we cannot add ,remove ,clear because its a immutable 
#but it can be access faster ...


#Sets {}

chai  = {"lemon tea" , "green tea" , "ginger tea" , "masala tea" , "black tea"}
print(chai) # prited all elements but in unordered way

chai.add("herbal tea") #append is not used in set we use add() to add new element
chai.remove("black tea") #remove the element
chai.clear() #remove all elements from set



tea = input("Enter the chai name: ") #user input

if tea in chai :
    print(f"{tea} is found")
else:
    print (f"{tea} is not found")

# if "green tea" in chai :
#     print("green tea is available")
# else:
#     print("its not available")



# dulpicates not allowed , same element print only once .

