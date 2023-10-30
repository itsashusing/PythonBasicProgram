# 40. Write a Python program to split a list based on first character of word.

n = int(input('Enter How many value you want to enter: '))
l1 = []
keylst={}
print('Enter Your First List')
for i in range(1, n + 1):
    val = input('Enter {} value: '.format(i))
    l1.append(val)
for i in l1:
    keylst[i[0]]=i
for k,v in keylst.items():
    print('\t{}\t-->{}'.format(k,v))

