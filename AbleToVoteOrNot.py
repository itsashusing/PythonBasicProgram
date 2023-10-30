# 52.Write a python program Which  will accept the age of the citizen decide
# weather citizen able to vote or not.
while True:
    val= int(input('Enter age: '))
    if val >17:
        print('{} years You are Eligible To Vote'.format(val))
        break
    else:
        print('Invalid age Please Try again: ')
