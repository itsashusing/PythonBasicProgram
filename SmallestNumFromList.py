# 4. Write a Python program to get the smallest number from a list.
n = int(input('Enter How many value you want to enter: '))
l = []
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    l.append(val)
else:
    print(l)
    l.sort(reverse=True)
    print('Smallest Number form the list Is-->', l[len(l) - 1])
