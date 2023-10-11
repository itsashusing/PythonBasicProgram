# 31. Write a python program which will find sum of first n natural number
n = int(input('Enter How many natural numbers sum you want to find: '))
s = 0
print('\t------- Using for loop--------')
for i in range(n + 1):
    s = s + i
else:
    print('\t sum of n number using for {} '.format(s))
print('-------- using while loop ----------')
s=0
i = 1
while i <= n:
    s = s + i
    i = i + 1
else:
    print('\t Sum of n Number using while {}'.format(s))
