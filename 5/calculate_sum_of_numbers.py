# calculate sum of three numbers if the values are equal then return thrice of their sum

def sum_thrice(x,y,z):
    sum = x+y+z
    if x == y ==z:
        sum = sum*3
    return sum
x = int(input("Enter the value of X: "))
y = int(input("Enter the value of Y: "))
z = int(input("Enter the value of Z: "))
print(sum_thrice(x,y,z))