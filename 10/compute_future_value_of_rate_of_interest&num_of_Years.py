amt = float(input("Enter the Amount: "))
interest = float(input("Enter the Interest: "))
years = 3
future_value = amt * ((1 + (0.01*interest))** years)
print(round(future_value))