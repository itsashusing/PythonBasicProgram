# write a python program which will implement the following menu-driven application.
#  Arithmetic Operations Calculator
# 	1. Addition
# 	2. substraction
# 	3. Multiplication
# 	4. Division
# 	5. Modulo Division
# 	6. Exponentiation
# 	7.Exit
# ---------
# Enter your choice:
print('*' * 50)
print('Arithetic Operations Calculator')
print('\t1. Addition')
print('\t2. Subtraction')
print('\t3. Multiplication')
print('\t4. Division')
print('\t5. Modulo Division')
print('\t6. Exponentiation')
print('\t7. Exit')
print('*' * 50)
ch = int(input('Enter Your Choice: '))
match (ch):
    case 1:
        print('Enter Two values for Addition: ')
        a, b = int(input()), int(input())
        print('Addition of {},{} is----> {}'.format(a, b, a + b))
    case 2:
        print('Enter Two values for Subtraction: ')
        a, b = int(input()), int(input())
        print('Subtraction of {},{} is----> {}'.format(a, b, a - b))
    case 3:
        print('Enter Two values for Multiplication: ')
        a, b = int(input()), int(input())
        print('Multiplication of {},{} is----> {}'.format(a, b, a * b))
    case 4:
        print('Enter Two values for Division: ')
        a, b = int(input()), int(input())
        print('Division of {},{} is----> {}'.format(a, b, a / b))
        print('Floor division of {} ,{} is ----> {}'.format(a, b, a // b))
    case 5:
        print('Enter Two values for Modulo Division: ')
        a, b = int(input()), int(input())
        print('Modulo of {},{} is----> {}'.format(a, b, a % b))
    case 6:
        print('Enter Two values for Exponentiation: ')
        a, b = int(input('Base value: ')), int(input('Power Value: '))
        print('Exponentiation of {},{} is----> {}'.format(a, b, a ** b))
    case 7:
        print('Thanks for using program')
    case _:
        print('Your choice is not match form above list. Please try again')
print('*' * 50)
print('Match Case Example Completed')
