def is_group_number (group_data,n):
    for value in group_data:
        if n == value:
            return True
    return False
n = int(input("Enter the value: "))
print(is_group_number([1,2,3,4,5,23,43,54,6,45],n))