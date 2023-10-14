# 47. Write a python program which will accept list of numerical values
# and fine the sum of positive and negative values.
n = int(input('Enter How many value you want to Enter: '))
pl = []
nl = list()
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    if val >= 0:
        pl.append(val)
    else:
        nl.append(val)
else:
    print('*' * 50)
    print('\t Positive List {} \t Negative list {}'.format(pl, nl))
ps = 0
for i in pl:
    ps = ps + i
else:
    ns = 0
    for j in nl:
        ns = ns + j
    else:
        print('\t Sum of Positive Number {} \t Sum of Negative Number {}'.format(ps, ns))
