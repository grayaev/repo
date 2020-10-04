def del_ind(list_1):
    for el in list_1:
        x=list_1.count(el)
        if x>1:
            for i in range(x):
                list_1.remove(el)
    return list_1
list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(del_ind(list_1))