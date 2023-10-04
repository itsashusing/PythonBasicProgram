# Program for accepting 3 values and find big among them and check for equality
a = float(input('Enter First value: '))
b = float(input('Enter Second value: '))
c = float(input('Enter third value: '))
res = a if a >= b and a > c else b if b > a and b >= c else c if c >= a and c > b else 'All are euqal'
print('*' * 30)
print("Big of in {} , {} , {} is ---> {}".format(a, b, c, res))
