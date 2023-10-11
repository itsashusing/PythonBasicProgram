# 38. Write a python program which will accept list of numerical values and short them in both
# ascending and descending order
# 39. Write a python program which will accept list of names and display
# them in both display them in both ascending and descending order.
print('Choose Your Option: ')
print('\t1. SORT NUMERICAL VALUES')
print('\t2. SORT NAMES VALUES')

ch = int(input('Enter Your choice: '))
match ch:
    case 1:
        n = int(input('How many number you want to enter: '))
        lst = []
        for i in range(1, n + 1):
            n1 = int(input('Enter {} value: '.format(i)))
            lst.append(n1)
        else:
            print('--' * 50)
            print('The list you entered is {}'.format(lst))
            lst.sort()
            print('*' * 50)
            print('Ascending order of list is {}'.format(lst))
            lst.sort(reverse=True)
            print('Descending order of list is {} '.format(lst))
            print('*' * 50)
    case 2:
        n = int(input('How many number you want to enter: '))
        lst = []
        for i in range(1, n + 1):
            n1 = input('Enter {} value: '.format(i))
            lst.append(n1)
        else:
            print('--' * 50)
            print('The list you entered is {}'.format(lst))
            lst.sort()
            print('*' * 50)
            print('Ascending order of list is {}'.format(lst))
            lst.sort(reverse=True)
            print('Descending order of list is {} '.format(lst))
            print('*' * 50)
