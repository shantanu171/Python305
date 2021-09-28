def integer_string (str,n):
    result = ""
    for i in range (n):
        result = result + str
    return result
n = int(input("Enter the number for repataion: "))
print(integer_string("abc ",n))
print(integer_string(".py ",n))
