# 9. Write a Python program to clone or copy a list.
n = int(input('Enter How many value you want to enter: '))
l = []
cl = []
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    l.append(val)
else:
    for i in l:
        cl.append(i)
    else:
        print('\t Your List {},Memory Add.{} \n\t Cloned List {}, Memory Add. {}'.format(l, id(l), cl, id(cl)))
