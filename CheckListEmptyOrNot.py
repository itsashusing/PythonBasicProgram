# 8. Write a Python program to check a list is empty or not.
n= int(input('Enter How many value you want to enter: '))
l=[]
for i in range(1,n+1):
    val= int(input('Enter {} value: '.format(i)))
    l.append(val)
else:
    if len(l) == 0:
        print('List is Empty')
    else:
        print('List is Not Empty')