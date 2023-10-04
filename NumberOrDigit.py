#Program for accepting any value and decide whether It is Number or digit
a = int(input('Enter any Numerical value: '))
res = '+Digit' if a in (range(10)) else '-Digit' if a in (range(-9,0)) else'Number'
print('*' * 30)
print('The value {} is {}'.format(a,res))
