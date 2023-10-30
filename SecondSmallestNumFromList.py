# 27. Write a Python program to find the second-smallest number in a list.
# 28. Write a Python program to find the second-largest number in a list.
n = int(input('Enter How many value you want to enter: '))
l1 = []
print('Enter Your First List')
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    l1.append(val)
else:
    print('\t Your list {}'.format(l1))
    l1.sort()
    print('\t Second smallest Number {}'.format(l1[1]))
    print('\t Second largest Number {}'.format(l1[-2]))
