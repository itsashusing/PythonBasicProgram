# 28. Write a python program which will generate 1 to N numbers  n is +ve . BY using for loop.
# 29. Write a python program which will generate N to 1 numners by using for loop.
n = int(input('Enter How many Values till you want: '))
if n<=0:
    print('Invalid Number')
else:
    print('-----------------')
    print('1 to  N numbers')
    for i in range(1,n+1):
        print(i,end=' ')
    print('\n',end='-------------------\n')
    print('Reverse Of N numbers')
    for j in range(n,0,-1):
        print(j,end=' ')

