def sum(x,y,z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y +z
    return sum
x = int(input("Enter X: "))
y = int(input("Enter Y: "))
z = int(input("Enter Z: "))
print(sum(x,y,z))