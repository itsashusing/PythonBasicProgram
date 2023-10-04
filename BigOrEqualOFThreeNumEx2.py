# Program for accepting 3 values and find big among them and check for equality
a = float(input('Enter First value: '))
b = float(input('Enter Second value: '))
c = float(input('Enter third value: '))
res = a if b<=a>c else b if  a<b>=c else c if a<=c>b else "All are equal"
print('*' * 30)
print("Big of in {} , {} , {} is ---> {}".format(a, b, c, res))