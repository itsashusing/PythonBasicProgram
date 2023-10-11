# 34. Write a python program which will find the product of first n natural numbers.
# 35. Write a python program which will calculate factorial of a given number.

n = int(input('Which num you want to calculate factorial: '))
if n<0:
    print('invalid Input')
else:
    s=1
    for i in range(1,n+1):
        s=s*i
        print(i,end=' ')
    else:
        print('\n-----------------------------')
        print('{} <------factorial of {}'.format(s,n))
        print('------------------------------')
    s = 1
    for i in range(n,0,-1):
        s = s * i
        print(i, end=' ')
    else:
        print('\n-----------------------------')
        print('{} <------factorial of {}'.format(s, n))
        print('------------------------------')