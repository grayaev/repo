from itertools import count
from itertools import cycle
num=int(input('inter number 0 - 9: '))
for el in count(num):
    if el > 10:
        break
    else:
        print(el)
        
text=input('ВВедите буквы: ')
stop=0
for bu in cycle(text):
    if stop==5:
        break
    print(bu)
    stop+=1