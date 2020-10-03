def my_func(a, b, c):
    if a > c and b > c:
        print(a + b)
    elif b > a and c > a:
        print(b + c)
    else:
        print(a + c)


a1, b1, c1 = int(input('inter number 1: ')), int(input('inter number 2: ')), int(input('inter number 3: '))

my_func(a1, b1, c1)
