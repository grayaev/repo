from functools import reduce
list=[el for el in range(100,1001) if el%2==0 ]
print(list)
print(reduce(lambda x, y: x * y, list))