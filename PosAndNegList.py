# 44. Write a python program which will accept list of numerical values and
# display only positive number.
# 45.Write a python program which will accept list of values from keyboard and
# display list of negative values.

n= int(input('Enter How many values you want to enter: '))
lst=list()

for i in range(1,n+1):
    val = int(input('Enter {} value: '.format(i)))
    lst.append(val)
print('Your List Is {}'.format(lst))
pos=[]
neg=[]
for i in lst:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

print('*'*50)
print("\n Positive Number is {}\n Negative Number is {}".format(pos, neg))