a = int(input("Enter the 1st lenght: "))
b = int(input("Enter the 2nd lenght: "))
c = int(input("Enter the 3rd lenght: "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(area)