'''13. Write a python program which will accept two numerical value and
decide the biggest and check for equality.'''

a = float(input('Enter frist value: '))
b = float(input('Enter second value: '))

c = a if a > b else b if b > a else 'Both are equal'
print('Big of {} and {} is {}'.format(a, b, c))
