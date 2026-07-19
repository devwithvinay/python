# Logical Operators = Evaluate Multiple Conditions ( or , and , not )
                    # or = Atleast one condition is True 
                    # and  = All conditions must be True 
                    # not = Reverse the result , (true =not false  ,false = not true )

# OR   
is_raining = False

temp = int(input("Enter the temperature: "))

if temp > 35 or temp < 0 or is_raining :
    print("The party is cancelled")
else:
    print("The party is on !")

# and 
is_sunny = True 
temp = int(input("Enter the Temperature: "))

if temp >= 30 and is_sunny :
    print("Its Hot outside 🥵")
elif temp <=0 and is_sunny :
    print("Its cold outside 🥶")
elif 28 > temp > 20 and is_sunny:
  print("Its warm outside")
  print("Its sunny outside 😎")
else :
    print("its normal outside")

# not
 
  
    