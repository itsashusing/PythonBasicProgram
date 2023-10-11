# 17. Write a python program which
# will accept any numerical value and dicide it is even of odd by using simple if statement.

n = float(input('Enter any value: '))
print('*' * 30)
if (n % 2 == 0):
    print('{} is Even'.format(n))
if (n % 2 != 0):
    print('{} is Odd'.format(n))
print('Program Done')
print('*' * 30)
