list1=[1,'a',4,5,'b',4,'c']
b=len(list1)
list2=[]
for i in range (0,b-1,2):
    d=list1[i]
    if i-1<b:
        e=list1[i+1]
    else:
        break
    list2.append(e)
    list2.append(d)
if b%2!=0:
    list2.append(list1[b-1])
print(list2)