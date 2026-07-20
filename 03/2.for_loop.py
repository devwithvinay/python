# For Loop : A for loop used to iterate over a sequence (String  , list , tuple , set )
#           Repeat a block of code an adjact amout of times , but in while it can run infinite times..

for i in range (1,11): # the 11 is not included.
    print(f"count {i}")

for i in range (1 , 11 , 3) : #here we increment by 3
    print(f" i = {i}")

name ="Vinay Kumar"

for letter in name :
    print(letter, end = "") # prints each letter of the name on the same line
    
#Countdown project 😂

import time
for i in range (10 ,0,-1):
    print(i)
    time.sleep(1)
print("Happy Birthday Vinay")