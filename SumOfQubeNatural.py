# 33. write a python program which will fine sum of qubes of first n natural numbers.
n= int(input('Enter how many natural number square of sum you want: '))
s=0
print('\t------- Using for loop--------')
for i in range(1,n+1):
    s=s+i**3
else:
    print('\t sum of qube till {} using for {} '.format(n,s))
print('-------- using while loop ----------')
s=0
i = 1
while i <= n:
    s = s + i**3
    i = i + 1
else:
    print('\t Sum of qube till {}  using while {}'.format(n,s))
