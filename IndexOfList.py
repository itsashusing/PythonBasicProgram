# 20. Write a Python program access the index of a list.
n = int(input('Enter How many value you want to enter: '))
l=[]
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    l.append(str(val))
else:
    for i,j in enumerate(l):
        print('Index {}, Value {}'.format(i,j))