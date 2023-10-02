# 10. Write a python program which will evaluate a^m/a^n
a= float(input('Enter a: '))
m= float(input('Enter m: '))
n= float(input('Enter n: '))

print('*' * 30)
print('result of a to the power of n upon a to the power of m is (a^n/a^m) = {}'.format((a**n)/(a**m)))
print('*' * 30)