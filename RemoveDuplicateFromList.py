# 7. Write a Python program to remove duplicates from a list.
n= int(input('Enter How many value you want to enter: '))
l=[]
nl=[]
for i in range(1,n+1):
    val= int(input('Enter {} value: '.format(i)))
    l.append(val)
else:
    for i in l:
        if i in nl:
            continue
        else:
            nl.append(i)
print('~'*50)
print('\t Original list {} \n\t Unique List {} '.format(l,nl))
print('~'*50)
