# 29. Write a Python program to get unique values from a list.
n = int(input('Enter How many value you want to enter: '))
l1 = []
uv=[]
print('Enter Your First List')
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    l1.append(val)
else:
    for i in l1:
        if l1.count(i)==1:
            uv.append(i)
    else:
        print('Unique Values {}'.format(uv))