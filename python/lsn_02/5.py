my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
number = int(input('Inter nember: '))

for el in range(len(my_list)):
    if my_list[el] == number:
        my_list.insert(el + 1, number)
        break
    elif my_list[0] < number:
        my_list.insert(0, number)
    elif my_list[-1] > number:
        my_list.append(number)
    elif my_list[el] > number and my_list[el + 1] < number:
        my_list.insert(el + 1, number)
print(f"текущий список - {my_list}")
