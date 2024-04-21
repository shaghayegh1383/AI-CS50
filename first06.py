c = ["david", "ali", "barbod", "akbar"]

a = input("Enter a name: ")
c.append(a)
c.sort()
for i in range(len(c)):
    print(c[i])
