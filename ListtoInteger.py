# 39. Write a Python program to convert a list of multiple integers into a single integer.
# 		Sample list: [11, 33, 50]
# 		Expected Output: 113350

n = int(input('Enter How many value you want to enter: '))
l1 = []
print('Enter Your First List')
for i in range(1, n + 1):
    val = int(input('Enter {} value: '.format(i)))
    l1.append(val)
s= ''
for i in l1:
    s= s + str(i)
s=int(s)
print(l1)
print(int(s),type(s))