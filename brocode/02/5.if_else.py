# if Statement = Execute code only if statement is True 
               # they allow for basic decision making
               # ( if , elif , else )

age = int (input("Enter your age: "))

if age >= 18 :
    print("You are an Adult")
elif age<0:
    print("you are not born yet")
elif age>=12 and age<18 :
    print("you are a Teen")

else:
    print("you are a child") 