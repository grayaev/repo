user = 'Write, Run & Share Python code online using OneCompiler\'s Python online compiler for free. It\'s one of the robust'
word = []
count = 1

for el in range(user.count(' ')):
    word = user.split()
    if len(str(word)) <= 10:
        print(count, {word[el]})
        count += 1
    else:
        print (count, (word[el][0:10]))
        count += 1
