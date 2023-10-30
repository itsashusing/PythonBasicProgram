# 19(a). Write a Python program to get the difference between digits of a list.
n = int(input('Enter How many value you want to enter: '))
l=[]
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    l.append(str(val))
else:
    print('Difference of list of Digits')
    for i,j in l:
        print('\t{}{}---> {}'.format(i,j,abs(int(i)-int(j))))
