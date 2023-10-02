# 3. Write a python program which will calculate area and parimeter of rectangle.
# ar= l*b
# pr= 2(l+b)
print('-' * 40)
l = float(input('Enter height of rectangle: '))
b = float(input('Enter width of rectangle: '))
print('-' * 40)
ar = l * b
pr = 2 * (l + b)
print('Area of rectangle is {}'.format(ar))
print('Parimeter of rectangle is {}'.format(pr))
print('-' * 40)