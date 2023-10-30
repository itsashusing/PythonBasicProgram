# 12. Write a Python program to print a specified list after removing the
# 0th, 4th and 5th elements.
# 		Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# 		Expected Output : ['Green', 'White', 'Black']

n = int(input('Enter How Many item you want to Enter\n(Enter atleast 6 or more than 6): '))
l = []
if n < 6:
    print('Invalid Input N must be greater than 5')
else:
    for i in range(1, n + 1):
        val = input('Enter {} value: '.format(i))
        l.append(val)
for i,j in enumerate(l):
    print('{}:{}'.format(i,j),end=' ')
print('\nAfter Removing 0th, 4th, 5th Elements')
l.pop(0)
l.pop(3)
l.pop(3)
print(l)
