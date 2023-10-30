# 35. Write a Python program to create a list by concatenating a given list
# which range goes from 1 to n.
# 	Sample list : ['p', 'q']
# 	n =5
# 	Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

sam_list = ['p', 'q']
flist = []
n = int(input('Enter n value '))
for i in range(n):
    flist.append(sam_list[0] + str(i + 1))
    flist.append(sam_list[1] + str(i + 1))

print(flist)
