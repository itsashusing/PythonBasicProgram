# 30. Write a Python program to get the frequency of the elements in a list.
n = int(input('Enter How many value you want to enter: '))
l1 = []
cv = {}
print('Enter Your First List')
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    l1.append(val)
else:
    for i in l1:
        cv[l1.count(i)]=i

print('\tYour List {} \n\tNumberOfTime:Value'.format(l1))
print('\t {}'.format(cv))
