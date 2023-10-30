# 14. Write a Python program to print the numbers of a specified list
# after removing even numbers from it.
n = int(input('Enter How many value you want to enter: '))
el = []
l=[]
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    l.append(val)
    if val %2!=0:
        el.append(val)
else:
    print('User Enter The list: ',l)
    print('After removing Even Numbers {}'.format(el))
