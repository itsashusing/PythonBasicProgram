# 30. Generate odd even number using for loop
print('-' * 50)
n= int(input('Enter How many values till you want: '))
if n<=0:
    print('Invalid Input value less than Or equal to Zero')
else:
    print('-'*50)
    print('Even Values')
    for i in range(0,n+1,2):
        print(i,end=' ')
    print('\n',end='----------------\n')
    print('Odd values')
    for j in range(1,n+1,2):
        print(j,end=' ')
