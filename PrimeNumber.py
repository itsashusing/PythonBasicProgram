# 42.Write a python program which will accept any numerical integer value and decide weather
# it is prime number or not.
n = int(input('Enter a number: '))
res = 'Prime'
for i in range(2, n):
    if n % i == 0:
        res = 'Not Prime'
        break
print(res)
