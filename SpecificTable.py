ls = []
while True:
    n = int(input('Enter number/ press (0) for stop: '))
    if n == 0:
        break
    else:
        ls.append(n)
print(ls)

for j in ls:
    print('*' * 40)
    for i in range(1, 11):
        print('{} X {} = {}'.format(j, i, j * i))
