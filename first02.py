age = int(input("Enter your age: "))
if age >= 18:
    
   print ("You are an adult")
   
   b = input("Are you blind?").lower().strip()
   if b == "yes" or b == "y":
       print ("You can't drive a car.")
       
   elif b == "no" or b == "n":
       print ("You can drive a car.")
       
   else:
       print ("Invalid Input")
       
elif age < 18 and age > 12:
    print ("Tou are a teenager")
    
    
       