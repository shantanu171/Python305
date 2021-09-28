# BMI = Weight/(height)^2     h = meters


height = float(input("Enter the Height: "))
weight = float(input("Enter the Weight: "))
BMI = weight/(height/100)**2
print(f"Your BMI is: {BMI}")