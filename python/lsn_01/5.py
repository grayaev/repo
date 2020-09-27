profit = int(input('Введите прибыль '))
costs = int(input('Введите издержки '))
if (profit - costs) < 0:
    print('Фирма отработала с убытком в ', profit - costs, 'р.')
elif (profit - costs) == 0:
    print('Фирма отработала в 0')
else:
    print('Фирма отработала c прибылью ', profit - costs, 'р.')
    print('Рентабельность фирмы ', "%.2f" % ((profit - costs) * 100 / profit), '%')
    workers = int(input('Введите количество сотрудников: '))
    print('Прибыль в расчете на сотрудника составила: ', "%.2f" % ((profit - costs) / workers), 'р.')
