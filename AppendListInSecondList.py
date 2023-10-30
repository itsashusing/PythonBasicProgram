n = int(input('Enter How many value you want to enter: '))
l1 = []
l2 = []
print('Enter Your First List')
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    l1.append(val)
print('Enter Your Second List')
for i in range(1, n + 1):
    val = int(input('Enter {} value '.format(i)))
    l2.append(val)
print('\t List First {}\n\t List Second {}'.format(l1, l2))
print('~' * 50)
print('\t Final List after appending list2 in list1')
for i in l2:
    l1.append(i)
else:
    print('\t Final List {}'.format(l1))
