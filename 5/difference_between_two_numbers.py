def difference(n):
    if n <=17:
        return 17-n
    else:
        return (n-17)*2
n = int(input("Enter the value: "))
print(difference(n))