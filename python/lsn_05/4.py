'''
    Создать (программно) текстовый файл, записать в него программно
    набор чисел, разделенных пробелами. Программа должна
    подсчитывать сумму чисел в файле и выводить ее на экран.
'''

def summary():
    try:
        with open('4.txt', 'w+') as f_s:
            line = input('Введите цифры через пробел \n')
            f_s.writelines(line)
            numb = line.split()

            print(sum(map(int, numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()