# 4. Write a python program which will calculate simple interest and total amount to pay.
# si=prt/100
# amount= si+ p
print('-' * 40)
p = float(input('Enter Principal amount: '))
r = float(input('Enter Rate% : '))
t = float(input('Enter time: '))
print('-' * 40)
si = (p * r * t) / 100
am = si + p
print("Simple Interest of these value is {} ".format(si))
print('Total Amount to payable is {}'.format(am))
print('-' * 40)
