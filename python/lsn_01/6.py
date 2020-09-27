start = int(input('Inter start: '))
end = int(input('Inter end: '))
print('1-й день:', start)
cost = 1
while end > start:
    cost += 1
    start = start * 1.1
    print(str(cost) + '-й день:', "%.2f" % (start))
print('Ответ: на', str(cost) + '-й день', 'спортсмен достиг результата — не менее', end, 'км.')
