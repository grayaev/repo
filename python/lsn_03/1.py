def div_2_arg(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return print('ZeroDivisionError')


first = int(input('inter number: '))
second = int(input('inter number: '))
print(div_2_arg(first, second))
