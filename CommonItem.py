# 37. Write a Python program to find common items from two lists.
n = int(input('Enter How many value you want to enter: '))
l1 = []
l2 = []
print('Enter Your First List')
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    l1.append(val)
print('Enter your Second List')
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    l2.append(val)
print('Common Items')
for i in l1:
    if i in l2:
        print(i,end=' ')
 