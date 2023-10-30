# 60. Writ a python program which will accept numerical value which is given as below:
# and given a list of sum of the digit of each value
# 	lst=[234,13, 5673,3,345,890,15789]
# 	Expected output: reslist=[9,4,21,3,12,17,30]

n = int(input('How many list item you want to enter: '))
l = []
dl = []
i = 1
while i <= n:
    val = int(input('Enter {} value: '.format(i)))
    l.append(val)
    i += 1

for i in l:
    val = str(i)
    s = 0
    for j in val:
        s = s + int(j)
    else:
        dl.append(s)
print(l)
print(dl)
