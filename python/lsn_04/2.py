list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
n_list = []
for i in range(len(list1)):
    if 0 > i - 1:
        continue
    elif list1[i - 1] < list1[i]:
        n_list.append(list1[i])
print(n_list)
