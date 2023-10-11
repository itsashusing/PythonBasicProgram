# 36. Write a python program which will accept list of numerical value and display the values
# 37. Write a python program which will accept list of numerical values and find the sum and average using loop .
n = int(input('Enter how many values you want to enter: '))
lst=[]
for i in range(1,n+1):
    ch=int(input('\tEnter {} value '.format(i)))
    lst.append(ch)
else:
    print('The list is {}'.format(lst))
    sum=0
    for s in lst:
        sum=sum+s
    else:
        print('The sum of {} is {} '.format(lst,sum))
        print('The average of {} is {}'.format(lst,sum/len(lst)))