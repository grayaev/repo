d = { 0:'Зима', 1:'Весна', 2:'Лето',3:'Осень'}
list=['Зима', 'Весна', 'Лето', 'Осень']
user=int(input('Введите номер месяца: '))
if user==1 or user==2 or user==12:
    print(d.get(0))
    print(list[0])
elif user==3 or user==4 or user==5:
    print(d.get(1))
    print(list[1])
elif user==6 or user==7 or user==8:
    print(d.get(2))
    print(list[2])
elif user==9 or user==10 or user==11:
    print(d.get(3))
    print(list[3])
else:
    print ('Такого месяца не существует!')
