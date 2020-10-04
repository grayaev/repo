def summary(num_str, ex):
    zero = 0
    number1 = []
    for el in range(num_str.count(' ')):
        number1 = num_str.split()
    for i in range(len(number1)):
        if number1[i] != '*':
            zero += int(number1[i])
        else:
            ex += 1
            break
    return zero, ex

lost = 0
ex1 = 0
while ex1 != 1:
    num_str = input('Введите числа через пробел, для выхода введите * : ')
    cost = summary(num_str, ex1)
    lost += cost[0]
    ex1 = cost[1]
    print(lost)
    if num_str == '*':
        break
