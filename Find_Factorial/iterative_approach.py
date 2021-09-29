# Find Factorial with help of loop
# ex: 1 * 2 * 3 * 4 * 5 = 120    ------>> Forward method


factorial = 1
num = int(input("Enter the number: "))

if num<0:
    print("Factorial does not exist")

else:
     for i in range(1,num+1):
         factorial = factorial * i
     print(f"The fatorial of {num} is {factorial}")