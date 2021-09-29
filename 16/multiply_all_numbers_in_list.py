from functools import reduce
num = [1,2,3,4]
# nums_product = reduce((lambda x,y:x*y),num)
a =reduce((lambda x,y:x*y),num)
print(a)