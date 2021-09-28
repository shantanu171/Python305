str = '17djfjsbhd'
try:
    i = float(str)
except (ValueError,TypeError):
    print("Not numeric")
