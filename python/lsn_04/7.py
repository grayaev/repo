def fact(n):
    x=1
    print(x)
    for i in range(1,n):
        x*=i+1
        yield x

#n=int(input('digit: '))
n=-5

for el in fact(n):
    print((el))