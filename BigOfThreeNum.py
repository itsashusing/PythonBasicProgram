#Program for accepting 3 values and find big among
a= float(input('Enter First value: '))
b= float(input('Enter Second value: '))
c= float(input('Enter third value: '))

res= a if a>b else b if b>c else c
print('Big of in {} , {} , {} is ---> {}'.format(a,b,c,res))