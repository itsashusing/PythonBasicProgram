# 46. Write a Python program to select the odd items of a list.

n = int(input('Enter How many value you want to enter: '))
l1 = []
print('Enter Your First List')
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    if val%2!=0:
        l1.append(val)
print('Odds Item: ',l1)