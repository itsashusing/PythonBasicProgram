# 22. Write a Python program to find the index of an item in a specified list.

n = int(input('Enter How many value you want to enter: '))
l = []
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    l.append(val)
else:
    print(l.index(int(input('What value index you want '))))
