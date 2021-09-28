def concatenate_list (list):
    result = ''
    for element in list:
        result += str(element)
    return result
print(concatenate_list([1,3,4,'aq','dsa',5,6]))