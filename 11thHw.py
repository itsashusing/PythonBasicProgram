# 11. Write a python progarm which will accept two value and swap then or interchange them.
a = input('Enter any value of a: ')
b = input('Enter any value of b: ')
print('*' * 30)
print('Before swaping value of a & b is ({} ,{}) '.format(a,b))
print('*' * 30)
a,b=b,a
print('Swapped value of a & b is ({} {})'.format(a,b))