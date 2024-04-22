try:
    print ("This line works well.")
    print (2 + 2)
    print ( 10 / 0)
    print ( 3 - 2 )
    
except ZeroDivisionError:
    print ("can not divide by zero")
