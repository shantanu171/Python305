def gcd (x,y):
    gcd = 1
    if x % y ==0:
        return y
    for k in range(int(y/2),0,-1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd
x = int(input("Enter the value of X: "))
y = int(input("Enter the value of Y: "))
print(gcd(x,y))