def zp(h_count,h_cost,prem):
    return h_count*h_cost+prem
h_count=int(input('Количество часов: '))
h_cost=int(input('Стоимость часа: '))
prem=int(input('Премия: '))
print(f'Зарплата {zp(h_count, h_cost, prem)}р.')