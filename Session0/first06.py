c = ["david", "ali", "barbod", "akbar"]

a = input("Enter a name: ")
c.append(a) #اسم گرفته شده رو به اخر لیست اضافه میکنه
c.sort()  #بر اساس حروف الفبا مرتب میکنه
for i in range(len(c)): #len طولش یعنی تعداد اسمایی که تو لیسته رو میده
    print(c[i])
