# 46.write a python program which will accept list of words and obtain only palindrome words.
n = int(input('How many values you want to enter: '))
lst = list()
pl = []
for i in range(n):
    val = input('Enter {} value: '.format(i))
    lst.append(val)
else:
    print('Your list is {}'.format(lst))
    print('*' * 50)
    for j in lst:
        if j == j[::-1]:
            pl.append(j)
    else:
        print('List of Palindrome Numbers is {}'.format(pl))
