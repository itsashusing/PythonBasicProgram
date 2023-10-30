# 1. Write a Python program to sum all the items in a list.
n= int(input('Enter How many value you want to enter: '))
l=[]
s=0
for i in range(1,n+1):
    val= int(input('Enter {} value: '.format(i)))
    l.append(val)
else:
    for i in l:
        s=s+i
    else:
        print('~'*30)
        print('\tSum Of List is {}'.format(s))
        print('~' * 30)