# 15. Write a Python program to shuffle and print a specified list.

n = int(input('Enter How many value you want to enter: '))

for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    l.add(val)

else:
    print(l,type(l),type(list(l)))
    print('Shuffle List is ',list(l))