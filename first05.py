# calculate n!
def fac(n):
    ans = 1
    for i in range (n):
        ans = ans * (n - i)
        return ans

def main():
    u = int(input("Enter a number: "))
    o = fac(u)
    print(f"{u}! = {o}")

main()
