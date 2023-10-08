# 24. Write a python program which will generate one to N numbers where N is Positive number.
# 25. Write a python program which will generate odd numbers within one to N
# 26. Write a python program which will generate even number within one to N.
print('*' * 50)
print('\t1. Generate N real numbers')
print('\t2. Generate N real Odd numbers')
print('\t3. Generate N real Even numbers')
print('*' * 50)
ch = int(input('Enter Your Choice: '))
match (ch):
    case 1:
        n = int(input('Enter N value: '))
        i = 1
        while (i <= n):
            print(i, end='')
            i = i + 1
        print('\n' + '*' * 50)
    case 2:
        n = int(input('Enter N value: '))
        i = 1
        while (i <= n):
            print(i, end='')
            i = i + 2
        print('\n' + '*' * 50)
    case 3:
        n = int(input('Enter N value: '))
        i = 0
        while (i <= n):
            print(i, end='')
            i = i + 2
        print('\n' + '*' * 50)
    case _:
        print('Inviled Input')
print('Program is Complete')
