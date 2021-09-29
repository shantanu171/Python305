
# ex: 5 * 4 * 3 * 2 * 1 = 120    ------->> Revers method

def factorial(n):
    # if (n==0 or n==1):
    #     return  1
    # else:
    #     return n * factorial(n-1)

#    ternary operator
    return 1 if(n == 0 or n == 1) else n * factorial(n-1)

num = int(input("Enter the number: "))
print(f"Factorial of {num} is {factorial(num)}")