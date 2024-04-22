# While

i = 1
while i < 10:
    print (i)
    i += 1  # important to increment count to avoid an infinite loop
    
i = 1
while True:
    print(i)
    i += 1
    
    if i == 20:
        break
    
    print ("Loop is broken")
    