# 32. Write a python program which will find sum of square of first n natural numbers.
n= int(input('Enter how many natural number square of sum you want: '))
s=0
print('\t------- Using for loop--------')
for i in range(1,n+1):
    s=s+i**2
else:
    print('\t sum of square n using for {} '.format(s))
print('-------- using while loop ----------')
s=0
i = 1
while i <= n:
    s = s + i**2
    i = i + 1
else:
    print('\t Sum of square fo n  using while {}'.format(s))
