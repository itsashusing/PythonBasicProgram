# 41. Write a python program which will accept list of names from the keyboard and find their length
n = int(input('How many name you want to enter: '))
lst = []
for i in range(1, n + 1):
    na = input('Enter {} name: '.format(i))
    lst.append(na)
else:
    print('*'*50)
    print('\tList You entered is {}'.format(lst))
    print('*' * 50)
    for k in range(len(lst)):
        print('\t Length in ({}) -----> {} '.format(lst[k],len(lst[k])))
