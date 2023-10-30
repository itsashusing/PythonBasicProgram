# 31. Write a Python program to count the number of elements
# in a list within a specified range.

n = int(input('Enter How many value you want to enter: '))
l1 = []
print('Enter Your First List')
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    l1.append(val)
print('\tYour List {} \n Number count between 1 to 20 '.format(l1))
for i in l1:
    if i in range(1, 20):
        print('\t{}-->{} times'.format(i, l1.count(i)))
