# 51. Write a python program which will display 1 to N multiplication table
# where n is Positive Integer value

n= int(input('Enter a value: '))
for i in range(1,n+1):
    print('*' * 50)
    print('Table of {}'.format(i))
    print('*'*50)
    for j in range(1,11):
        print('{} X {} = {}'.format(i,j,i*j))
