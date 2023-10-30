# 47. Write a Python program to insert an element before each element of a list.
n = int(input('Enter How many value you want to enter: '))
l1 = []
nl=[]
print('Enter Your First List')
for i in range(1, n + 1):
    val = input('Enter {} value: '.format(i))
    l1.append(val)
n= input('What value you want to insert : ')
for i in l1:
    nl.append(n)
    nl.append(i)
print(nl)