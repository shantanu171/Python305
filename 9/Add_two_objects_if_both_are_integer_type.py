def add_number(a,b):
    if not (isinstance(a,int) and isinstance(b,int)):
        raise TypeError ("Must be Integer")
    return  a + b
print(add_number(1.1,32))