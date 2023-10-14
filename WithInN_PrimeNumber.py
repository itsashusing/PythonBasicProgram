# 50. Write a python program which will list the prime number with in n
n = int(input("Enter a Number in which, U need prime numbers within in it: "))
if n > 1:
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=' ')
else:
    print("{} is Invalid Input".format(n))

