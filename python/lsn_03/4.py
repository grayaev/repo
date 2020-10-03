def my_func(x, y):
    print(x ** y)


def my_func1(x, y):
    z = x
    for i in range(y * -1 + 1):
        z = z / x
    print(z)


x1, y1 = int(input('inter x: ')), int(input('inter y: '))

my_func(x1, y1)
my_func1(x1, y1)
print(pow(x1, y1))
