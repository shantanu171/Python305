def lcm (x,y):
    if x > y:
        z = x
    else:
        z = y
    while(True):
        if ((z % x == 0) and (z % y == 0 )):
            lcm = z
            break
        z += 1
    return lcm
x = int(input("Enter X: "))
y = int(input("Enter Y: "))
print(lcm(x,y))